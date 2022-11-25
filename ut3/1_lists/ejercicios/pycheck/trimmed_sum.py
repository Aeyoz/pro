'''
Dada una lista de valores numéricos, calcule la suma de todos sus elementos sin tener en
cuenta el valor máximo y el valor mínimo.

NOTAS:
- Pueden haber varios valores máximos o varios valores mínimos (repeticiones).
- Puede venir la lista vacía como entrada.
'''


def run(values: list) -> int:
    min_value = min(values)
    max_value = max(values)
    for i in values:
        if i == min_value:
            values.pop(values.index(i))
        elif i == max_value:
            values.pop(values.index(i))
    tsum = sum(values)
    return tsum


if __name__ == '__main__':
    run([6, 2, 1, 8, 10])
