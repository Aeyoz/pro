year = input("Introduzca la el año: ")

if year.isnumeric():
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 ==0:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
else:
    print("Formato no valido")
