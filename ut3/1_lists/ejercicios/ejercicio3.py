unleveled_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
leveled_list = []
for element in unleveled_list:
    if type(element) == list:
        for sub_element in element:
            leveled_list.append(sub_element)
    else:
        leveled_list.append(element)
print(leveled_list)   