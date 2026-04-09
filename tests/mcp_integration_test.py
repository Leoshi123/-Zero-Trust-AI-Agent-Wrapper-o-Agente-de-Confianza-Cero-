import subprocess
import json
import time
import os
import pytest
from pathlib import Path

# Configuration
SERVER_SCRIPT = "src/mcp_server.py"
TIMEOUT = 10  # Seconds for each test payload

def launch_server():
    """Launches the MCP server as a subprocess in stdio mode."""
    return subprocess.Popen(
        ["python", SERVER_SCRIPT, "stdio"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

def send_payload(process, payload):
    """Sends a JSON-RPC payload to the server and reads the response."""
    process.stdin.write(json.dumps(payload) + "\n")
    process.stdin.flush()

    # Read until we see a complete JSON response or timeout
    response_data = ""
    start_time = time.time()
    while time.time() - start_time < TIMEOUT:
        line = process.stdout.readline()
        if line:
            response_data += line
            try:
                json.loads(response_data)
                return json.loads(response_data)
            except json.JSONDecodeError:
                continue
    return None

def test_server_resilience():
    """
    THE TORTURE TEST: Sends a series of malformed and aggressive payloads
    to ensure the server never crashes.
    """
    print("\nStarting MCP Server Torture Test...")
    process = launch_server()

    # Wait for server to start
    time.sleep(2)

    # 1. Poison Pill: Completely malformed JSON
    print("Sending poison pill (malformed JSON)...")
    process.stdin.write("{'invalid': 'json', missing_quotes: 123}\n")
    process.stdin.flush()
    time.sleep(1)

    # 2. Massive Payload: Giant string to test memory/buffer boundaries
    print("Sending oversized payload (1MB of garbage)...")
    giant_code = "print('hello')\n" * 50000
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {"name": "sanitize_code", "arguments": {"code": giant_code}},
        "id": 1
    }
    response = send_payload(process, payload)
    assert response is not None, "Server crashed or timed out on oversized payload"
    print("SUCCESS: Server survived oversized payload")

    # 3. AST Bomb: Malformed nested syntax to test ASTExtractor resilience
    print("Sending AST bomb (malformed nested brackets)...")
    ast_bomb = "(" * 1000 + "print(1)" + ")" * 1000
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {"name": "prune_context", "arguments": {"code": ast_bomb}},
        "id": 2
    }
    response = send_payload(process, payload)
    assert response is not None, "Server crashed on AST bomb"
    print("SUCCESS: Server survived AST bomb")

    # 4. Timeout Test: Verifying server health after attacks
    print("Verifying server health after attacks...")
    health_payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {"name": "clean_code", "arguments": {"code": "print('alive')"}},
        "id": 3
    }
    response = send_payload(process, health_payload)
    assert response is not None, "Server died after adversarial attacks"
    print("SUCCESS: Server is still alive and responsive")

    process.terminate()
    print("\nTorture Test Passed: Server is INDESTRUCTIBLE.")

if __name__ == "__main__":
    try:
        test_server_resilience()
    except Exception as e:
        print(f"\nTORTURE TEST FAILED: {e}")
        exit(1)
