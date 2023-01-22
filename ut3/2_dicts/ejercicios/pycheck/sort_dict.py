# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
    sorted_items = []
    same_key_items = []
    unsorted_items_2 = {}
    for key, value in unsorted_items.items():
        if value not in unsorted_items_2:
            unsorted_items_2[value] = key
        else:
            same_key_items.append(tuple((key,value)))
    sorted_values = sorted(list(unsorted_items_2.items()))
    values = {tupple[1]:tupple[0] for tupple in sorted_values}
    if len(same_key_items) > 0:
        for t in same_key_items:
            key = t[0]; value = t[1]; values[key] = value
    sorted_items = list(values.items())
    return sorted_items


if __name__ == '__main__':
    run({'a': 'two', 'b': 'one', 'c': 'three'})