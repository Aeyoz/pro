unsorted_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
sorted_list = []
for i in unsorted_list:
    if type(i) == list:
        for j in i:
            sorted_list.append(j)
    else:
        sorted_list.append(i)
print(sorted_list)   