n = int(input("Introduce a number: "))

numbers = 5

while numbers < n:
    if n % numbers == 0:
        print(f"{numbers} is divisor of {n}")
        numbers += 5
    elif numbers == 0:
        print("You can't divide by zero")
        numbers += 5
    else:
        print(f"{numbers} is not divisor of {n}")
        numbers += 5