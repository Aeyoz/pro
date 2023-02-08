# *************
# SUMANDO FILAS
# *************
from pathlib import Path


def run(data_path: Path) -> tuple:
    addition = []
    with open(data_path) as f:
        for row in f:
            data = [int(element) for element in row.strip().split()]
            addition.append(sum(data))
    rsum = tuple(addition)

    return rsum


if __name__ == '__main__':
    run('data/sum_rows/data1.txt')