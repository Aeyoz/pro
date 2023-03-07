# *******************************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO (CON RECURSIVIDAD)
# *******************************************************


def factorial(n: int) -> int|None:
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)