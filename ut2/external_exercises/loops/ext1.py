num = 8
sumatorio = 0
cadena = ""
for i in range(num + 1):
    if i != num:
        sumatorio += i
        cadena += f"{i} + "
    elif i == num:
        sumatorio += i
        cadena += f"{i} = {sumatorio}"
print(cadena)