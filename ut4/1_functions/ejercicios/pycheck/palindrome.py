# **********
# PALÍNDROMO
# **********


def is_palindrome(phrase):
    phrase = phrase.lower().replace(" ", "")
    return phrase == phrase[::-1]