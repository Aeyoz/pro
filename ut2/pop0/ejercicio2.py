import sys

import pycheck


def run(word: str) -> float:
    additions = 0
    for i in word:
        lenght = len(word)
        additions += ord(i)
    char_avg = additions / lenght
    return char_avg


if __name__ == '__main__':
    pycheck.check('pro.ut2.pop0.ej2', sys.argv, run)