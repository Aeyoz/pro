# *****************
# HAN CANTADO LÍNEA
# *****************
from pathlib import Path


def run(input_path: Path, line_no: int) -> str:
    with open(input_path) as text:
        line = None
        for n_line, phrase in enumerate(text, 1):
            if int(n_line) == line_no:
                line = phrase.strip()            
    return line


if __name__ == '__main__':
    run('data/get_line/nasdaq.txt', 20)