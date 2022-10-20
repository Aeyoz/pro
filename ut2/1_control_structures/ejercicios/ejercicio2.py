num1 = int(input("Give me a number: "))
num2 = int(input("Give me a number: "))
num3 = int(input("Give me a number: "))

if num1 < num2 and num1 < num3:
    min_value = num1
elif num2 < num3 and num2 < num1:
    min_value = num2
elif num3 < num1 and num3 < num2:
    min_value = num3
else:
    print("Error")
    

print(min_value)