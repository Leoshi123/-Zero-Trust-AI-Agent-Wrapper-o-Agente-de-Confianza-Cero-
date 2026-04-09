# =============================================================================
# ZTC-Wrapper Integration for Nova AI
# 
# Nova is an AI coding assistant. Configure it to use ZTC-Wrapper.
# =============================================================================

# Install ZTC-Wrapper first
# ./install.sh  # or install.ps1 on Windows

# METHOD 1: Nova Configuration
# Add to ~/.novarc or project .nova/config:

"""
[ztc]
enabled = true
python_path = python
project_root = .

# Security settings
block_on_critical = true
prune_context = true
sanitize_input = true
sanitize_output = true

[ztc.security]
scan_on_generate = true
auto_scan_patterns = "eval,exec,pickle,yaml,subprocess"
allowed_severities = "LOW,MEDIUM"

[ztc.pruning]
enabled = true
reduction_target = 70
include_signatures = true
"""

# METHOD 2: Nova Hook System
# Create a pre-generation hook:

"""
# File: ~/.nova/hooks/pre_generate.py
#!/usr/bin/env python3
import sys
import subprocess

def pre_generate_hook(code_context):
    """Run ZTC-Wrapper before AI generates code"""
    # Sanitize input
    result = subprocess.run(
        ["python", "-m", "src.cli", "sanitize", "clean", code_context],
        capture_output=True,
        text=True
    )
    return result.stdout if result.returncode == 0 else code_context
"""

# METHOD 3: Nova Security Plugin
# File: ~/.nova/plugins/ztc_security.py

"""
# ZTC-Wrapper Security Plugin for Nova
# Place in: ~/.nova/plugins/ztc_security.py

import subprocess
import json

class ZTCSecurityPlugin:
    name = "ztc-security"
    version = "1.0.0"
    
    def __init__(self, config):
        self.config = config
        self.block_critical = config.get("block_on_critical", True)
    
    def on_code_generated(self, code: str) -> dict:
        '''Validate generated code'''
        # Run security scan
        result = subprocess.run(
            ["python", "-m", "src.cli", "shield", "scan", "-"],
            input=code,
            capture_output=True,
            text=True
        )
        
        return {
            "allowed": result.returncode == 0 or not self.block_critical,
            "scan_result": result.stdout,
            "sanitized_code": self._sanitize(code)
        }
    
    def on_code_received(self, code: str) -> str:
        '''Sanitize received code'''
        return self._sanitize(code)
    
    def _sanitize(self, code: str) -> str:
        result = subprocess.run(
            ["python", "-m", "src.cli", "sanitize", "clean"],
            input=code,
            capture_output=True,
            text=True
        )
        return result.stdout if result.returncode == 0 else code

# Register the plugin
PLUGIN = ZTCSecurityPlugin
"""

# METHOD 4: Environment Variables
# Add to your shell profile (~/.bashrc, ~/.zshrc):

"""
# ZTC-Wrapper for Nova
export ZTC_ENABLED=true
export ZTC_PYTHON=python
export ZTC_PROJECT_ROOT=.
export ZTC_BLOCK_CRITICAL=true
export ZTC_PRUNE_CONTEXT=true
export NOVA_USE_ZTC=true
"""

# Run a security check with Nova context
echo "Example: Scan Nova's generated code"
echo 'python -m src.cli shield scan --block file.py'