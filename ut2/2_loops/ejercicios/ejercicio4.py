expresion = "hello world"

for char in expresion:
    if char.isalpha() == False:
        print(f"The following character is not alphabetic: {char}")
        break
else:
    print(f"{expresion} is alphabetic")