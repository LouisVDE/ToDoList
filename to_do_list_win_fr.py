import os
import time
from utils_fr import *

def tdl_win_fr():
    tasks = load_tasks()
    tasks_completed = load_completed_tasks()
    os.system("cls")
    print("Windows\n")
    time.sleep(1)
    os.system("cls")
    while True:
        x = gui_fr()
        if x == "1":
            os.system("cls")
            task = add_task()
            tasks.append(task)
            print("Tâche ajoutée !")
            time.sleep(1)
            os.system("cls")
        elif x == "2":
            os.system("cls")
            i = remove_task()
            tasks_completed.append(tasks[i])
            tasks.remove(tasks[i])
            print("Tâche supprimée !")
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
            print("Tâches complétées nettoyées !")
            tasks_completed = load_completed_tasks()
            time.sleep(1)
            os.system("cls")
        elif x == "6":
            save_tasks(tasks)
            save_completed_tasks(tasks_completed)
            os.system("cls")
            break
        else:
            print("Commande inconnue !")
            time.sleep(1)
            os.system("cls")
