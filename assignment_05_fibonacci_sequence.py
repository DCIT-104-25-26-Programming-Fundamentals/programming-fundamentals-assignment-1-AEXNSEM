# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def fibonacci(n):
    if n <= 0:
        print("Invalid input, try again.")
    else:
        sequence=[]
        a = 0
        b = 1
        for i in range(n):
                sequence.append(a)
                a = b
                b = a+b
    print("Fibonacci sequence: ", " ".join(map(str,sequence)))
            
def check(num):
        if num<0:
               print("Invalid input, try again.")
               return False
        
        a=0
        b=1
        while a < num:
                a=b
                b=a+b    
                if a == num:
                    return True
                else:
                    return False
        
           
try:        
    term=int(input("How many terms? \n"))
    fibonacci(term)
    print  ("fibonacci sequence of first", term,"terms")
except ValueError:
    print  ("Invalid input: please enter a valid integer.")

print(" "*40)

try:
    check_num=int(input("Enter a number to check: "))
    if check(check_num):
         print(check_num, "is a fibonacci number.")
    else:
         print("is NOT a fibonacci number.")
except ValueError:
     print("Invalid input, please enter valid input.")
     
