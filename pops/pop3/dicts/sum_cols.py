# ****************
# SUMANDO COLUMNAS
# ****************
from pathlib import Path


def run(data_path: Path) -> tuple:
    sums = {}
    with open(data_path) as f:
        for row in f:
            row = row.strip().split()
            for col in range(0, len(row)):
                sums[col] = sums.get(col, 0) + int(row[col])
    csum = tuple(sums.values())

    return csum


if __name__ == '__main__':
    run('data/sum_cols/data1.txt')