x1 = int(input("Introduzca la coordenada X1: "))
y1 = int(input("Introduzca la coordenada Y1: "))
x2 = int(input("Introduzca la coordenada X2: "))
y2 = int(input("Introduzca la coordenada Y2: "))

subs_xs = (x2 - x1) ** 2 
subs_ys = (y2 - y1) ** 2

dist = (subs_xs + subs_ys) ** 0.5
print(dist)