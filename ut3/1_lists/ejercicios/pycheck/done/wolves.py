'''
Usted es granjera y debe cuidar sus ovejas, pero existe un lobo merodeando por la zona y
hay peligro de que coma alguna oveja.

La lista de entrada contiene ovejas y un lobo. Casos:
a) Si el lobo está cerca de una oveja, habrá que responder con el mensaje:
"Cuidado oveja X, el lobo te va a comer".
b) Si el lobo está al final de la lista, habrá que responder con el mensaje:
"No te quiero ver más por aquí, lobo"

Las posiciones hay que calcularlas empezando por el final de la lista con índice 1.
'''


def run(farm: list) -> str:
    wolf = farm.index("lobo")
    animals = 0
    msg = ""
    for animal1,animal2 in zip(farm, farm[1:]):
        if wolf == len(farm) - 1:
            msg = "No te quiero ver más por aquí, lobo"
        elif animal1 or animal2 != "oveja":
            warn = farm.index("lobo")
            animals = farm[warn:].count("oveja")
            msg = f"Cuidado oveja {animals}, el lobo te va a comer"
    return msg

if __name__ == '__main__':
    run(['oveja', 'oveja', 'lobo', 'oveja'])
