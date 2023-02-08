def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number1 = int(input("Introduce the first number: "))
number2 = int(input("Introduce the second number: "))
operator = input('''Introduce one of the following operators:

1. + (Returns the addition of two numbers)
2. - (Returns the difference between 2 numbers)
3. / (Returns the result of the division between the two numbers)
4. * (Returns the product of the two numbers)
5. ^ (Returns the result of exponentiation the first number to the second one)
6. ! (Returns the factorial of a number, just one, so you will have to choose between them, a factorial is the product of the number and all that preceeds it)
7. % (Returns the module of a division, let's say 13 / 2, the module would be 1)
Your choice: ''')

ERROR = "Something went wrong"
operators = "+ - * / ^ %"
result = ""

match operator:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "/":
        result = number1 / number2
    case "*":
        result = number1 * number2
    case "^":
        result = number1 ** number2        
    case "%":
        result = number1 % number2
    case "!":
        n = int(input(f'''Choose one of the two numbers to show it's factorial:  
1. {number1}
2. {number2}
Your choice: '''))
        if n == 1:
            result = factorial(number1)
        elif n == 2:
            result = factorial(number2)
        else:
            print(ERROR)

match operator:
    case operator if operator in operators:
        print(f"\nThe result of your desired operation is {result}")
    case "!" if operator == "!" and result != "":
        print(f"\nThe result of your factorial is {result}")
    case _:
       print(ERROR)