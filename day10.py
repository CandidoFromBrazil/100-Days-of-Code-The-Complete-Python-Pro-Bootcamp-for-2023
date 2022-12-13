# link to game in replit: https://replit.com/@MatheusWillians/calculator-final?v=1, you can always fork it
# All the project and the inherent libraries are in the additional folder to be downloaded by you, is a folde named: day10.py.zip, enjoy it

from replit import clear
from art import logo

#Calculator V.2


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# dictionary used to orientation through the calculator
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    # input
    num1 = float(input("What's the first number?: "))
    # looking through the keys inside the dictionary
    for symbol in operations:
        print(symbol)
    should_continue = True
    # while for whiley kk
    # logic for the right function call by symbol chosen
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        # using the symbol chosen as a index to reach the values inside the dictionary
        # rough-creation of the calculation_symbol() function
        calculation_function = operations[operation_symbol]
        #calling the calculation_symbol() and assigning it
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        #if for the recursion use of the calculator() function
        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        ) == 'y':
            # re-assinging the value of the answer to re-use in the num1
            num1 = answer
        else:
            should_continue = False
            #clear function, and most important, the call of a functiion who call's itself. RECURSION CALL
            clear()
            calculator()


# first call of the function
calculator()
