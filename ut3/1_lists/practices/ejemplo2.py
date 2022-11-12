word = "background"
letters = []

for char in word:
    if char in letters:
        print("Not a isogram")
        break
    if char.isalpha():
        letters.append(char)
else:
    print("Is a isogram")