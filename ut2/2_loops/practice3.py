VOWELS = "aeiou"
word = "Supercalifragilisticoespialidoso"
vowels_count = 0

for char in word:
    if char in VOWELS:
        vowels_count += 1
print(vowels_count)