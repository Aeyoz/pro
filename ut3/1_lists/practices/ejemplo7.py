matrix_A = [[6, 4],[8, 9]]
matrix_B = [[3, 2],[1, 7]]
matrix_C = []

# for rows in matrix_A[0]:
#     for j in rows[0][0]:
#         result = matrix_A[rows][j]
#         print(matrix_A[rows][j])

for _A in matrix_A:
    pos1 = 0
    pos2 = 0
    for i in range(len(_A)):
        print(_A[i])
for _B in matrix_B:

# for _A, _B in zip(matrix_A, matrix_B):
#     pos1 = 0
#     pos2 = 0
#     for value_A in _A:
#         for value_B in _B:
#             pos1 += value_A * value_B
#             break
#     for value_B in _B:
#         for value_A in _A:
#             ""
#         mult = pos1 + pos2
#         matrix_C.append(mult)
# print(matrix_C)



# for _A, _B in zip(matrix_A, matrix_B):
#     for value_A, value_B in zip(_A, _B):
#         mult = value_A * value_B
#         matrix_C.append(mult)
# print(matrix_C)