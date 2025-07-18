import tkinter as tk
from tkinter import messagebox
import requests
import json

# Funzione per ottenere l'ID dell'utente da Instagram tramite l'URL del profilo
def get_user_id_from_profile(username):
    try:
        # URL del profilo Instagram pubblico (aggiungiamo ?__a=1 per ottenere il JSON)
        url = f'https://www.instagram.com/{username}/?__a=1'

        # Esegui la richiesta GET per ottenere i dati del profilo
        response = requests.get(url)
        
        if response.status_code == 200:
            # Analizza la risposta JSON per ottenere l'ID
            data = response.json()
            user_id = data['graphql']['user']['id']  # Estrai l'ID
            return user_id
        else:
            return f"Errore nella richiesta: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Errore: {e}"

# Funzione per raccogliere e analizzare i dati usando il token di accesso
def get_follower_data(token, user_id):
    try:
        # URL per ottenere i dati del profilo tramite Instagram Graph API
        url = f'https://graph.instagram.com/{user_id}?fields=id,username,media_count,followers_count,follows_count&access_token={token}'

        # Esegui la richiesta GET per ottenere i dati tramite Instagram Graph API
        response = requests.get(url)
        
        if response.status_code == 200:
            profile_data = response.json()
            # Dizionari per raccogliere i dati
            gender_data = {'Male': 0, 'Female': 0, 'Unknown': 0}
            age_data = {'18-34': 0, '35-44': 0, '45-54': 0, '55+': 0}
            personal_profiles = 0
            business_profiles = 0
            city_data = {}

            # Qui aggiungi una logica per raccogliere i dati relativi a genere, età e città.
            # Nota: l'Instagram Graph API non fornisce informazioni dettagliate su genere ed età direttamente,
            # quindi dovresti ottenere questi dati da un'altra fonte se sono necessari.
            # Puoi anche usare altre chiamate API per ottenere informazioni più specifiche.

            summary = {
                "Genere": gender_data,
                "Età": age_data,
                "Profili Personali": personal_profiles,
                "Profili Business": business_profiles,
                "Distribuzione per Città": city_data,
                "Dati Profilo": profile_data
            }

            return summary
        else:
            return f"Errore nella richiesta: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Errore: {e}"

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

    # Mostra il risultato nella finestra di testo
    text_result.delete(1.0, tk.END)  # Pulisce il campo di testo
    if isinstance(result, str):  # Se è un errore
        text_result.insert(tk.END, result)
    else:
        # Mostra i dati di riepilogo
        text_result.insert(tk.END, f"Genere:\n{result['Genere']}\n")
        text_result.insert(tk.END, f"Età:\n{result['Età']}\n")
        text_result.insert(tk.END, f"Profili Personali: {result['Profili Personali']}\n")
        text_result.insert(tk.END, f"Profili Business: {result['Profili Business']}\n")
        text_result.insert(tk.END, f"Distribuzione per Città:\n{result['Distribuzione per Città']}\n")
        text_result.insert(tk.END, f"Dati Profilo:\n{json.dumps(result['Dati Profilo'], indent=2)}\n")

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
