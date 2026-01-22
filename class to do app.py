class TodoList:
    def _init_(self):
        self.tasks = []  # List of dicts: {"description": str, "status": str}

    def add_task(self, description):
        self.tasks.append({"description": description, "status": "Pending"})
        print("Task added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['description']} - {task['status']}")

    def mark_completed(self, index):
        try:
            idx = int(index) - 1
            if 0 <= idx < len(self.tasks):
                self.tasks[idx]["status"] = "Completed"
                print("Task marked as completed.")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_task(self, index):
        try:
            idx = int(index) - 1
            if 0 <= idx < len(self.tasks):
                del self.tasks[idx]
                print("Task deleted.")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def run(self):
        while True:
            print("\nTo-Do List Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                description = input("Enter task description: ")
                self.add_task(description)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                index = input("Enter task index to mark completed: ")
                self.mark_completed(index)
            elif choice == "4":
                index = input("Enter task index to delete: ")
                self.delete_task(index)
            elif choice == "5":
                print("Exiting.")
                break
            else:
                print("Invalid choice. Try again.")

# To run the application
if _name_ == "_main_":
    todo = TodoList()
    todo.run()