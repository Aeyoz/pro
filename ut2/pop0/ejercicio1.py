import sys

import pycheck


def run(text: str) -> str:
    VOWELS = "aeiouáéíóúäëïöüàèìòù"
    output = ""
    for i in text:
        if i.lower() in VOWELS:
            continue
        else:
            output += i
    return output


if __name__ == '__main__':
    pycheck.check('pro.ut2.pop0.ej1', sys.argv, run)