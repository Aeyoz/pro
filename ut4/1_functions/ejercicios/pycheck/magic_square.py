# ***************
# CUADRADO MÁGICO
# ***************

def is_magic_square(values) -> bool:
    all_values = []
    rows, cols, diagonal, inverted_diagonal = {}, {}, 0, 0
    for row, matrix in enumerate(values, start=0):
        for col, element in enumerate(range(0, len(matrix)), start=0):
            rows[row] = rows.get(row, 0) + matrix[element]
            cols[col] = cols.get(col, 0) + matrix[element]
        diagonal += matrix[row]
        inverted_diagonal += matrix[len(values)-1-row]
    all_values.extend(list(rows.values()))
    all_values.extend(list(cols.values()))
    all_values.append(diagonal)
    all_values.append(inverted_diagonal)

    return all_values == sorted(all_values)