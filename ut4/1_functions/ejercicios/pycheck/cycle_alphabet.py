# *****************
# ALFABETO CIRCULAR
# *****************

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
def text_gen(limit):
    alpha_len = len(ALPHABET)
    while limit > 0:
        election = min(alpha_len, limit)
        for i in range(election):
            yield ALPHABET[i]
        limit -= alpha_len

def run(max_letters: int) -> str:
    text = "".join([letter for letter in text_gen(max_letters)])
    return text 


if __name__ == '__main__':
    run(0)