def find_item(items: tuple, value: int = 2) -> int:
    """ Find how many times a value is found in a tuple of items.
    :param items: tuple to be iterated
    :type items: tuple
    :param value: Value to be found
    :type value: int

    :return: repeated
    :rtype: int
    """
    repeated = len([item for item in items if item == value])
    return repeated

print(find_item((1, 2, 2, 3, 4, 5, 6, 2, 3, 2, 99, 7, 4, 5, 7), 99))
print(find_item((1, 2, 2, 3, 4, 5, 6, 2, 3, 2, 99, 7, 4, 5, 7), 3))
print(help(find_item))