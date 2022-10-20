numbers = int(input("Introduce your desired number: "))
n_numbers = str(numbers) + " " + str(numbers) * 2 + " " + str(numbers) * 3 
values = n_numbers.split()
calc = int(values[0]) + int(values[1]) + int(values[2])
print(calc)