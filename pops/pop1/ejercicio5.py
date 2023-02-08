# ut1-pop1-ej5
text = "El Sistema Operativo que funcionará Libre y Gratuito"
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓

no_accents_text = text.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

slug = no_accents_text.replace(" ", "-").lower()

# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert slug == "el-sistema-operativo-que-funcionara-libre-y-gratuito"
