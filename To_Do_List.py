# Simple To-Do List Manager

'''
- This Python program serves as a user-friendly to-do list manager, allowing users to easily organize and track their tasks.
- Upon launching the program, users are greeted with a warm welcome message and presented with a menu offering various options.
- Users can add new tasks to the list, mark existing tasks as complete, view all tasks with their completion status, or exit the program.
- The program utilizes a list of tasks, each represented by a dictionary containing a task name and a completion status (True or False).
- Each menu option is implemented as a function, and the main loop continuously prompts the user for input until they choose to exit.
- Comments are included throughout the code to provide clear explanations, making it accessible for users and future developers alike.
- Enjoy a straightforward and effective task management experience with this Simple To-Do List Manager!

'''

# Initialize a list of tasks with their completion status
tasks = [
    {"task": "Quraan", "status": True},
    {"task": "Salah", "status": True},
    {"task": "Playing sports", "status": False},
    {"task": "Study", "status": False},
    {"task": "Visit Hamada", "status": False}
]

# Main function to manage the to-do list program
def main():
    print("Welcome to the Simple To-Do List Manager! 😊")
    print("Keep track of your tasks effortlessly.")
    
    # Display a menu with options for the user
    message = '''1 - Add tasks to a list\n2 - Mark a task as complete\
    \n3 - View all tasks\n4 - Quit'''

    while True:
        print(message)
        choice = input('Enter your choice: ')

        # Process the user's choice and perform the corresponding action
        if choice == "1":
            add_task()  # Add a new task to the list
        elif choice == "2":
            mark_complete(tasks)  # Mark a task as complete
        elif choice == "3":
            view_tasks(tasks)  # View all tasks and their completion status
        elif choice == "4":
            break  # Exit the program if the user chooses to quit
        else:
            print("Invalid choice, please enter a number between 1 and 4")

# Function to add a new task to the list
def add_task():
    task = input("Enter the task: ")

    # Create a dictionary for the new task and add it to the list
    task_info = {"task": task, "status": False}
    tasks.append(task_info)

    print("Task added to the list successfully")
    print("-" * 30)

# Function to mark a task as complete
def mark_complete(list_tasks):
    # Create a list of uncompleted tasks
    uncompleted_list = [task for task in list_tasks if not task["status"]]
    
    # check are there tasks? 
    if not uncompleted_list:
        print("No task to mark")
        return

    print("\nList of tasks uncompleted: 🔻\n")
    for i, task in enumerate(uncompleted_list):
        print(f"{i + 1}. {task['task']}")
        print("-" * 15)

    try:
        # Prompt the user to choose a task to mark as complete
        task_num = int(input("Enter the task number to mark complete: "))

        if task_num < 1 or task_num > len(uncompleted_list):
            print("Invalid Task Number")
            return

        # Mark the selected task as complete
        uncompleted_list[task_num - 1]['status'] = True

        print("Task marked completed")
        print("-" * 30)

    except ValueError:
        print("Invalid input, please enter a number!")

# Function to view all tasks and their completion status
def view_tasks(list_tasks):
    # check are there tasks? 
    if not list_tasks:
        print("No tasks to view")
        return

    print("\nList of tasks: 🔻\n")
    for i, task in enumerate(list_tasks):
        # Display the task name and its completion status
        status = "✔" if task['status'] else "❌"
        print(f"{i + 1}. {task['task']}: {status}")

    print("-" * 30)

# Call the main function to start the to-do list program
main()
