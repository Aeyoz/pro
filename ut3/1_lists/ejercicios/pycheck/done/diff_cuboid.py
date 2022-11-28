'''
Como datos de entrada tendrá dos listas representando las dimensiones de sendos cuboides:
   o--------o
  / c      /|
 /        / | b
o--------o  |      ---> [a, b, c]
|        |  o
|        | /
|    a   |/
o--------o

Debe calcular la diferencia de volumen entre los dos cuboides como valor positivo,
indpendientemente de qué cuboide sea mayor.
'''


def run(cuboid1: list, cuboid2: list) -> float:
    cube1 = [float(i) for i in cuboid1]
    cube2 = [float(j) for j in cuboid2]
    c1_vol = 1
    c2_vol = 1
    for i,j in zip(cube1,cube2):
        c1_vol *= i
        c2_vol *= j
    vol_diff = abs(c1_vol - c2_vol)
    return vol_diff


if __name__ == '__main__':
    run([2, 2, 3], [5, 4, 1])
