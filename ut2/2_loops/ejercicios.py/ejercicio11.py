trial_numbers = 9
lowest_number = 0
for x in range(-trial_numbers,trial_numbers + 1):
    formula = x ** 2 - 6 * x + 3
    if formula < lowest_number:
        lowest_number = formula
        x_solution = x
        
print(f"The solution to the formula f(x) = x^2 -6x +3 is f({lowest_number}) being x = {x_solution} ")