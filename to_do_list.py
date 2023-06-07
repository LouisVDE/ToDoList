import os
import time
from utils import *

def main():
    os.system("cls")
    tasks = load_tasks()
    tasks_completed = load_completed_tasks()
    while True:
        x = gui()
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
            time.sleep(1)
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
        elif x == "5":
            os.system("cls")
            clean_completed_tasks()
            print("Tâches complétées nettoyées !")
            tasks_completed = load_completed_tasks()
            time.sleep(1)
        elif x == "6":
            save_tasks(tasks)
            save_completed_tasks(tasks_completed)
            break
        else:
            print("Commande inconnue !")
            time.sleep(1)
            os.system("cls")

if __name__ == "__main__":
    main()