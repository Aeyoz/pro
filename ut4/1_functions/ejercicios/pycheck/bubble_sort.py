# **********************
# ORDENANDO CON BURBUJAS
# **********************


def bubble(items):
    sorted_items = items.copy()
    change = True
    while change:
        change = False
        for i in range(len(sorted_items) - 1):
            if sorted_items[i] > sorted_items[i + 1]:
                sorted_items[i + 1], sorted_items[i] = sorted_items[i], sorted_items[i + 1]
                change = True

# Version ineficiente de bubble sort, porque no sabes la cantidad de veces que 
# se recorre. Por lo que es más eficiente detectar si hay cambios o no, que es 
# lo que se hace en la linea 10 y 14

#    for _ in range(len(sorted_items)):
#        for i in range(len(sorted_items) - 1):
#            if sorted_items[i] > sorted_items[i + 1]:
#                sorted_items[i + 1], sorted_items[i] = sorted_items[i], sorted_items[i + 1]
    return sorted_items
