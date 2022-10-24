VOWELS = "aeiou"
word = "Supercalifragilisticoespialidoso"
vowels_count = 0

for i in word:
    if i in VOWELS:
        vowels_count += 1
print(vowels_count)