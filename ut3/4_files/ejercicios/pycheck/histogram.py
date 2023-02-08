# **********
# HISTOGRAMA
# **********
import filecmp
from pathlib import Path


def run(data_path: Path) -> bool:
    histogram_path = 'data/histogram/histogram.txt'
    bar_incrementer = "█"
    
    with open(data_path) as f:
        document = "".join(f.readlines())
        letters = sorted("".join(set(document)))
        print(letters)
        freq = {}
        for letter in letters:
            freq[letter] = document.count(letter)

    with open(histogram_path, "w") as f:
        for letter in freq:
            f.write(f"{letter} {freq[letter] * bar_incrementer} {freq[letter]}\n")
        
    return filecmp.cmp(histogram_path, 'data/histogram/.expected', shallow=False)


if __name__ == '__main__':
    run('data/histogram/data.txt')