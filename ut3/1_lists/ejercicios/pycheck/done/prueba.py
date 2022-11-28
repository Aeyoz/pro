#values = [6, 2, 1, 8, 10]
values = [1, 1, 11, 2, 3]
#values = [1]
#values = [1,1]
#values = [1,2]
#values = []

values = list(sorted(values))
minimun = values[0]
maximun = values[-1]
for i, j in zip(values,values[1:]):
    if i or j == minimun or maximun:
        values.pop(values.index(i))
        values.pop(values.index(j))

print(sum(values)) 