n = 12
m = 44
min_num = n if n < m else m 

for num in range(min_num, 0, -1):
    if n % num == 0 and m % num == 0:
        break
print(num)