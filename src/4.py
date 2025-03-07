import random

def get_random_math_problem():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    operators = ["+", "-", "*", "/"]
    problem = ""
    for i in range(random.randint(2, 3)):
        number1 = random.choice(numbers)
        number2 = random.choice(numbers)
        operator = random.choice(operators)
        problem += str(number1) + " " + operator + " " + str(number2) + "="
    return problem
