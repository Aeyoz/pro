import re

text = """
    Bello es mejor que feo.
    Explícito es mejor que implícito.
    Simple es mejor que complejo.
    Complejo es mejor que complicado.
    Plano es mejor que anidado.
    Espaciado es mejor que denso.
    La legibilidad es importante.
    Los casos especiales no son lo suficientemente especiales como para romper las reglas.
    Sin embargo la practicidad le gana a la pureza.
    Los errores nunca deberían pasar silenciosamente.
    A menos que se silencien explícitamente.
    Frente a la ambigüedad, evitar la tentación de adivinar.
    Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
    A pesar de que esa manera no sea obvia a menos que seas Holandés.
    Ahora es mejor que nunca.
    A pesar de que nunca es muchas veces mejor que ahora mismo.
    Si la implementación es difícil de explicar, es una mala idea.
    Si la implementación es fácil de explicar, puede que sea una buena idea.
    Los espacios de nombres son una gran idea, ¡tengamos más de esos!
    """


er = r"\b[aeiou]\w+"  # |\b[aeiou]\w?"


def get_vowel_started_words(text):
    words = re.findall(er, text, re.I)
    return words


print(get_vowel_started_words(text))
