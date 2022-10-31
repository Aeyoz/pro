from tkinter import N


n = 12
m = 150
max_num = max(12, 44) // 2
mcd = 0

for num in range(1, max_num + 1):
    if n % num == 0 and m % num == 0:
        mcd = num

print(mcd)