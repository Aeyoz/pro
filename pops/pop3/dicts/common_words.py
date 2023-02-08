# *************************
# BUSCANDO PALABRAS COMUNES
# *************************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = 'data/common_words/output.txt'
    coincidences = []
    with open(input_path) as f:
        document = "".join(f.readlines()).strip().lower().split("\n")
        for row1 in document:
            set1 = set(row1.split())
            for row2 in document:
                set2 = set(row2.split())
                coincidences.append(f"{len(set1.intersection(set2))}\n")

    with open(output_path, "w") as f:
        f.writelines(coincidences)

    return filecmp.cmp(output_path, 'data/common_words/.expected', shallow=False)


if __name__ == '__main__':
    run('data/common_words/minizen.txt')