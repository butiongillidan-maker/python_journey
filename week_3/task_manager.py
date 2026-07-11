import os

if os.path.exists("task.txt"):
    with open("task.txt", "r")as file:
        task_list = [line.strip() for line in file]

else:
    task_list = []

def save_task():
    with open("task.txt", "w")as file:
        for task in task_list:
            file.write(task)
            file.write("\n")


while True:
    print("1. View Task\n 2. Add a task\n 3. Complete / Remove task\n 4. Exit")
    choices = int(input("My choice: "))

    if choices == 1:
        if not task_list:
            print("task is empty! no task is scheduled")
        else:
            addition = 0
            for task in task_list:
                addition = addition + 1
                print(f"{addition}: {task}", "\n")
                
    elif choices == 2:
        new_task = input("Add a New Task: ")
        task_list.append(new_task)
        save_task()
        
        print("task added successfully!")
        
    elif choices == 3:
        if len(task_list) == 0:
            print("No task available to complete.")
        else:
            addition = 0
            for task in task_list:
                addition += 1
                print(f"{addition}: {task}")
            completed_num = int(input("Enter the number of task you completed: "))
            removed_task = task_list.pop(completed_num - 1)
            save_task()
            print(f"The {removed_task} is complete and removed!")
            
    elif choices == 4:
        print("Exiting Task manager. keep monitoring your work today!")
        break
    else:
        print("Invalid option please enter 1 to 4 only and try again!")
