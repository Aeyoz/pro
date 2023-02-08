values = [1, 1, 1, 1, 1, 1, 1]

for i, j in zip(values, values[1:]):
    if i != j:
        print("No son iguales")
        break
else:
    print("Iguales")