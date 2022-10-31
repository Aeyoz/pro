trial_numbers = 9
lowest_number = 0
x_solution = 0

for number in range(-trial_numbers,trial_numbers + 1):
    x = number
    formula = x ** 2 - 6 * x + 3
    if formula < lowest_number:
        lowest_number = formula
        x_solution = x
        
print(f"The solution to the formula f(x) = x^2 -6x +3 is f({lowest_number}) being x = {x_solution} ")