tries = 0
num = 13

while guess:= (int(input("Introduce a number between 0 and 100: "))) != num:
    tries += 1
    if guess > num: 
        print("Menor")
    elif guess < num:
        print("Mayor")

tries += 1
print(f"Wow, it only took you {tries} tries to guess")