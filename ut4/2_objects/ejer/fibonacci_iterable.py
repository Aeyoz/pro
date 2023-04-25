# ******************
# FIBONACCI ITERABLE
# ******************

class Fibonacci:
    def __init__(self, limit: int):
        self.limit = limit
        self.current_num = 0
        self.first_num = 0
        self.second_num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < 2:
            self.current_num += 1
            return self.first_num
#        if self.first_num and self.current_num == 0:
#            self.current_num += 1
#            return self.first_num
        if self.current_num == self.limit:
            raise StopIteration
        result = self.first_num + self.second_num
        self.first_num = self.second_num
        self.second_num = result
        self.current_num += 1
        return result

#pepe = Fibonacci(20)
#fibo = []
#for i in pepe:
#    fibo.append(i)
#print(fibo)

#Sucesion de fibonacci
N = 0
M = 1
repetitions = int(input("Times to execute?: "))
result = 0

for _ in range(repetitions + 1):
    print(result)
    result = N + M
    N = M
    M = result
