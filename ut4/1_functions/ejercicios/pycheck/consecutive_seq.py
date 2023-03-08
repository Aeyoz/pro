# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************

def all_same(args):
    if len(args) >= 2:
        for item1, item2 in zip(args, args[1:]):
            if item1 != item2:
                return False
        return True

def consecutive_seq(items, target_count, counter=0):
    piece = items[:target_count]
    if all_same(piece):
        return piece[0]
    if all_same(piece) == None:
        return False
    items = items[1:]
    return consecutive_seq(items, target_count, counter+1)