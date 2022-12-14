MIN_CODES = 33
MAX_CODES = 127
COLUMNS = 1
codes = ""
LINE_SIZE = 5

for code in range(MIN_CODES, MAX_CODES + 1):
    codes += f"{code:03d} = {chr(code)} "
    if COLUMNS % LINE_SIZE == 0:
        print(codes)
        codes = ""
    COLUMNS +=1