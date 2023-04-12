# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


def cfreq(items, /, as_string=False) -> list:
    freqs = []
    counter = 1
    if len(items) > 0:
        prev = items[0]
        for item in items[1:]:
            if item != prev:
                freqs.append((prev, counter))
                prev = item
                counter = 1
            else:
                counter += 1
        freqs.append((prev, counter))
    if as_string:
        freqs = ",".join([f"{num}:{freq}" for num, freq in freqs])
    return freqs
