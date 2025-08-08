import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "date": datetime.date.today(), "done": False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nYour Tasks:")
        for i, t in enumerate(self.tasks, 1):
            status = "Done" if t["done"] else "Pending"
            print(f"{i}. {t['task']} - Added on {t['date']} - Status: {status}")

    def mark_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["done"] = True
            print(f"Task '{self.tasks[task_number - 1]['task']}' marked as done.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f"Task '{removed['task']}' deleted.")
        else:
            print("Invalid task number.")

def main():
    todo = ToDoList()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            num = int(input("Enter task number to mark as done: "))
            todo.mark_done(num)
        elif choice == "4":
            num = int(input("Enter task number to delete: "))
            todo.delete_task(num)
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
