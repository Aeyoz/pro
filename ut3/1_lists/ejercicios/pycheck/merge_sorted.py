'''
Como datos de entrada dispone de dos listas con valores numéricos que ya vienen ordenadas.
Obtenga una lista de salida con la mezcla de las dos listas de entrada de forma ordenada.

NOTAS:
- No se puede utilizar la función sorted().
- No hay que realizar ninguna validación en los datos de entrada.
- Las listas de entrada pueden tener elementos repetidos.
- Las listas de entrada pueden tener distinto tamaño.
- Las listas de entrada pueden tener elementos comunes. Elimine los duplicados en la lista
de salida.
'''

def run(values1: list, values2: list) -> list:
    merged = []
    for i,j in zip(values1,values1[1:]):
        if i == j:
            values1.pop(values1.index(j))
    for x,z in zip(values2,values2[1:]):
        if x == z:
            values2.pop(values2.index(z))
    for l,k in zip(values1,values2):
        if l != k:
            merged.append(l)
            merged.append(k)
    return merged


if __name__ == '__main__':
    run([1, 2, 3, 4], [1, 1, 2, 3, 4, 5])
