trial_numbers = 9
min_func = 0
for x in range(-trial_numbers,trial_numbers + 1):
    formula = x ** 2 - 6 * x + 3
    if formula < min_func:
        min_func = formula
        min_x = x
        
print(f"The solution to the formula f(x) = x^2 -6x +3 is f({min_func}) being x = {min_x}")