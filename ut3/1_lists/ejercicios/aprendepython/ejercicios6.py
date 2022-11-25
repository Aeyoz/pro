matrix = [[4, 6, 1], [2, 9, 3], [1, 7, 7]]
result = 0
for element in range(len(matrix)):
    result += matrix[element][element]
print(result)