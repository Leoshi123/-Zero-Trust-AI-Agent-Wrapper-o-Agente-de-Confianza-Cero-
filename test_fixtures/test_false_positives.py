# Test file for FALSE POSITIVES
# Safe code that might be incorrectly flagged

# Example 1: Math calculator using eval safely

import subprocess
# Safe: literal eval alternative
import ast

def calculate(expression):
    """Simple calculator - input is strictly controlled"""
    # Only allow digits and operators
    allowed = set("0123456789+-*/.() ")
    if any(c not in allowed for c in expression):
        return "Invalid characters"
    return eval(expression)  # This is intentional and safe


# Example 2: Shell command hardcoded (no user input)
def run_lint():
    """Run linter with hardcoded command"""
    subprocess.run("pylint myapp", shell=True)  # Hardcoded, no injection possible

ast.literal_eval("1 + 2")  # safe parsing

# Safe: subprocess without shell
subprocess.run(["ls", "-l"])  # no shell=True

# Safe: escaped HTML
# element.innerHTML = escape(user_input)

