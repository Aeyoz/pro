# **********************
# MEZCLANDO DICCIONARIOS
# **********************


def run(d1: dict, d2: dict) -> dict:
    merged = d1.copy()
    for k, v in d2.items():
        merged[k] = v
    return merged


if __name__ == '__main__':
    run({'a': 1, 'b': 2}, {'a': 3, 'c': 4})