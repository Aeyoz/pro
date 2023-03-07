# ********
# PANGRAMA
# ********

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
def is_pangram(word):
    set_word = len(set(word))
    pangram_text = set_word >= len(ALPHABET)

    return pangram_text
