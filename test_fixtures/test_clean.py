import ast
import subprocess

def safe_eval(data):
    try:
        return ast.literal_eval(data)
    except (ValueError, SyntaxError):
        return None


def run_command_safe(cmd_list):
    if not isinstance(cmd_list, list):
        raise ValueError("Command must be a list")
    return subprocess.run(cmd_list, capture_output=True, shell=False)


# Test functions
if __name__ == "__main__":
    print("Testing safe_eval with '123':", safe_eval("123"))
    print("Testing safe_eval with '[1,2,3]':", safe_eval("[1,2,3]"))
    print("Testing safe_eval with 'invalid':", safe_eval("invalid"))
