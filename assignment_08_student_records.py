# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add_student():
    print("\n--- Add Student ---")
    name = input("Student name: ")
    student_id = input("Student ID: ")
    
    # Initialize a list to hold the scores
    scores_list = []
    
    num_scores = int(input("How many scores? "))
    
    # Collect scores one by one
    for i in range(1, num_scores + 1):
        score = float(input("Enter score " + str(i) + ": "))
        scores_list.append(score)
        
    # Create the student dictionary
    new_student = {
        "name": name,
        "id": student_id,
        "scores": scores_list
    }
    
    # Add the dictionary to our global database list
    student_database.append(new_student)
    print("Student \"" + name + "\" added successfully.")




def display_all_students():
    print("\n--- Display All Students ---")
    
    # Check if the list is empty
    if len(student_database) == 0:
        print("No student records found. Please add a student first.")
        return
        
    print("------------------------------------------------------------")
    print("Name           ID          Scores               Average")
    print("------------------------------------------------------------")
    
    for student in student_database:
        # Calculate the average
        total = sum(student["scores"])
        count = len(student["scores"])
        
        if count > 0:
            avg = round(total / count, 2)
        else:
            avg = 0.0
            
        # Convert list of scores to a readable string manually
        scores_str = ""
        for s in student["scores"]:
            scores_str += str(int(s)) + ", "
        scores_str = scores_str[:-2] # Strip off the last trailing comma and space
        
        # Simple spacing using tabs or spaces for basic alignment
        print(student["name"], "   ", student["id"], "   ", scores_str, "       ", avg)
        
    print("------------------------------------------------------------")




def calculate_specific_average():
    print("\n--- Calculate Average Score ---")
    search_id = input("Enter student ID: ")
    
    # Variable to track if we found the student
    found = False
    
    for student in student_database:
        if student["id"] == search_id:
            found = True
            
            # Calculate average
            total = sum(student["scores"])
            count = len(student["scores"])
            
            if count > 0:
                avg = round(total / count, 2)
            else:
                avg = 0.0
                
            print(student["name"] + "'s average score: " + str(avg))
            break # Exit loop early since IDs should be unique
            
    if found == False:
        print("Error: Student ID " + search_id + " not found.")




def main_menu():
    # Loop indefinitely until the user chooses option 4
    while True:
        print("\n================================")
        print("   STUDENT RECORD SYSTEM MENU")
        print("================================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            calculate_specific_average()
        elif choice == "4":
            print("Thank you for using the system. Goodbye!")
            break # Breaks the while loop to end the program
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")




# --- Run Program ---
if __name__ == "__main__":
    main_menu()