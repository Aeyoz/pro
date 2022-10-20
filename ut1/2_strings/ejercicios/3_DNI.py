dni = int(input("Introduzca su DNI:"))
letters = "TRWAGMYFPDXBNUZSQVHLCKE"
calc = dni % 23 
complete_dni = str(dni) + letters[calc]
print(complete_dni)