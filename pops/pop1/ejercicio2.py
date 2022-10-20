# ut1-pop1-ej2
number = 99
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓

binary_number = bin(number)

count_ones = binary_number.count("1")

# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert count_ones == 4