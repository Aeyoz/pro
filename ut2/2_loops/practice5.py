n = int(input("Prime number: "))
divs = 0


for div in range(1,n + 1):
    if (n % div) == 0:
        divs += 1

if divs == 2:
    print("The number is prime")
else:
    print("The number isn't prime")