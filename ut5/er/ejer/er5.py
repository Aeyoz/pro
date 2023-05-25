import re

operation = "4 +++ 4 99"

er = r"\d*\s*[\+\-\*\/]*\s*\d*"

def get_float(num):
    return re.findall(er, num)


print(get_float(operation))