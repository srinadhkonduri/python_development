# making to do list program

# 1 . initialize an empty list to store tasks
tasks = []


# 2 . function to add new task
def add_task(task):
    tasks.append(task)
    print("task added", task)


# 3 . function to view all tasks
def view_task():
    if tasks:
        print("tasks or", tasks in enumerate(tasks, start=1))
        print(f"index {tasks}")
    else:
        print("no tasks display")


# 4 . function to mark as task is completed
def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        complete_task = tasks.pop(task_index-1)
        print("task completed",complete_task)
    else:
        print("invalid task index")


# 5 . main loop
while True:
    print("\n select an option:")
    print("1 . add task")
    print("2 . view task")
    print("3 . complete task")
    print("4 . quit")
    choice = input("enter your choice")
    if choice == "1":
        new_task = input("enter the task: ")
        add_task(new_task)
    elif choice == "2":
        view_task()
    elif choice == "3":
        task_index = int(input("enter the number to mark as complete"))
        complete_task(task_index)
    elif choice == "4":
        print("goodBye")
        break
    else:
        print("invalid choice please choose again ")
