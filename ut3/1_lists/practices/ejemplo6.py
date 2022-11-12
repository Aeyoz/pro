from os import sys
values = sys.argv[1:]
values = [int(v) for v in values]
media = sum(values) / len(values)
print(media)


# for i in values:
#     values.insert(values.index(i), int(i))
#     values.pop(values.index(i))