# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************

def consecutive_seq(items, target_count, reps=1):
    if len(items) == 1:
        return False
    reps = 1 if items[0] != items[1] else reps + 1
    if reps == target_count:
        return items[0]
    return consecutive_seq(items[1:], target_count, reps+0)