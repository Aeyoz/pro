# ***************
# TUPLA DE DUPLAS
# ***************


def run(input: tuple) -> set:
    set1, set2 = set(), set()
    for f_element, s_element in input:
        set1.add(f_element)
        set2.add(s_element)
    output = set1, set2
    return output


if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))

