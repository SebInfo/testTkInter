import tkinter as tk


# Fonction pour ajouter les chiffres et opérateurs à l'affichage
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry_field.get()))
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, result)
        except Exception as e:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "Erreur")
    elif text == "C":
        entry_field.delete(0, tk.END)
    else:
        entry_field.insert(tk.END, text)


# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice")
root.geometry("450x500")
root.resizable(0, 0)  # Fenêtre non redimensionnable

# Champs d'entrée pour l'affichage des calculs
entry_field = tk.Entry(root, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, relief="ridge",
                       justify='right')
entry_field.grid(row=0, column=0, columnspan=4, pady=10)

# Liste des boutons de la calculatrice
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Création et disposition des boutons
row_val = 1
col_val = 0
for button in buttons:
    button_widget = tk.Button(root, text=button, font=("Arial", 18), padx=20, pady=20, borderwidth=4, relief="ridge")
    button_widget.grid(row=row_val, column=col_val, padx=10, pady=10)
    button_widget.bind("<Button-1>", click)  # Associer un événement à chaque bouton

    col_val += 1
    if col_val == 4:
        col_val = 0
        row_val += 1

# Lancement de la boucle principale
root.mainloop()
