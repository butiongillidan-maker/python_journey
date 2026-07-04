# Project 1 — Task Manager Planning
## What does this app do?
> A command-line task manager that lets users view, add, complete, and remove tasks from a running list, all through a simple numbered menu.
---

## Goal 
- [✓] create a working code
- [✓] Create a working CLI program
- [✓] Menu-driven interface with numbered options

## Step By Step Logic
---
    START
    Create an empty list called task_list
    Loop continuously (while True):
        Print menu: 1. View  2. Add  3. Complete/Remove  4. Exit
        Get user's choice
        
        IF choice == 1:
            IF list is empty: print message
            ELSE: print all tasks with numbers
        
        ELIF choice == 2:
            Get new task from user
            Append to task_list
        
        ELIF choice == 3:
            IF list is empty: print message
            ELSE: show tasks, get number to remove, pop() it
        
        ELIF choice == 4:
            Print goodbye message
            break
        
        ELSE:
            Print invalid option message
END
## Errors Encountered 
Used is instead of == for comparing numbers, which worked by accident in testing but is technically incorrect and was fixed.
Initially tried comparing an empty list directly to 0 (task_list is 0), which is invalid — fixed using len(task_list) == 0.
Forgot to indent the menu logic inside the while True loop at first, so the menu only showed once instead of repeating.

## Things That I've Learned
How to use .append() and .pop() to modify a list dynamically based on user input
The difference between == (value comparison) and is (identity comparison), and why == is almost always what you want
How to structure a menu-driven program using while True with break to exit cleanly
Zero-indexing matters when mapping user-facing numbers (1, 2, 3...) to actual list positions (0, 1, 2...)
