'''
Dado un nombre y apellidos en formato "apellidos, nombre", obtenga las iniciales de dicha
persona pasadas a mayúsculas y con punto al final.
'''


def run(fullname: str) -> str:
    fullname = fullname.upper().split(", ")
    name = fullname[1][0]
    surname = fullname[0]
    surname = surname.split()
    s_surname = ""
    if len(surname) >= 2:
        f_surname = surname[0][0]
        s_surname = surname[1][0]
    else:
        f_surname = surname[0][0]
    fullname = [name, f_surname, s_surname]
    initials = f'{".".join(fullname)}'.rstrip(".") + "."
    return initials


if __name__ == '__main__':
    run('Delgado Quintero, sergio')
