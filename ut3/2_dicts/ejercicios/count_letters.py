# ***************
# CONTANDO LETRAS
# ***************


def run(sentence: str) -> dict:
    counter = {}
    for char in sentence:
        if char not in counter.keys():
            counter[char] = 1
        else:
            counter[char] += 1
    return counter


if __name__ == '__main__':
    run('boom')
