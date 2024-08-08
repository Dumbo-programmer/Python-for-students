import json
from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority, due_date):
        task = {
            "description": description,
            "priority": priority,
            "due_date": due_date
        }
        self.tasks.append(task)
        print(f"Task added: {description}")

    def remove_task(self, description):
        for task in self.tasks:
            if task['description'] == description:
                self.tasks.remove(task)
                print(f"Task removed: {description}")
                return
        print("Task not found")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("Your tasks:")
        for task in self.tasks:
            desc = task['description']
            priority = task['priority']
            due_date = task['due_date']
            print(f"- {desc} (Priority: {priority}, Due: {due_date})")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)
        print("Tasks saved successfully!")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
            print("Tasks loaded successfully!")
        except FileNotFoundError:
            print("No previous tasks found.")
        except json.JSONDecodeError:
            print("Error loading tasks.")

def prompt_for_task():
    description = input("Enter the task description: ")
    priority = input("Enter the task priority (High, Medium, Low): ").capitalize()
    due_date = input("Enter the task due date (YYYY-MM-DD) or leave blank: ")
    if due_date:
        try:
            datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return None, None, None
    return description, priority, due_date

def todo_list():
    todo = ToDoList()
    todo.load_tasks("tasks.json")

    while True:
        action = input(
            "Enter 'add' to add a task, 'remove' to remove a task, 'view' to view tasks, "
            "'save' to save tasks, 'load' to load tasks, 'quit' to quit: "
        ).lower()

        if action == 'add':
            desc, priority, due_date = prompt_for_task()
            if desc:
                todo.add_task(desc, priority, due_date)
        elif action == 'remove':
            task = input("Enter the task description to remove: ")
            todo.remove_task(task)
        elif action == 'view':
            todo.view_tasks()
        elif action == 'save':
            todo.save_tasks("tasks.json")
        elif action == 'load':
            todo.load_tasks("tasks.json")
        elif action == 'quit':
            todo.save_tasks("tasks.json")
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid action")

if __name__ == "__main__":
    todo_list()
