tasks = []

while True:
    print("\n--- To-Do List ---")
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

    print("\nWhat do you want to do?")
    print("1. Add task")
    print("2. Delete task")
    print("3. Mark task as done")
    print("4. Quit")

    choice = input("\nEnter choice (1/2/3/4): ")

    if choice == "1":
        new_task = input("Enter task: ")
        tasks.append(new_task)
        print(f"'{new_task}' added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            task_num = int(input("Enter task number to delete: "))
            if task_num < 1 or task_num > len(tasks):
                print("Invalid task number!")
            else:
                removed = tasks.pop(task_num - 1)
                print(f"Deleted: '{removed}'")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to mark!")
        else:
            task_num = int(input("Enter task number to mark as done: "))
            if task_num < 1 or task_num > len(tasks):
                print("Invalid task number!")
            else:
                if "✅" in tasks[task_num - 1]:
                    print("Already marked as done!")
                else:
                    tasks[task_num - 1] = tasks[task_num - 1] + " ✅ "
                    print("Task marked as done!")

    elif choice == "4":
        print("Goodbye! Stay productive!")
        break

    else:
        print("Invalid choice! Enter 1, 2, 3 or 4.")