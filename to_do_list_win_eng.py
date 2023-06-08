import os
import time
from utils_fr import *
from utils_eng import *

def tdl_win_eng():
    tasks = load_tasks()
    tasks_completed = load_completed_tasks()
    os.system("cls")
    print("Windows\n")
    print("Version 1.0\n")
    time.sleep(1)
    os.system("cls")
    while True:
        x = gui_eng()
        if x == "1":
            os.system("cls")
            task = add_task()
            tasks.append(task)
            print("Task added!")
            time.sleep(1)
            os.system("cls")
        elif x == "2":
            os.system("cls")
            i = remove_task()
            tasks_completed.append(tasks[i])
            tasks.remove(tasks[i])
            print("Task removed!")
            time.sleep(2)
            os.system("cls")
        elif x == "3":
            os.system("cls")
            display_tasks(tasks)
            time.sleep(1)
            os.system("cls")
        elif x == "4":
            os.system("cls")
            display_completed_tasks(tasks_completed)
            time.sleep(1)
            os.system("cls")
        elif x == "5":
            os.system("cls")
            clean_completed_tasks()
            print("Completed tasks cleaned!")
            tasks_completed = load_completed_tasks()
            time.sleep(1)
            os.system("cls")
        elif x == "6":
            save_tasks(tasks)
            save_completed_tasks(tasks_completed)
            os.system("cls")
            break
        else:
            print("Unknown command!")
            time.sleep(1)
            os.system("cls")
