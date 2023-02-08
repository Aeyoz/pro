nested_values = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
flattened_values = []
for element in nested_values:
    #if type(element) == list:
    if isinstance(element, list):
        flattened_values.extend(element)
        #for sub_element in element:
            #flattened_values.append(sub_element)
    else:
        flattened_values.append(element)
print(flattened_values)   