def user_input():
    x = 0
    x = input("What would you like to do?\n")
    return x

def gui_eng():
    cyan = "\033[1;36m"
    reset = "\033[0;0m"
    print(cyan + " _______      _____          _      _     _   ")
    print("|__   __|    |  __ \        | |    (_)   | |  ")
    print("   | | ___   | |  | | ___   | |     _ ___| |_ ")
    print("   | |/ _ \  | |  | |/ _ \  | |    | / __| __|")
    print("   | | (_) | | |__| | (_) | | |____| \__ \ |_ ")
    print("   |_|\___/  |_____/ \___/  |______|_|___/\__|")
    print("       Version 1.0         by LouisVDE")
    print(reset)    
    print('\n')
    print("What would you like to do?")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display tasks")
    print("4. Display completed tasks")
    print("5. Clean completed tasks")
    print("6. Quit")
    x = input("Your choice: ")
    return x

def add_task():
    task = input("What task would you like to add?\n")
    return task

def remove_task():
    task_index = int(input("Which task would you like to remove?\n"))
    return task_index - 1

def display_tasks(tasks):
    print("Here are your tasks:")
    for i in range(len(tasks)):
        print(str(i+1) + ". " + tasks[i])

def display_completed_tasks(tasks_completed):
    print("Here are your completed tasks:")
    for i, task in enumerate(tasks_completed):
        print(str(i+1) + ". " + task)

def load_completed_tasks():
    tasks_completed = []
    with open("tasks_completed.txt", "r") as file:
        for line in file:
            tasks_completed.append(line.strip())
    return tasks_completed

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def save_completed_tasks(tasks_completed):
    with open("tasks_completed.txt", "w") as file:
        for task in tasks_completed:
            file.write(task + "\n")

def load_tasks():
    tasks = []
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
    return tasks

def clean_completed_tasks():
    with open("tasks_completed.txt", "w") as file:
        file.write("")
