task_list = [
    "going to sleep",
    "eat breakfast",
    "do a coding in python",
    "play videogames",
    "study operating systems in cisco"
]

# 1. Start the infinite loop here
while True:
    print("1. View Task\n 2. Add a task\n 3. Complete / Remove task\n 4. Exit")
    choices = int(input("My choice: "))

    # 2. All of this must be indented inside the while loop
    if choices == 1:
        if not task_list:
            print("task is empty! no task is scheduled")
        else:
            addition = 0
            for task in task_list:
                addition = addition + 1
                print(f"{addition}: {task}")
                
    elif choices == 2:
        new_task = input("Add a New Task: ")
        task_list.append(new_task)
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
            print(f"The {removed_task} is complete and removed!")
            
    elif choices == 4:
        print("Exiting Task manager. keep monitoring your work today!")
        break
    else:
        print("Invalid option please enter 1 to 4 only and try again!")
