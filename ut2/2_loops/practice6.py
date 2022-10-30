size = 5

for row in range(size):
    for column in range(size):
        if row < column:
            symbol = "U"
        elif row > column:
            symbol = "D"
        else:
            symbol = "X"
        print(symbol, end=" ")
    print()