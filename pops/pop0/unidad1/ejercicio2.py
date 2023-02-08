# ut1-pop0-ej2
adn = 'GGTTACCAACCCAGTCGAAGGTCATGAAGGGGCGTATTTGGATGGAGCTG'
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓

adn_length = len(adn)

adenines_rate = (adn.count("A") * 100) / adn_length
thymines_rate = (adn.count("T") * 100) / adn_length
guanines_rate = (adn.count("G") * 100) / adn_length
cytosines_rate = (adn.count("C") * 100) / adn_length

# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert adenines_rate == 24.0
assert thymines_rate == 22.0
assert guanines_rate == 36.0
assert cytosines_rate == 18.0