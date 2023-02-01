# ***********************
# REEMPLAZO DE CARACTERES
# ***********************
import filecmp
from pathlib import Path


def run(input_path: Path, replacements: str) -> bool:
    output_path = 'data/replace_chars/r_noticia.txt'
    tilda, non_tilda = [], []

    for vowel1, vowel2 in replacements.split("|"):
        tilda.append(vowel1)
        non_tilda.append(vowel2)

    with open(input_path) as f:
        document = "".join(f.readlines())
    
    with open(output_path, 'w') as f:
        for vowel1, vowel2 in zip(tilda, non_tilda):
            document = document.replace(vowel1, vowel2)
        f.write(document)
        
    return filecmp.cmp(output_path, 'data/replace_chars/.expected', shallow=False)


if __name__ == '__main__':
    run('data/replace_chars/noticia.txt', 'áa|ée|íi|óo|úu')