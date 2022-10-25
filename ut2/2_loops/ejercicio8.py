bin_num_1 = "0001010011101"
bin_num_2 = "0000110010001"
# index = 0
diffs = 0
str_length = len(bin_num_1)

for i in range(1, str_length):
    if bin_num_2[i] != bin_num_1[i]:
        diffs += 1

print(diffs)
        
# while True:
#     for _ in bin_num_1:
#         if bin_num_1[index] == bin_num_2[index]:
#             index += 1
#         else:
#             index += 1
#             diffs += 1
#     break
# print(diffs)