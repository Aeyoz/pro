# ******************
# FIBONACCI ITERABLE
# ******************

from __future__ import annotations

class Fibonacci:
    def __init__(self, limit: int):
        self.iteration_limit = limit
        self.current_iteration = 0
        self.first_num = 0
        self.second_num = 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current_iteration == self.iteration_limit:
            raise StopIteration
        self.current_iteration += 1
        result = self.first_num 
        self.first_num, self.second_num = self.second_num, self.first_num + self.second_num
        return result

def run(n: int) -> list:
    fibo = list(Fibonacci(n))
    return fibo