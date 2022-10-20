# ut1-pop1-ej4
hexcolor = "A131F7"
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓

red_code = hexcolor[:2]
green_code = hexcolor[2:4]
blue_code = hexcolor[4:6]

red = int(red_code, 16)
green = int(green_code, 16)
blue = int(blue_code, 16)

rgb_color = f"({str(red)},{str(green)},{str(blue)})"

# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert rgb_color == "(161,49,247)"
