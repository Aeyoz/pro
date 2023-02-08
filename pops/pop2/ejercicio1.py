import sys

import pycheck

CHECK_CASES = [
    [[67], 2],
    [[99], 6],
    [[1024], 11],
]


def run(number: int) -> int:
    num_divisors = 0
    for div in range(1, number + 1):
        if number % div == 0:
            num_divisors += 1
    return num_divisors


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)