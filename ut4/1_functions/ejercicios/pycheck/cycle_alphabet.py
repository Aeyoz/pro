# *****************
# ALFABETO CIRCULAR
# *****************

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
def text_gen(text: str, limit: int = 0):
    for i in range(limit):
        current_pos = i % len(text)
        yield ALPHABET[current_pos]

def run(max_letters: int) -> str:
    text = "".join(text_gen(ALPHABET, max_letters))
    return text 


if __name__ == '__main__':
    run(0)