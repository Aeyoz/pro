full_name = input("Introduce your name: ")
sliced = full_name.split()
check = 0

for i in sliced:
    if i.istitle():
        check += 1
        if check == 3:
            print(f"Your name is: {full_name}")
    else:
        print("Your name must be in title format")