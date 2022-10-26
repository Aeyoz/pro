N = 0
M = 1
repetitions = int(input("Times to execute?: "))
result = 0

for _ in range(repetitions + 1):
    print(result)
    result = N + M
    N = M
    M = result
        