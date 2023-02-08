# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path

INVALID_CHARS = ".,:;()'¡!-"

def run(data_path: Path, target_word: str) -> list:
    matches = []
    tword = target_word.lower()
    with open(data_path) as f:
        document = f.readlines()
        for row, line in enumerate(document, start = 1):
            phrase = line.strip().lower().split()
            column = 1
            for word in phrase:
                if word.strip(INVALID_CHARS).lower() == tword:
                    a = len(word) 
                    b = len(word.lstrip(INVALID_CHARS)) 
                    dif = a - b
                    matches.append((row, column + dif))
                column += len(word) + 1
    return matches


if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'persona')