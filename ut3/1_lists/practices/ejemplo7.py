matrix_A = [[6, 4],[8, 9]]
matrix_B = [[3, 2],[1, 7]]
matrix_C = []

for _A, _B in zip(matrix_A, matrix_B):
    for value_A, value_B in zip(_A, _B):
        mult = value_A * value_B
        matrix_C.append(mult)
print(matrix_C)