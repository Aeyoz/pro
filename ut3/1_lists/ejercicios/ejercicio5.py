nums = [1, 1, 1, 1, 1, 1, 1]

for i, j in zip(nums, nums[1:]):
    if i != j:
        print("No son iguales")
        break
else:
    print("Iguales")