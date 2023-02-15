# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


def cfreq(values, as_string=False):
    output = []
    counter = 0

    if not values:
        if not as_string:
            return output
        elif as_string:
            return ""
    prev_v = values[0]
    
    for value in values[1:]:
        counter += 1
        if value != prev_v:
            output.append((prev_v, counter))
            prev_v = value
            counter = 0
    counter += 1
    output.append((prev_v, counter))
    
    if not as_string:
        return output
    else:
        freqs = []
        for t in output:
            item1, item2 = t
            freqs.append(f"{item1}:{item2}")
        freq = ",".join(freqs)
        return freq