str1 = "abc"
str2 = "123"
new_str = ""

for char in str1:
    for num in str2:
        new_str += f"{char + num} "
print(new_str)