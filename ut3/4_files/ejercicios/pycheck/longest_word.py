# ********************
# LA PALABRA MÁS LARGA
# ********************
from pathlib import Path


def run(input_path: Path) -> str:
    longest_word = ""
    banned_chars = ",;.:´¨`^[]{}*'¿¡!@$~%&¬/()=<>-+"
    with open(input_path) as text:
        for line in text:
            for word in line.strip().split():
                longer = len(word.strip(banned_chars)) >= len(longest_word.strip())
                if longer:
                    longest_word = word.strip(banned_chars)

    return longest_word


if __name__ == '__main__':
    run('data/longest_word/python.txt')