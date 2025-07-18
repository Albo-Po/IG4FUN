import tkinter as tk
from tkinter import messagebox
import json
from instagram_api import get_user_id_from_profile, get_follower_data
from data_analysis import analyze_follower_data

# Funzione di login e raccolta dati tramite il token
def on_login():
    username = entry_username.get()
    token = entry_token.get()

    if not username or not token:
        messagebox.showerror("Errore", "Inserisci sia il nome utente che il token!")
        return

    # Ottieni l'ID utente dal profilo Instagram
    user_id = get_user_id_from_profile(username)
    if isinstance(user_id, str) and user_id.startswith("Errore"):
        messagebox.showerror("Errore", user_id)
        return
    
    # Ottieni i dati dal Graph API usando l'ID utente
    result = get_follower_data(token, user_id)

    if isinstance(result, str):
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result)
    else:
        # Mostra i dati di riepilogo
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, f"ID Utente: {result['id']}\n")
        text_result.insert(tk.END, f"Username: {result['username']}\n")
        text_result.insert(tk.END, f"Media Count: {result['media_count']}\n")
        text_result.insert(tk.END, f"Followers Count: {result['followers_count']}\n")
        text_result.insert(tk.END, f"Follows Count: {result['follows_count']}\n")

        # Esegui l'analisi dei dati
        stats = analyze_follower_data(result)
        text_result.insert(tk.END, f"Statistiche:\n{stats}\n")

# Crea la finestra principale
root = tk.Tk()
root.title("Instagram Follower Data Scraper")

# Aggiungi etichetta e campo di testo per il nome utente
label_username = tk.Label(root, text="Nome utente Instagram:")
label_username.pack(pady=5)
entry_username = tk.Entry(root, width=30)
entry_username.pack(pady=5)

# Aggiungi etichetta e campo di testo per il token di accesso
label_token = tk.Label(root, text="Token di Accesso Instagram:")
label_token.pack(pady=5)
entry_token = tk.Entry(root, width=30)
entry_token.pack(pady=5)

# Pulsante per fare il login
login_button = tk.Button(root, text="Ottieni Dati", command=on_login)
login_button.pack(pady=10)

# Aggiungi un campo di testo per mostrare il risultato
text_result = tk.Text(root, width=50, height=10)
text_result.pack(pady=10)

# Avvia la GUI
root.mainloop()
