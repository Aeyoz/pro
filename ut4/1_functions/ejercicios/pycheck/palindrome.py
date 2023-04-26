# **********
# PALÍNDROMO
# **********


def is_palindrome(phrase) -> bool:
    phrase = phrase.lower().replace(" ", "")
    return phrase == phrase[::-1]