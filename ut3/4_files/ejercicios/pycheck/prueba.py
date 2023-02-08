tilda = "áéíóú"
non_tilda = "aeiou"

text = "Hasta 17 millones de españoles reconocen ser usuarios habituales de patinetes eléctricos \
        o bicicletas eléctricas, y un 60% de la población ve su uso probable a corto plazo. Estos\
        datos, recogidos en un estudio elaborado por la Fundación Línea Directa en colaboración con\
        la Fundación Española para la Seguridad Vial (FESVIAL), son la confirmación de lo que se ve \
        a diario en las calles de nuestras ciudades: cada vez más personas eligen los conocidos como \
        VMPs (vehículos de movilidad personal) para sus desplazamientos urbanos, motivados sobre todo \
        por el alza de los precios del combustible, el aumento del precio de los coches y los elevados \
        costes de su posterior mantenimiento."

for vowel1, vowel2 in zip(tilda, non_tilda):
        text = text.replace(vowel1, vowel2)

print(text)