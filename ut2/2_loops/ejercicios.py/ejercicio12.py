min_codes = 33
max_codes = 127
line = 1
codes = ""

for code in range(min_codes, max_codes + 1):
    codes += f"{code} = {chr(code)} | "
    if line % 5 == 0:
        print(codes)
        codes = ""
    line +=1