# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************

def consecutive_seq(items: list[int], target_count: int = 3) -> int:
    def helper(items: list[int], last_seen: int = None, count: int = 0):
        if len(items) == 0:
            return False
        current_item = items[0]
        count = count + 1 if current_item == last_seen else 1
        if count == target_count:
            return current_item
        return helper(items[1:], current_item, count)
    return helper(items)

#def consecutive_seq(items, target_count, reps=1):
#    if len(items) == 1:
#        return False
#    reps = 1 if items[0] != items[1] else reps + 1
#    if reps == target_count:
#        return items[0]
#    return consecutive_seq(items[1:], target_count, reps+0)

#def consecutive_seq(items, target_count, counter=0):
#    if items[:target_count].count(items[:target_count][0]) == target_count:
#        return items[:target_count][0]
#    if len(items[:target_count]) <= 1:
#        return False
#    return consecutive_seq(items[1:], target_count, counter)
