# *******************************
# VENTAS EN TIENDA DE INFORMÁTICA
# *******************************


def run(sales: list) -> tuple:
    pcs = 0 
    displays = 0
    if len(sales) > 0:
        for component in sales:
            pcs += component[0]
            displays += component[1]
    return pcs, displays


if __name__ == '__main__':
    run([[4, 5], [1, 3], [3, 2]])
