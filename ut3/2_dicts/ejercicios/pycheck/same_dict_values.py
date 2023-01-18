# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:
    for item1, item2 in zip(items.values(), list(items.values())[1:]):
        if item1 != item2:
            all_same = False
            break
    else:
        all_same = True
    return all_same


if __name__ == '__main__':
    run({'a': 1, 'b': 1, 'c': 1, 'd': 1})
