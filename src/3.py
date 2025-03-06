import random

def get_random_code():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)

    # Create a list of strings to represent operators
    operators = ["+", "-", "*", "/"]

    # Use a random operator from the list
    operator = random.choice(operators)

    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Use the random number and operator to create a math problem
    problem = f"{num1} {operator} {num2}"

    # Return the math problem as a string
    return problem