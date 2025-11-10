from datetime import datetime

def add_task(tasks, history):
    name = input("Enter task name: ").strip()
    if not name:
        print("You entered nothing.\n")
        return

    # Priority input
    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
    if priority not in ["High", "Medium", "Low"]:
        priority = "Low"

    # Optional deadline
    deadline_input = input("Enter deadline (YYYY-MM-DD) or leave blank: ").strip()
    deadline = None
    if deadline_input:
        try:
            deadline = datetime.strptime(deadline_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Deadline ignored.")

    task = {"name": name, "priority": priority, "deadline": deadline}
    tasks.append(task)
    history.append(("add", task))
    print(f"Task added: {name} (Priority: {priority})\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.\n")
        return

    # Sort by priority first, then by deadline
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    sorted_tasks = sorted(
        tasks,
        key=lambda t: (priority_order[t["priority"]], t["deadline"] or datetime.max.date())
    )

    print("\nYour tasks:")
    for i, task in enumerate(sorted_tasks, start=1):
        deadline_str = task["deadline"].strftime("%Y-%m-%d") if task["deadline"] else "No deadline"
        print(f"{i}. {task['name']} [Priority: {task['priority']}, Deadline: {deadline_str}]")
    print()


def remove_task(tasks, history):
    view_tasks(tasks)
    if not tasks:
        return

    number = input("Enter task number to remove: ").strip()
    if number.isdigit():
        number = int(number)
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            history.append(("remove", removed))
            print("Removed:", removed["name"], "\n")
        else:
            print("Invalid task number.\n")
    else:
        print("Please enter a valid number.\n")


def undo_last_action(tasks, history):
    if not history:
        print("No actions to undo.\n")
        return
    action, task = history.pop()
    if action == "add":
        tasks.remove(task)
        print(f"Undo: Removed task '{task['name']}' added previously.\n")
    elif action == "remove":
        tasks.append(task)
        print(f"Undo: Restored task '{task['name']}' removed previously.\n")


def main():
    tasks = []
    history = []

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Undo Last Action")
        print("5. Exit")

        choice = input("Choose (1-5): ").strip()
        if choice == "1":
            add_task(tasks, history)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks, history)
        elif choice == "4":
            undo_last_action(tasks, history)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()