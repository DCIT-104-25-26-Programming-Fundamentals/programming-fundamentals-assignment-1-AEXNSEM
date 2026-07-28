# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add(num1, num2):
    result = num1 + num2
    print("Result:", num1, "+", num2, "=", result)


def subtract(num1, num2):
    result = num1 - num2
    print("Result:", num1, "-", num2, "=", result)


def multiply(num1, num2):
    result = num1 * num2
    print("Result:", num1, "*", num2, "=", result)


def divide(num1, num2):
    # Handle division by zero 
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        # Round division to 2 decimal places
        result = round(num1 / num2, 2)
        print("Result:", num1, "/", num2, "=", result)


def modulus(num1, num2):
    # Modulus also fails if dividing by zero
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 % num2
        print("Result:", num1, "%", num2, "=", result)


def exponentiate(num1, num2):
    result = num1 ** num2
    print("Result:", num1, "**", num2, "=", result)




def main_menu():
    # Loop keeps the program running until option 7 is selected
    while True:
        print("\n============================")
        print("     SIMPLE CALCULATOR")
        print("============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")
        
        choice = input("Select an operation (1-7): ")
        
        # If user wants to quit, exit immediately before asking for numbers
        if choice == "7":
            print("Goodbye!")
            break
            
        # Check if the input matches any valid math operation choice
        if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6":
            # Collect the numbers from the user
            n1 = float(input("Enter first number : "))
            n2 = float(input("Enter second number: "))
            
            # Direct to the correct function based on the choice
            if choice == "1":
                add(n1, n2)
            elif choice == "2":
                subtract(n1, n2)
            elif choice == "3":
                multiply(n1, n2)
            elif choice == "4":
                divide(n1, n2)
            elif choice == "5":
                modulus(n1, n2)
            elif choice == "6":
                exponentiate(n1, n2)
        else:
            print("Invalid choice! Please select a number between 1 and 7.")




# main code
if __name__ == "__main__":
    main_menu()