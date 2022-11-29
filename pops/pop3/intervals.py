# ********************
# INTERVALO DESPLEGADO
# ********************


def run(interval: str) -> list:
    interval = interval.split(",")
    lower = int(interval[0][1])
    upper = int(interval[1][:-1])
    if interval[0][0] == "(":
        lower += 1
    if interval[1][-1] == ")":
        upper -= 1
    irange = list(range(lower, upper + 1))
    return irange


if __name__ == '__main__':
    run('[3,10]')
