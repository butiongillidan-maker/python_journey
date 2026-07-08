import os

if os.path.exists("task.txt"):
    with open("task.txt", "r") as file:
        task_list = [line.strip() for line in file]
else:
    task_list = []

print("1. View Task\n2. Add a task\n3. Complete / Remove Task\n4. Exit App")
# which is i put up in task_list_manager

