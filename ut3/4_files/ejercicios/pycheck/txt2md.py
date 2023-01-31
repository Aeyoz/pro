# *******************
# DE TEXTO A MARKDOWN
# *******************
import filecmp
from pathlib import Path


def run(text_path: Path) -> bool:
    md_path = 'data/txt2md/outline.md'
    output_lines = []
    with open(text_path) as input_file:
        for line in input_file:
            tabs = line.count("\t") + 1
            output_lines.append(f"{'#' * tabs} {line.strip()}\n")
    
    with open(md_path, "w") as output_file:
        for line in output_lines:
            output_file.write(line)

    return filecmp.cmp(md_path, 'data/txt2md/.expected', shallow=False)


if __name__ == '__main__':
    run('data/txt2md/outline.txt')