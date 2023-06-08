import os
import time
from utils_fr import *

def tdl_mac_eng():
    tasks = load_tasks()
    tasks_completed = load_completed_tasks()
    os.system("clear")
    print("MacOs")
    time.sleep(1)
    os.system("clear")
    while True:
        os.system("clear")
        x = gui_fr()
        if x == "1":
            os.system("clear")
            task = add_task()
            tasks.append(task)
            print("Task added!")
            time.sleep(1)
            os.system("clear")
        elif x == "2":
            os.system("clear")
            i = remove_task()
            tasks_completed.append(tasks[i])
            tasks.remove(tasks[i])
            print("Task removed!")
            time.sleep(2)
            os.system("clear")
        elif x == "3":
            os.system("clear")
            display_tasks(tasks)
            time.sleep(1)
            os.system("clear")
        elif x == "4":
            os.system("clear")
            display_completed_tasks(tasks_completed)
            time.sleep(1)
            os.system("clear")
        elif x == "5":
            os.system("clear")
            clean_completed_tasks()
            print("Completed tasks cleaned!")
            tasks_completed = load_completed_tasks()
            time.sleep(1)
            os.system("clear")
        elif x == "6":
            save_tasks(tasks)
            save_completed_tasks(tasks_completed)
            os.system("clear")
            break
        else:
            print("Unknown command!")
            time.sleep(1)
            os.system("clear")
