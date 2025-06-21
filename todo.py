print("Welcome to the To-Do List App!")
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    with open(TASKS_FILE) as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("Your Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t['title']}")

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title})
    save_tasks(tasks)
    print("Task added.")

def delete_task():
    tasks = load_tasks()
    list_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def update_task():
    tasks = load_tasks()
    list_tasks()
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("Enter new task title: ")
            tasks[index]['title'] = new_title
            save_tasks(tasks)
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            update_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            
if __name__ == "__main__":
    main()            