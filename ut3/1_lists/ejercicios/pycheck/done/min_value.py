'''
Dada una lista de valores numéricos enteros, obtenga su mínimo valor.

Prohibido utilizar:
- La función "built-in" min().
- La función "built-in" sorted().
'''


def run(values: list) -> int:
    min_value = values[0]
    for i in values[1:]:
        if i < min_value:
            min_value = i
    return min_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])
