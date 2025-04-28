def main():
    print("Welcome to Task Manager!")
    tasks = []
    while True:
        command = input("Command (add, list, done, quit): ").strip().lower()
        if command == "add":
            add_task(tasks)
        elif command == "list":
            list_tasks(tasks)
        elif command == "done":
            complete_task(tasks)
        elif command == "quit":
            break
        else:
            print("Unknown command.")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    tasks.append({"task": task, "completed": False})

def list_tasks(tasks):
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['task']}")

def complete_task(tasks):
    list_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")
