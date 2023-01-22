unsorted_items = {'C1': 'Red', 'C2': 'Black', 'C3': 'Red', 'C4': 'Green'}
sorted_items = []
unsorted_items_2 = {}
same_key_items = []
for key, value in unsorted_items.items():
    if value not in unsorted_items_2:
        unsorted_items_2[value] = key
    else:
        same_key_items.append(tuple((key,value)))
sorted_values = sorted(list(unsorted_items_2.items()))
values = {tupple[1]:tupple[0] for tupple in sorted_values}
values[same_key_items[0]] = same_key_items[1]
sorted_items = list(values.items())
print(sorted_items)