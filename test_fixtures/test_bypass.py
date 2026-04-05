# Test file for bypass attempts
import os
import subprocess

# BYPASS 1: eval() with string concatenation
code = "ev" + "al"
result = eval(code + "(user_input)")

# BYPASS 2: getattr to access eval
getattr_evil = getattr(__builtins__, "eval")
result2 = getattr_evil("1 + 1")

# BYPASS 3: subprocess import dynamically
subprocess_module = __import__("subprocess")
result3 = subprocess_module.run("ls", shell=True)

# BYPASS 4: API key with different format
# Base64 encoded: AKIAIOSFODNN7EXAMPLE1234
import base64

encoded = base64.b64encode(b"AKIAIOSFODNN7EXAMPLE1234").decode()

# BYPASS 5: Fragmented secret
part1 = "ghp_xxxx"
part2 = "xxxxxxxxxxxxxx"
full_secret = part1 + part2
