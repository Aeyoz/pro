import sys

import pycheck

CHECK_CASES = [
    [['AGTCCCAGGT'], 'AGUCCCAGGU'],
    [['GCGCACTCTTCTTTGCTCTT'], 'GCGCACUCUUCUUUGCUCUU'],
    [['CCGGAGATTGGCTACTGAAGATCCA'], 'CCGGAGAUUGGCUACUGAAGAUCCA'],
]


def run(adn: str) -> str:
    arn = ""
    for molecule in adn:
        if molecule == "T":
            arn += "U"
        else:
            arn += molecule
    return arn


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)