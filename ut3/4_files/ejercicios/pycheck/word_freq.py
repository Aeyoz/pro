# **********************
# FRECUENCIA DE PALABRAS
# **********************
from pathlib import Path


def run(input_path: Path, lower_bound: int) -> dict:
    banned_chars = ",;.:´¨`^[]{}*'¿¡!@$~%&¬/()=<>-+\n\t"
    freq = {}
    with open(input_path) as document:
        words = []
        for word in document:
            ""
    return freq


if __name__ == '__main__':
    run('data/word_freq/cistercian.txt', 9)