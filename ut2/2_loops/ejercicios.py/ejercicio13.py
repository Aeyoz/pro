tries = 0
num = 13

while True:
    guess = int(input("Introduce a number between 0 and 100: "))
    tries += 1
    if guess > num: 
        print("The number introduced was too big")
    elif guess < num:
        print("The number introduced was too low")
    else:
        print(f"Wow, it only took you {tries} tries to guess")
        break