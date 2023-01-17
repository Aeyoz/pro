# **********************
# BORRANDO VALORES CLAVE
# **********************


def run(items: dict) -> dict:
    citems = {item:list() for item in items}
    return citems


if __name__ == '__main__':
    run({'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]})
