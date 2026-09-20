import json
import os

Task_data = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(Task_data):
        return []
    try:
        with open(Task_data, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read the task file.")
        return []

# Save tasks to JSON file
def save_tasks(tasks):
    try:
        with open(Task_data, "w") as file:
            json.dump(tasks, file, indent=4)
    except OSError:
        print("Could not save the task file.")

# Add a new task 
def add_task(tasks):
    print("\n---- ADD TASK ----")
    task_name = input("Enter your task that need to be done: ").strip()
    if task_name == "":
        print("Task cannot be empty.")
        return
        
    # Category selection
    print("\nSelect Category of your task:")
    print("1. Short-term \n2. Long-term")
    c_choice = input("Enter your choice (1 or 2): ")
    if c_choice == "1":
        category = "Short-term"
    elif c_choice == "2":
        category = "Long-term"
    else:
        print("Invalid choice.")
        return
        
    # Priority
    print("\nSelect Priority of your task:")
    print("1. High \n2. Medium \n3. Low")
    p_choice = input("Enter your choice (1, 2, or 3): ")
    if p_choice == "1":
        priority = "High"
    elif p_choice == "2":
        priority = "Medium"
    elif p_choice == "3":
        priority = "Low"
    else:
        print("Invalid Priority.")
        return
        
    # Create a new task dictionary
    task = {
        "name": task_name,
        "category": category,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("\nTask added successfully!")

# View all tasks 
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\n---- YOUR TASKS ----")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(
            f"{index}. [{status}] "
            f"{task['name']} "
            f"| Category: {task['category']} "
            f"| Priority: {task['priority']} "
        )

# Delete a task
def delete_task(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        if task_number < 1 or task_number > len(tasks):
            print("Task does not exist.")
            return
        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"\nTask '{deleted_task['name']}' deleted successfully!")
    except ValueError:
        print("Please enter a valid task number.")

# Mark a task as completed 
def mark_done(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to mark as completed: "))
        if task_number < 1 or task_number > len(tasks):
            print("Task does not exist.")
            return
        
        # Pull the specific task from the list
        task = tasks[task_number - 1]
        
        if task["completed"]:
            print(f"\nTask '{task['name']}' is already marked as completed.")
            return
            
        task["completed"] = True
        save_tasks(tasks)
        print(f"\nTask '{task['name']}' marked as completed!")
    except ValueError:
        print("Please enter a valid task number.")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        print("\n---- TO-DO LIST ----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            print("Thank you for using the To-Do List app.")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
