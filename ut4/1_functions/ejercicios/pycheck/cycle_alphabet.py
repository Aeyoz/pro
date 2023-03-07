# *****************
# ALFABETO CIRCULAR
# *****************

def text_gen(text):
    for letter in text:
        yield letter

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def run(max_letters: int) -> str:
    text = []
    while len(text) < max_letters:
        a_gen = text_gen(ALPHABET)
        for letter in a_gen:
            text.append(letter)
            if len(text) == max_letters:
                break
    return "".join(text)


if __name__ == '__main__':
    run(0)