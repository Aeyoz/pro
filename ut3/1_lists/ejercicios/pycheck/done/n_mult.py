'''
Genere una lista on los "n" primeros múltiplos de "x", donde "n" y "x" son parámetros de
entrada representando valores enteros mayores que 0.

Resuelva el ejercicio utilizando listas por comprensión.
'''


def run(x: int, n: int) -> list:
    multiples = [n * x for n in range(1, n + 1)]
    return multiples
