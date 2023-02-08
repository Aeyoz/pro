elements = ["Keep", "Remove", "Keep", "Remove", "Keep"]

for i in elements:
    if elements.index(i) % 2:
        elements.pop()
