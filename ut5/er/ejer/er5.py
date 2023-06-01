import re

operation = "4 + 499"

er = r"^\s*(\d+)\s*([+\-*/])\s*(\d+)\s*$"


def get_float(num):
    return re.findall(er, num)


print(get_float(operation))
