'''
Dado un número entero no negativo, genere una lista con los dígitos de dicho número
en orden inverso.
'''


def run(number: int) -> list:
    number = str(number)[::-1]
    rev_digits = []
    rev_digits.extend(number)
    rev_digits = [int(i) for i in rev_digits]
    return rev_digits


if __name__ == '__main__':
    run(35231)
    