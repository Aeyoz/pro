'''
Dada una lista de números enteros positivos y un número no negativo N, calcule el valor del
elemento en la posición N elevado a N.

Ejemplo:
[1, 2, 3, 4] y N=2, el resultado sería 3^2 = 9

Notas:
- Si N está fuera de rango, hay que devolver el valor -1.
- N se representa por "power" en el parámetro de entrada.
'''

def run(values: list, power: int) -> int:
    if power >= len(values):
        result = -1
    else:
        result = values[power] ** power 
    return result