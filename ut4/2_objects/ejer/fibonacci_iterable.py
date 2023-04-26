# ******************
# FIBONACCI ITERABLE
# ******************

class Fibonacci:
    def __init__(self, limit: int):
        self.iteration_limit = limit
        self.current_iteration = 0
        self.first_num = 0
        self.second_num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_iteration == self.iteration_limit:
            raise StopIteration
        if self.current_iteration == 0:
            self.current_iteration +=1
            return self.first_num
        if self.current_iteration == 1:
            self.current_iteration += 1
            return 1
        result = self.first_num + self.second_num
        self.first_num, self.second_num = self.second_num, self.first_num + self.second_num
        self.current_iteration += 1
        return result

def run(n):
    fibo_gen = Fibonacci(n)
    fibo = list(fibo_gen)
    return fibo