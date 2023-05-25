import re

text = """Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
Lorem Ipsum ha sido el texto de relleno estándar https://es.wikipedia.org/wiki/Wikipedia:Portada de las industrias desde el año 1500,
cuando un impresor (N. del https://aprendepython.es/ T. persona que se dedica a la imprenta) desconocido usó una galería de textos
y los mezcló de tal manera que logró https://pythex.org/ hacer un libro de textos especimen. No sólo sobrevivió 500 años,
sino que tambien ingresó como texto de relleno en documentos electrónicos, http://www.cticanarias.com quedando esencialmente igual al original.
Fue popularizado en los https://mail.google.com/ 60s con la creación de las hojas Letraset, las cuales contenian pasajes de Lorem Ipsum,
y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum."""

er = r"\bhttps?://\S*\.\S*"


def get_urls(text):
    words = re.findall(er, text, re.I)
    return words


print(get_urls(text))
