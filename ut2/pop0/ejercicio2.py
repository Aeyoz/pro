import sys

import pycheck


def run(word: str) -> float:
    additions = 0
    counter = 0
    for i in word:
        additions += ord(i)
        counter += 1
    char_avg = additions / counter
    return char_avg


if __name__ == '__main__':
    pycheck.check('pro.ut2.pop0.ej2', sys.argv, run)