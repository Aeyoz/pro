# while isinstance(num := input("Give me an integer number: "), str):
#    try:
#        num = int(num)
#    except ValueError:
#        print("Try again")
#    else:
#        print(num)
#        break


def get_num():
    try:
        num = int(input("Give a number: "))
    except ValueError:
        print("Try again")
        return get_num()
    else:
        return num


a = get_num()
print(a)
