'''
Dada una lista de valores numéricos, calcule la suma de todos sus elementos sin tener en
cuenta el valor máximo y el valor mínimo.

NOTAS:
- Pueden haber varios valores máximos o varios valores mínimos (repeticiones).
- Puede venir la lista vacía como entrada.
'''


def run(values: list) -> int:   
    values = sorted(values)
    tsum = 0
    if len(values) > 1:
        min_value = values.pop(-1)
        max_value = values.pop(0)
        for i in values:
            if i == min_value or i == max_value:
                values.pop(values.index(i))
        tsum = sum(values)        
    elif len(values) > 0:
        values.pop(0)
    else:
        tsum = 0
    return tsum


if __name__ == '__main__':
    run([6, 2, 1, 8, 10])
