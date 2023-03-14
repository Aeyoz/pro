# *******************
# CREANDO OPERACIONES
# *******************

def make_oper(sign: str):
    def mathmatical_operation(num1: int, num2: int) -> int|None:
        operations = ["add", "sub", "mul", "div"]
        if sign in operations:
            if sign == "add":
                return num1 + num2
            if sign == "sub":
                return num1 - num2
            if sign == "mul":
                return num1 * num2
            if sign == "div":
                return num1 / num2
        return None
    return mathmatical_operation

def run(oper: str, num1: int, num2: int) -> int|float|None:
    operation = make_oper(oper)
    result = operation(num1, num2)
    return result