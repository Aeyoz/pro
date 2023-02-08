unchecked_dup_nums = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
checked_dup_nums = []
prev = None
for num in unchecked_dup_nums:
    if num != prev:
        checked_dup_nums.append(num)
    prev = num
print(checked_dup_nums)
