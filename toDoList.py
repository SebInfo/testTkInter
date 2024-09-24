import tkinter as tk
from tkinter import messagebox

# Fonction pour ajouter une tâche à la liste
def ajouter_tache():
    tache = entree_tache.get()
    if tache != "":
        liste_taches.insert(tk.END, tache)
        entree_tache.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrée vide", "Veuillez entrer une tâche.")

# Fonction pour supprimer la tâche sélectionnée
def supprimer_tache():
    try:
        selection = liste_taches.curselection()
        liste_taches.delete(selection)
    except:
        messagebox.showwarning("Erreur", "Veuillez sélectionner une tâche à supprimer.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("To-do list")
root.geometry("400x400")

# Champ d'entrée pour la nouvelle tâche
label_nouvelle_tache = tk.Label(root, text="Nouvelle tâche:")
label_nouvelle_tache.pack(pady=10)

entree_tache = tk.Entry(root, width=40)
entree_tache.pack(pady=10)

# Bouton pour ajouter la tâche
bouton_ajouter = tk.Button(root, text="Ajouter", width=15, command=ajouter_tache)
bouton_ajouter.pack(pady=5)

# Liste des tâches
label_liste_taches = tk.Label(root, text="Liste des tâches:")
label_liste_taches.pack(pady=10)

liste_taches = tk.Listbox(root, height=10, width=40, selectmode=tk.SINGLE)
liste_taches.pack(pady=10)

# Bouton pour supprimer la tâche sélectionnée
bouton_supprimer = tk.Button(root, text="Supprimer", width=15, command=supprimer_tache)
bouton_supprimer.pack(pady=5)

# Lancement de la boucle principale
root.mainloop()
