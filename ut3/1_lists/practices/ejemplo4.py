v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]
sums = 0

# Con zip y sin embellecer la frase.

for i, j in zip(v1,v2):
    sums += i * j
print(sums)

# Sin Zip en listas y la frase embellecida

#result = "v1 x v2 = "

# for i in v1:
#     if i == v1[-1]:
#         sums += i * v2[v1.index(i)]
#         result += f"{i} + {v2[v1.index(i)]} = {sums}"
#     else:
#         sums += i * v2[v1.index(i)]
#         result += f"{i} + {v2[v1.index(i)]} + "
# print(result)

# Embelleciendo la frase

# for i, j in zip(v1,v2):
#     if i != v1[-1]:
#         result += f"{i} * {j} + "
#         sums += i * j
#     else:
#         sums += i * j
#         result += f"{i} * {j} = {sums}"
# print(result)