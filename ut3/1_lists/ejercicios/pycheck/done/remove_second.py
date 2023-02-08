'''
Dada una lista, genere otra lista eliminando el segundo elemento de forma repetida.
'''

def run(items: list) -> list:
    filter = []
    for i in range(len(items)):
        if i % 2 == 0:
            filter.append(items[i])
    # filter = items[::2]
    # filter = [item for index, item in enumerate(items, 1) if index % 2 != 0]
    # for index,item in enumerate(items, 1):
    #     if index % 2 != 0:
    #         filter.append(item)
    return filter
