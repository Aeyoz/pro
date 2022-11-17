nested_values = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
flatted_values = []
for element in nested_values:
    if type(element) == list:
        for sub_element in element:
            flatted_values.append(sub_element)
    else:
        flatted_values.append(element)
print(flatted_values)   