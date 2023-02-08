# ******************
# AGRUPANDO PALABRAS
# ******************


def run(words: list) -> dict:
    group_words = {}
    for word in words:
        if word[0] not in group_words.keys():
            group_words[word[0]] = [word]
        else:
            group_words[word[0]].append(word)
    return group_words


if __name__ == '__main__':
    run(['mesa', 'móvil', 'barco', 'coche', 'avión', 'bandeja', 'casa', 'monitor', 'carretera', 'arco'])
