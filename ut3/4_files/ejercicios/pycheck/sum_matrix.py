# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    result_path = 'data/sum_matrix/result.dat'
    with open(matrix1_path) as matrix1:
        matrixA = []
        data = matrix1.readlines()
        for dat in data:
            nums = dat.strip().split()
            coords = [int(num) for num in nums]
            matrixA.append(coords)

    with open(matrix2_path) as matrix2:
        matrixB = []
        data = matrix2.readlines()
        for dat in data:
            nums = dat.strip().split()
            coords = [int(num) for num in nums]
            matrixB.append(coords)
    
    with open(result_path, "w") as output_file:
        for row1, row2 in zip(matrixA, matrixB):
            row = []
            for num1, num2 in zip(row1, row2):
                addition = num1 + num2
                row.append(str(addition))
            result_row = " ".join(row)
            output_file.write(f"{result_row}\n")
            
    return filecmp.cmp(result_path, 'data/sum_matrix/.expected', shallow=False)


if __name__ == '__main__':
    run('data/sum_matrix/matrix1.dat', 'data/sum_matrix/matrix2.dat')