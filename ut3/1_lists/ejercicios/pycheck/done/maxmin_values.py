'''
Dada una lista de valores numéricos, encuentre el valor máximo y el valor mínimo de la
misma. No se pueden utilizar las funciones "built-in" max() y min(), y tampoco sorted().
'''


def run(values: list) -> tuple:
    max_value = values[0]
    min_value = values[0]
    for value in values[1:]:
        if value > max_value:
            max_value = value
        elif value < min_value:
            min_value = value
    return max_value, min_value


if __name__ == '__main__':
    run([4, 6, 2, 1, 9, 63, -134, 566])
