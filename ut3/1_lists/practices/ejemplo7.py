matrix_A = [[6, 4],[8, 9]]
matrix_B = [[3, 2],[1, 7]]
matrix_C = [[],[]]

matrix_C[0].append(matrix_A[0][0] * matrix_B[0][0] + matrix_A[0][1] * matrix_B[1][0])
matrix_C[0].append(matrix_A[0][0] * matrix_B[0][1] + matrix_A[0][1] * matrix_B[1][1])
matrix_C[1].append(matrix_A[1][0] * matrix_B[0][0] + matrix_A[1][1] * matrix_B[1][0])
matrix_C[1].append(matrix_A[1][0] * matrix_B[0][1] + matrix_A[1][1] * matrix_B[1][1])

print(matrix_C)