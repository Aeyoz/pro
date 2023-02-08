# *******************
# CONSONANTES COMUNES
# *******************


def run(text1: str, text2: str) -> str:
    set1 = set(text1)
    set2 = set(text2)
    chars = "aeiou "
    symbols = {char for char in set1 & set2 if char not in chars}
    cconst = "".join(sorted(symbols))
    return cconst



if __name__ == '__main__':
    run('Flat is better than nested', 'Readability counts')