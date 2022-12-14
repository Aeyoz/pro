# ***************************
# BUSCANDO LA MAYOR DISTANCIA
# ***************************


def run(values: list, target: int) -> int:
    max_diff = 0
    for value in values:
        if abs(target - value) > max_diff:
            max_diff = abs(target - value) 
    return max_diff


if __name__ == '__main__':
    run([7, 3, 1, 12, 21, 4], 8)



