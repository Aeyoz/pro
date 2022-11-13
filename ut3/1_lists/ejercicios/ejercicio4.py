unchecked_dup_nums = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
checked_dup_nums = []

for num, i in zip(unchecked_dup_nums,unchecked_dup_nums[1:]):
    if num != i:
        checked_dup_nums.append(i)
    elif num == 0:
        checked_dup_nums.append(num)
print(checked_dup_nums)