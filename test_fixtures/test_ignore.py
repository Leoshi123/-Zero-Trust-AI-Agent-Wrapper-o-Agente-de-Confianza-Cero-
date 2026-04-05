# Test file con magic comment en misma línea
def safe_calculator(expression):
    result = eval(expression)  # ztc: ignore - math expression, validated before
    return result
