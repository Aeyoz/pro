'''
El objetivo es encontrar el primer número no consecutivo dentro de una lista de valores
numéricos enteros. Si todos los valores son consecutivos entonces el resultado es None.
'''


def run(values: list) -> int:
    for i,j in zip(values,values[1:]):
        if (i + 1) != j:
            target = j
            break
    else:
        target = None
    return target


if __name__ == '__main__':
    run([1, 2, 3, 4, 6, 7, 8])
