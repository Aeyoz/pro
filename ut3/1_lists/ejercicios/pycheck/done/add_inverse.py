'''
Dada una lista de valores numéricos, obtenga la suma de los valores invertidos.
'''


def run(numbers: list) -> int:
    add_inv = 0
    for num in numbers:
        add_inv += num
    add_inv = -add_inv
    return add_inv


if __name__ == '__main__':
    run([1, 2, 3, 4, 5])
