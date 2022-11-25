'''
Dado un número entero no negativo "n", obtenga una lista con los números desde "n" hasta 1.
'''


def run(n: int) -> list:
    rev_nums = []
    for i in range(n, 0, -1):
        rev_nums.append(i)
    return rev_nums


if __name__ == '__main__':
    run(5)
