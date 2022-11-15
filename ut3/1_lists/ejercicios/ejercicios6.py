matrix = [[4, 6, 1], [2, 9, 3], [1, 7, 7]]
diagonal = 0
result = 0
for i in matrix:
    result += matrix[diagonal][diagonal]
    diagonal += 1
print(result)