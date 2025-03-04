def get_random_code():
    import random

    # Generate a random number between 1 and 10
    num = random.randint(1, 10)

    # Generate a random operator (+, -, *, /)
    op = random.choice(["+", "-", "*", "/"])

    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Calculate the answer
    ans = eval(f"{num1} {op} {num2}")

    return f"What is {num1} {op} {num2}?"
