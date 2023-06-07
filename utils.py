def user_input():
    x = input("Que voulez-vous faire ?\n")
    return x

def gui():
    print("Bienvenue dans votre To Do List !")
    print("Que voulez-vous faire ?")
    print("1. Ajouter une tâche")
    print("2. Supprimer une tâche")
    print("3. Afficher les tâches")
    print("4. Afficher les tâches complétées")
    print("5. Nettoyer les tâches complétées")
    print("6. Quitter")
    x = input("Votre choix : ")
    return x

def add_task():
    task = input("Quelle tâche voulez-vous ajouter ?\n")
    return task

def remove_task():
    task_index = int(input("Quelle tâche voulez-vous supprimer ?\n"))
    return task_index - 1

def display_tasks(tasks):
    print("Voici vos tâches :")
    for i in range(len(tasks)):
        print(str(i+1) + ". " + tasks[i])

def display_completed_tasks(tasks_completed):
    print("Voici vos tâches complétées :")
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