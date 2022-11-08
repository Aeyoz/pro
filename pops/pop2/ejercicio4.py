import sys

import pycheck

CHECK_CASES = [
    [[67, 23], (88, 44)],
    [[50, 20], (60, 30)],
    [[28, 4], (48, 24)],
]


def run(mother_age: int, daughter_age: int) -> tuple:
    target_mother_age, target_daughter_age = mother_age, daughter_age
    while (target_mother_age / target_daughter_age) != 2:
        target_mother_age += 1
        target_daughter_age += 1
    return target_mother_age, target_daughter_age


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)