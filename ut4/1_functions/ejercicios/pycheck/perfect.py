# *****************
# NÚMEROS PERFECTOS
# *****************


def is_perfect(num):
    def get_divs(num):
        divs = []
        for div in range(1, num//2 + 1):
            if num % div == 0:
                divs.append(div)
        return divs
    return num == sum(get_divs(num))