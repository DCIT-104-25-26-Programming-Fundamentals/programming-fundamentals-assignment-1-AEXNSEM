# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

todo_list = []


def add_task():
    print("\n--- Add a Task ---")
    task = input("Enter task: ")
    
    # Save the task to our list
    todo_list.append(task)
    print("Task added: \"" + task + "\"")




def view_tasks():
    print("\n--- Your Tasks ---")
    
    # Check if the list has no items
    if len(todo_list) == 0:
        print("Your to-do list is empty!")
        return
    
    # Loop through the list and display each item with a 1-based number
    for i in range(len(todo_list)):
        display_number = i + 1
        print(str(display_number) + ". " + todo_list[i])




def delete_task():
    print("\n--- Delete a Task ---")
    
    # Check if there is anything to delete first
    if len(todo_list) == 0:
        print("There are no tasks to delete.")
        return
        
    # Show current tasks so the user can pick the right number
    for i in range(len(todo_list)):
        print(str(i + 1) + ". " + todo_list[i])
        
    print()
    choice_num = int(input("Enter task number to delete: "))
    
    # Convert the user's 1-based number back to a 0-based Python index
    target_index = choice_num - 1
    
    # Validate if the index actually exists in our list bounds
    if target_index >= 0 and target_index < len(todo_list):
        # Remove the item and capture its text before it disappears
        removed_task = todo_list.pop(target_index)
        print("Task \"" + removed_task + "\" has been removed.")
    else:
        print("Error: Invalid task number!")




def main_menu():
    # Infinite loop to keep running until option 4 is selected
    while True:
        print("\n============================")
        print("     TO-DO LIST MENU")
        print("============================")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break # Breaks out of the while loop to stop the program
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")




# --- Run Program ---
if __name__ == "__main__":
    main_menu()

