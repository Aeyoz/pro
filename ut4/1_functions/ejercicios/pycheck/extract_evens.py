# *******************
# EXTRACCIÓN DE PARES
# *******************


def run(nums) -> list:
    evens = [num for num in nums if num % 2 == 0]
    return evens