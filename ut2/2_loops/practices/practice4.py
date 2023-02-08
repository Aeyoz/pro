number = int(input("Introduce un numero: "))
pos_divs = 2

for div in range(1,number):
    if number % div == 0:
        pos_divs += 1

if pos_divs > 2:
    print(f"El numero {number} no es primo")
elif pos_divs == 2:
    print(f"El numero {number} no es primo")