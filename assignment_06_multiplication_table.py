# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

#functions


#functions


def single(num):
    table_line=[]
    for i in range(1, 13):
            answer = num * i
            table_line.append(f"{num} * {i} = {answer}")
    return table_line


def multiple(n):
    multi=[]
    for m in range (1, n+1):
        table_line=[]
            
        for i in range(1, 13):
                answer = m * i
                table_line.append(f"{m} * {i} = {answer}")
        multi.append(table_line)
    return multi    
print("============================================")


print("--- PART A: Single Table ---")
single_num = -1 
try:
    single_num = int(input("Enter a number for the table: "))
except ValueError:
    print("Invalid entry: Please enter a valid integer.")

if single_num > 0:
    results = single(single_num)
    print()
    print("Multiplication Table for", single_num, ":")
    for line in results:
        print(line)
elif single_num == 0 or single_num < -1:
    print("Error: Please enter a positive integer.")

print("\n--- PART B: Tables from 1 to N ---")
multiple_n = -1 
try:
    multiple_n = int(input("Enter a number N for tables 1 to N: "))
except ValueError:
    print("Invalid entry: Please enter a valid integer.")


if multiple_n > 0:
    result = multiple(multiple_n)
    for index, lines in enumerate(result, start=1):
        print()
        print("Multiplication Table for", index, ":")
        for line in lines:
            print(line)
        print("============================================")
elif multiple_n == 0 or multiple_n < -1:
    print("Error: Please enter a positive integer.")