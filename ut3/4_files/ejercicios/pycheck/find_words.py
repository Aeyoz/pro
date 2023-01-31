# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    matches = []
    with open(data_path) as file:
        row = 0
        for line in file:
            row += 1
            if line.count(target_word.lower()) >= 1 < 2:
                column = len(line[:line.index(target_word):]) + 1
                matches.append((row, column))
            elif line.count(target_word) >= 2:
                for word in line:
                    if word == target_word.strip().lower():
                        column = len(line[:line.index(target_word):]) + 1
                        matches.append((row, column))
    return matches


if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'persona')