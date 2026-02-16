def sum_numbers(a, b):
    return a + b


try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", sum_numbers(a, b))
except ValueError:
    print("Please enter valid numbers.")
