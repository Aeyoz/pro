# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************

def cfreq(values, as_string=False):
    freqs = []
    counter = 0

    if len(values) > 0:
        prev_v = values[0]
        for value in values[1:]:
            counter += 1
            if value != prev_v:
                freqs.append((prev_v, counter))
                prev_v = value
                counter = 0
        counter += 1
        freqs.append((prev_v, counter))

    if as_string:
        freqs = ",".join([f"{i}:{f}" for i, f in freqs])
    return freqs