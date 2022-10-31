obj_x = 7
obj_y = 8
x = 0
y = 0
flow = True


while obj_x >= x and obj_y >= y:
    print(f"({x}, {y})")
    x += 2 - flow
    y += 1 + flow
    flow = not flow