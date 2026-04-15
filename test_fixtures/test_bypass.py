# Test file for bypass attempts
import os
import subprocess
import base64
import importlib
import builtins

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

encoded = base64.b64encode(b"AKIAIOSFODNN7EXAMPLE1234").decode()

# BYPASS 5: Fragmented secret
part1 = "ghp_xxxx"
part2 = "xxxxxxxxxxxxxx"
full_secret = part1 + part2

# BYPASS 6: Using globals() to reach eval indirectly
evil = globals()["__builtins__"]["eval"]
result = evil("2 + 2")

# BYPASS 7: Using locals() trick
def test():
    ev = "eval"
    return locals()[ev]("3 + 3")

# BYPASS 8: Obfuscated function name via join
fn_name = "".join(["e", "v", "a", "l"])
result = getattr(__builtins__, fn_name)("4 + 4")

# BYPASS 9: Using compile + exec instead of eval
code = compile("print('bypass')", "<string>", "exec")
exec(code)

# BYPASS 10: Indirect import using importlib
sub = importlib.import_module("subprocess")
sub.run(["echo", "hello"])

# BYPASS 11: Using __builtins__.__dict__
evil = __builtins__.__dict__["eval"]
result = evil("5 + 5")

# BYPASS 12: Lambda execution trick
evil = (lambda x: eval(x))
result = evil("6 + 6")

# BYPASS 13: Hidden exec via function default argument
def sneaky(cmd, runner=exec):
    runner(cmd)

sneaky("print('hidden exec')")

# BYPASS 14: Encoding payload in hex
payload = "6576616c2822372b372229"  # "eval('7+7')" in hex
decoded = bytes.fromhex(payload).decode()
eval(decoded)

# BYPASS 15: Double base64 encoding
payload = base64.b64encode(base64.b64encode(b"eval('8+8')")).decode()
decoded = base64.b64decode(base64.b64decode(payload)).decode()
eval(decoded)

# BYPASS 16: Using exec inside eval
eval("exec('print(9+9)')")

# BYPASS 17: Using getattr on modules indirectly
mod = __import__("builtins")
getattr(mod, "eval")("10 + 10")

# BYPASS 18: Splitting dangerous keywords across variables
a = "ev"
b = "al"
getattr(__builtins__, a + b)("11 + 11")

# BYPASS 19: Using map to execute
list(map(eval, ["12 + 12"]))

# BYPASS 20: Using filter trick
list(filter(lambda x: exec("print(13+13)") or True, [1]))

# BYPASS 21: Environment variable injection
os.environ["PAYLOAD"] = "print(14+14)"
exec(os.environ["PAYLOAD"])

# BYPASS 22: Using setattr to override safe function
setattr(builtins, "safe_eval", eval)
builtins.safe_eval("15 + 15")

# BYPASS 23: Using class __init__ side effects
class Evil:
    def __init__(self):
        exec("print(16+16)")

Evil()

# BYPASS 24: Using decorators to hide execution
def run(func):
    exec("print(17+17)")
    return func

@run
def harmless():
    pass

# BYPASS 25: Using exception handling to execute
try:
    raise Exception("print(18+18)")
except Exception as e:
    exec(str(e))
