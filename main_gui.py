import tkinter as tk
from tkinter import messagebox

def set_french():
    global current_language
    current_language = "fr"
    tasks_menu.entryconfig(0, label="Tâches actives")
    tasks_menu.entryconfig(1, label="Tâches complétées")
    completed_tasks_menu.entryconfig(0, label="Supprimer tâche")
    add_button.config(text="Ajouter")
    remove_button.config(text="Supprimer")

def set_english():
    global current_language
    current_language = "en"
    tasks_menu.entryconfig(0, label="Active Tasks")
    tasks_menu.entryconfig(1, label="Completed Tasks")
    completed_tasks_menu.entryconfig(0, label="Delete Task")
    add_button.config(text="Add")
    remove_button.config(text="Remove")

# Fonction pour ajouter une tâche
def add_task(event=None):
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()

# Fonction pour supprimer une tâche
def remove_task():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        if current_list == "active":
            completed_task = tasks.pop(index)
            tasks_completed.append(completed_task)
            listbox.delete(index)
            save_tasks()
            save_completed_task(completed_task)
        elif current_list == "completed":
            tasks_completed.pop(index)
            listbox.delete(index)
            save_completed_tasks()

# Fonction pour basculer vers les tâches actives
def switch_to_active_tasks():
    global current_list
    current_list = "active"
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Fonction pour basculer vers les tâches complétées
def switch_to_completed_tasks():
    global current_list
    current_list = "completed"
    listbox.delete(0, tk.END)
    for task in tasks_completed:
        listbox.insert(tk.END, task)

# Fonction pour supprimer une tâche complétée
def delete_completed_task():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        tasks_completed.pop(index)
        listbox.delete(index)
        save_completed_tasks()
        completed_tasks_menu.delete(0, tk.END)
        for i, task in enumerate(tasks_completed):
            completed_tasks_menu.add_command(label=task, command=lambda i=i: delete_completed_task_menu(i))

# Fonction pour supprimer une tâche complétée depuis le menu
def delete_completed_task_menu(index):
    tasks_completed.pop(index)
    listbox.delete(index)
    save_completed_tasks()

# Fonction pour sauvegarder les tâches
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Fonction pour sauvegarder une tâche complétée
def save_completed_task(task):
    with open("tasks_completed.txt", "a") as file:
        file.write(task + "\n")

# Fonction pour sauvegarder les tâches complétées
def save_completed_tasks():
    with open("tasks_completed.txt", "w") as file:
        for task in tasks_completed:
            file.write(task + "\n")

# Fonction pour charger les tâches
def load_tasks():
    tasks = []
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
    return tasks

# Fonction pour charger les tâches complétées
def load_completed_tasks():
    tasks_completed = []
    with open("tasks_completed.txt", "r") as file:
        for line in file:
            tasks_completed.append(line.strip())
    return tasks_completed

# Fonction pour gérer le redimensionnement de la fenêtre
def on_resize(event):
    listbox.config(width=event.width // 10, height=event.height // 25)

# Création de la fenêtre principale
window = tk.Tk()
window.title("To-Do List")
window.geometry("800x600")

# Chargement des tâches et des tâches complétées
tasks = load_tasks()
tasks_completed = load_completed_tasks()
current_list = "active"
current_language = "fr"  # Langue par défaut est le français

# Création de la liste des tâches
listbox = tk.Listbox(window)
listbox.pack(fill=tk.BOTH, expand=True)

# Création de l'entrée pour ajouter une tâche
entry = tk.Entry(window)
entry.pack()
add_button = tk.Button(window, text="Ajouter", command=add_task)
add_button.pack()
remove_button = tk.Button(window, text="Supprimer", command=remove_task)
remove_button.pack()

# Création du menu principal
menu = tk.Menu(window)
window.config(menu=menu)

# Création du menu "Tâches"
tasks_menu = tk.Menu(menu)
menu.add_cascade(label="Tâches", menu=tasks_menu)
if current_language == "fr":
    tasks_menu.add_command(label="Tâches actives", command=switch_to_active_tasks)
    tasks_menu.add_command(label="Tâches complétées", command=switch_to_completed_tasks)
else:
    tasks_menu.add_command(label="Active Tasks", command=switch_to_active_tasks)
    tasks_menu.add_command(label="Completed Tasks", command=switch_to_completed_tasks)

# Création du menu "Langue"
language_menu = tk.Menu(menu)
menu.add_cascade(label="Langue", menu=language_menu)
language_menu.add_command(label="Français", command=set_french)
language_menu.add_command(label="English", command=set_english)

# Création du menu "Tâches complétées"
completed_tasks_menu = tk.Menu(menu)
completed_tasks_menu.add_command(label="Supprimer tâche", command=delete_completed_task)

# Initialisation des traductions du menu selon la langue actuelle
if current_language == "fr":
    set_french()
else:
    set_english()

# Configuration des raccourcis clavier
window.bind("<Configure>", on_resize)
window.bind("<Return>", add_task)

# Boucle principale
window.mainloop()
