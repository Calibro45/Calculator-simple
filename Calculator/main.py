# Calculator
from art import logo


# Add
def add(n1, n2):
    """addiction function"""
    return n1 + n2


# Subtract
def subtract(n1, n2):
    """Subtract function"""
    return n1 - n2


# Multiply
def multiply(n1, n2):
    """Multiply function"""
    return n1 * n2


# Divide
def divide(n1, n2):
    """Divide fucntion"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")

        continue_calculate = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.").lower()

        if continue_calculate == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()