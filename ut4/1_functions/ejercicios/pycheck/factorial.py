# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************

def factorial(n):
    if n < 0:
        return None
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod