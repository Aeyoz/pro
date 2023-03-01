# ********
# PANGRAMA
# ********


def is_pangram(word):
    letters = []
    pangram_text = True
    for letter in word:
        if letter not in letters:
            letters.append(letter)
        else:
            pangram_text = False
            break
    return pangram_text
