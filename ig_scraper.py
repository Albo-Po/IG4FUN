import instaloader
import tkinter as tk
from tkinter import messagebox
from collections import defaultdict
import csv

# Funzione per raccogliere e analizzare i dati
def get_follower_data(username, password):
    try:
        # Crea un'istanza di Instaloader
        L = instaloader.Instaloader()

        # Login su Instagram
        L.login(username, password)

        # Ottieni il profilo
        profile = instaloader.Profile.from_username(L.context, username)

        # Dizionari per raccogliere i dati
        gender_data = {'Male': 0, 'Female': 0, 'Unknown': 0}
        age_data = {'18-34': 0, '35-44': 0, '45-54': 0, '55+': 0}
        personal_profiles = 0
        business_profiles = 0
        city_data = defaultdict(int)

        # Estrai i follower e analizzali
        for follower in profile.get_followers():
            # Verifica se il profilo è personale o business
            if follower.is_business_account:
                business_profiles += 1
            else:
                personal_profiles += 1

            # Analisi della città (se presente)
            locations = follower.get_location_names()
            if locations:
                for location in locations:
                    city_data[location] += 1

            # (Nota: In questo esempio, non abbiamo dati reali su genere ed età, 
            # li aggiungiamo per esempio come "Unknown" per ora)
            gender_data['Unknown'] += 1  # Placeholder per il genere
            age_data['18-34'] += 1  # Placeholder per fascia d'età

        # Crea un riepilogo
        summary = {
            "Gender": gender_data,
            "Age": age_data,
            "Personal Profiles": personal_profiles,
            "Business Profiles": business_profiles,
            "City Data": dict(city_data)
        }

        return summary

    except Exception as e:
        return f"Errore: {e}"

# Funzione di login e raccolta dati
def on_login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Errore", "Inserisci sia il nome utente che la password!")
        return

    # Ottieni i dati
    result = get_follower_data(username, password)

    # Mostra il risultato nella finestra di testo
    text_result.delete(1.0, tk.END)  # Pulisce il campo di testo
    if isinstance(result, str):  # Se è un errore
        text_result.insert(tk.END, result)
    else:
        # Mostra i dati di riepilogo
        text_result.insert(tk.END, f"Genere:\n{result['Gender']}\n")
        text_result.insert(tk.END, f"Età:\n{result['Age']}\n")
        text_result.insert(tk.END, f"Profili Personali: {result['Personal Profiles']}\n")
        text_result.insert(tk.END, f"Profili Business: {result['Business Profiles']}\n")
        text_result.insert(tk.END, f"Distribuzione per Città:\n{result['City Data']}\n")

# Crea la finestra principale
root = tk.Tk()
root.title("Instagram Follower Data Scraper")

# Aggiungi etichetta e campo di testo per il nome utente
label_username = tk.Label(root, text="Nome utente Instagram:")
label_username.pack(pady=5)
entry_username = tk.Entry(root, width=30)
entry_username.pack(pady=5)

# Aggiungi etichetta e campo di testo per la password
label_password = tk.Label(root, text="Password Instagram:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack(pady=5)

# Pulsante per fare il login
login_button = tk.Button(root, text="Login", command=on_login)
login_button.pack(pady=10)

# Aggiungi un campo di testo per mostrare il risultato
text_result = tk.Text(root, width=50, height=10)
text_result.pack(pady=10)

# Avvia la GUI
root.mainloop()
