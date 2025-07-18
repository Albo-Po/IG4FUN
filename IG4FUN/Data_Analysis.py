import pandas as pd
import matplotlib.pyplot as plt

# Funzione per analizzare i dati dei follower (esempio di analisi statistica)
def analyze_follower_data(follower_data):
    # Creiamo un DataFrame con i dati per esempio (modifica questa parte secondo i tuoi dati)
    data = {
        'Followers': [follower_data['followers_count']],
        'Following': [follower_data['follows_count']],
        'Media Count': [follower_data['media_count']],
    }
    df = pd.DataFrame(data)

    # Statistiche descrittive
    stats = df.describe()

    # Visualizzazione dei dati
    df.plot(kind='bar')
    plt.title("Analisi Follower Instagram")
    plt.show()

    return stats
