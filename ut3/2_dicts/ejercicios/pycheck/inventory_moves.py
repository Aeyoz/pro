# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    inventory = {}
    moves = imoves.split(",")
    for element in moves:
        position = element[0]
        cuantity = int(element[1:])
        if position not in inventory:
            inventory[position] = cuantity
        else:
            inventory[position] += cuantity
    return inventory


if __name__ == '__main__':
    run('A1,B4,A-2,A7,B1,C4')
