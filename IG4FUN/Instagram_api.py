import requests

# Funzione per ottenere l'ID dell'utente da Instagram tramite l'URL del profilo
def get_user_id_from_profile(username):
    try:
        url = f'https://www.instagram.com/{username}/?__a=1'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            user_id = data['graphql']['user']['id']  # Estrai l'ID
            return user_id
        else:
            return f"Errore nella richiesta: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Errore: {e}"

# Funzione per raccogliere i dati tramite il token di accesso
def get_follower_data(token, user_id):
    try:
        url = f'https://graph.instagram.com/{user_id}?fields=id,username,media_count,followers_count,follows_count&access_token={token}'
        response = requests.get(url)

        if response.status_code == 200:
            profile_data = response.json()
            return profile_data
        else:
            return f"Errore nella richiesta: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Errore: {e}"
