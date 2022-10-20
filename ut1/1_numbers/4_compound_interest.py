cap_ini = 10000
int_per = 3.5 * 0.01
years = 7

option = input('''Introduzca el tipo de interés que desea calcular: 
                1. Interés simple 
                2. Interés compuesto
                Su elección: ''')
if option == "1":
    capt_fin = cap_ini * int_per * years
elif option == "2":
    capt_fin = cap_ini * ((1 + int_per) ** years)
else:
    print("Opción no válida")

print(f"Su capital final es: {capt_fin}")