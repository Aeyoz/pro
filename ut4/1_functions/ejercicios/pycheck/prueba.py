value = []

def all_same(args):
    if len(args) >= 2:
        for item1, item2 in zip(args, args[1:]):
            if item1 != item2:
                return False
        return True

def consecutive_seq(items, target_count, n=1):
    piece = items[:target_count]
    if all_same(piece):
        return piece[0]
    if all_same(piece) == None:
        return False
    items = items[1:]
    return consecutive_seq(items, target_count)

#print(consecutive_seq([1, 74, 56, 56, 56, 332, 8, 8, 8], 3))
#print(consecutive_seq([1, 10, 20, 30, 30, 30, 30, 30, 40, 50], 5))
#print(consecutive_seq([11, 9, 20, 71, 51, 51, 2, 4, 4, 4, 4], 4))
print(consecutive_seq([77, 16, 99, 21, 1], 2))