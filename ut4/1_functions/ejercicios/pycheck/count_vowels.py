# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************

VOWELS = "aeiou"
def count_vowels(text, counter=0):
    text = text
    if len(text) == 0:
        return counter
    counter += 1 if text[0] in VOWELS else 0
    return count_vowels(text[1:], counter+0)
