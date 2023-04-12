# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************

VOWELS = "aeiou"
def count_vowels(text: str, counter: int = 0) -> int:
    if len(text) == 0:
        return counter
    counter += 1 if text[0] in VOWELS else 0
    return count_vowels(text[1:], counter+0)

def count_vowels(text: str) -> int:
    if len(text) == 1:
        if text[0] in VOWELS:
            return 1
        return 0
    return count_vowels(text[0]) + count_vowels(text[1:])
