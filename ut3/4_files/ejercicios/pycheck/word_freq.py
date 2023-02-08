# **********************
# FRECUENCIA DE PALABRAS
# **********************
from pathlib import Path


def run(input_path: Path, lower_bound: int) -> dict:
    banned_chars = ",;.:´¨`^[]{}*'¿@¡!$~%&¬/()=<>-+\n\t"
    freq = {}
    with open(input_path) as f:
        document = "".join(f.readlines()).lower()
        text = document.strip(banned_chars).split()
        for word in text:
            frequency = text.count(word)
            if frequency >= lower_bound:
                freq[word] = frequency
    return freq


if __name__ == '__main__':
    run('data/word_freq/cistercian.txt', 9)