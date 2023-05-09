while isinstance(num := input("Give me an integer number: "), str):
    try:
        num = int(num)
    except ValueError:
        print("Try again")
    else:
        print(num)
        break
