unsorted_items = {'C1': 'Red', 'C2': 'Black', 'C3': 'Red', 'C4': 'Green'}
values_then_keys = [(f"{v}:{k}") for k,v in unsorted_items.items()]
values_then_keys.sort()
sorted_values = [(item[0], item[1]) for item in values_then_keys.split(":")]
print(sorted_values)