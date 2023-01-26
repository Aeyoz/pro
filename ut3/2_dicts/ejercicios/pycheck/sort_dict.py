# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
    dvalues = [f"{v}:{k}" for k, v in unsorted_items.items()]
    dvalues.sort()
    sorted_items = []
    for value in dvalues:
        v, k = value.split(":")
        sorted_items.append((k,v))
    return sorted_items


if __name__ == '__main__':
    run({'a': 'two', 'b': 'one', 'c': 'three'})