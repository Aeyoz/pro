# ***********************
# SUMANDO CON ANIDAMIENTO
# ***********************


def sum_nested(items: list[int|list], additions=0) -> int:
    if isinstance(items[0], list):
        return sum_nested(items[0], additions+0)
    else:
        additions += 1
    return sum_nested(items[1:], additions+0)

print(sum_nested([1, [2, 4], 5, [6, [7, 8]]]))