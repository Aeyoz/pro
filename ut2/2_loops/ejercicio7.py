obj_x = 7
obj_y = 8

x = 0
y = 0
mov = True
positions = ""

while obj_x >= x and obj_y >= y:
    if mov:
        x += 1
        y += 2
        positions += f"[{x},{y}] "
        mov = False
    else:
        x += 2
        y += 1
        positions += f"[{x},{y}] "
        mov = True
print(positions)