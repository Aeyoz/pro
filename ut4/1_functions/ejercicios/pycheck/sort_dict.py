# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
    '''Function that sorts a dictionary by the value instead of the key
    :param unsorted_items: A bunch of elements with a value associated.

    :type unsorted_items: dict
    :return: sorted_items
    :rtype: list[tuple]
    '''
    sorted_items = sorted(unsorted_items.items(), key=lambda d: d[1])
    return sorted_items


if __name__ == '__main__':
    run({'a': 'two', 'b': 'one', 'c': 'three'})