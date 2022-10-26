size = 5
grid = ""

for row in range(size):
    for column in range(size):
        if row < column:
            grid += "D "
        elif row > column:
            grid += "U "
        else:
            grid += "X "

