# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path

def run(input_path: Path) -> tuple:
    num_lines = num_words = num_bytes = 0
    with open(input_path) as lines:
        for line in lines:
            num_bytes += len(line.encode('utf-8'))
            num_words += len(line.split())
            num_lines += 1
    return num_lines, num_words, num_bytes


if __name__ == '__main__':
    run('data/wc/lorem.txt')