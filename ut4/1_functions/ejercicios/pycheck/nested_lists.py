def _sum(items: list[int|list], additions=0) -> int:
    additions += items[0] if not isinstance(items[0], list) else sum(items[0]) 
    items = items[1:]
    if len(items) == 0:
        return additions
    return _sum(items, additions+0)

print(_sum([1,2,[1,2],4,5,[6,7,8]]))