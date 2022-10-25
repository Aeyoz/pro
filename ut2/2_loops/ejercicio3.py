number = "1"
times = 9

for rep in range(1, times + 1):
    operation = number * rep
    print(f"{operation} * {operation} = {int(operation) * int(operation)}")