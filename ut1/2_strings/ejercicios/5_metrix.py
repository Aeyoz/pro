word = input("Introduce your word: ")
w_length = len(word)
vowel_count = 0

vowel_count += word.count("a")
vowel_count += word.count("e")
vowel_count += word.count("i")
vowel_count += word.count("o")
vowel_count += word.count("u")

metric = vowel_count * w_length
print(metric)