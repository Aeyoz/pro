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
    merged.extend(values1)
    merged.extend(values2)
    for i, j in zip(merged, merged[1:]):
        if i == j:
            merged.pop(merged.index(j))
        elif i == max(merged):
            merged.insert(10, i)
        elif j == max(merged) and j not in merged:
            merged.insert(10, j)
    for i,j in zip(merged, merged[1:]):
        if merged.count(i) > 1:
            merged.pop(merged.index(i))
        if merged.count(j) > 1:
            merged.pop(merged.index(j))
    return merged


if __name__ == '__main__':
    run([1, 2, 3, 4], [1, 1, 2, 3, 4, 5])
