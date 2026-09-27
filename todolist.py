# Simple To-Do List App

tasks = []

def show_tasks():
    print("\n===== YOUR TASKS =====")

    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, start=1):
            if task["completed"]:
                status = "✓"
            else:
                status = " "

            print(f"{i}. [{status}] {task['name']}")


def add_task():
    task_name = input("\nEnter your task: ")

    if task_name.strip() == "":
        print("Task cannot be empty!")
    else:
        task = {
            "name": task_name,
            "completed": False
        }

        tasks.append(task)
        print("Task added successfully!")


def complete_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("\nEnter task number to complete: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number.")


def delete_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Deleted: {deleted_task['name']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number.")


# Main program
while True:

    print("\n===== TO-DO LIST =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please try again.")

