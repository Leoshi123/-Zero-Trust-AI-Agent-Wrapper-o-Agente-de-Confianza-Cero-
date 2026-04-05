# Test file for FALSE POSITIVES
# Safe code that might be incorrectly flagged

# Example 1: Math calculator using eval safely
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


# Example 3: HTML content from trusted source
def render_static_content():
    """Render static HTML that we control"""
    element = document.getElementById("content")
    element.innerHTML = "<h1>Welcome</h1>"  # Static, trusted content
