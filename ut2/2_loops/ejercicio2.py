name = ""
while not (name := input("Introduce your name: ")).istitle():
    print("Your name is in the wrong format")
print("Your name is in the correct format")
# 
# while True:
#     name = input("Introduce your name: ")
#     if name.istitle():
#         print("Your name is in the correct format")
#         break
#     else:
#         print("Your name is not in the correct format")