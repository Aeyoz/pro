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
        lim = min(len(text), max_letters)
        for _, letter in zip(range(lim), a_gen):
            text.append(letter)
        
    return "".join(text)


if __name__ == '__main__':
    run(0)