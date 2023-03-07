# *****************
# ALFABETO CIRCULAR
# *****************

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
def run(max_letters: int) -> str:
    text, counter = [], 0
    while len(text) < max_letters:
        text.append(ALPHABET[counter])
        counter += 1
        if counter == len(ALPHABET):
            counter = 0

    return "".join(text)


if __name__ == '__main__':
    run(0)