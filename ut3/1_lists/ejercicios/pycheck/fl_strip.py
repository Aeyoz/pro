'''
Partiendo de una cadena de texto con números separados por comas, obtenga una nueva cadena
de texto donde se elimine el primer y el último número, y los elementos aparezcan separados
por espacios.
'''


def run(numbers: str) -> str:
    numbers = numbers.replace(",", " ")
    stripped = numbers[1:-1].strip()
    num_list = []
    num_list.extend(stripped)
    strip_numbers = "".join(num_list)
    return strip_numbers


if __name__ == '__main__':
    run('1,2,3')
