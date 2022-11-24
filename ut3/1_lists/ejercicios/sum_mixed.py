'''
Dada una lista de enteros y enteros como cadenas de texto, calcule la suma de todos los
valores de la lista como si todos sus elementos fueran números.
'''


def run(items: list) -> int:
    sum_items = sum([int(item) for item in items])
    return sum_items
