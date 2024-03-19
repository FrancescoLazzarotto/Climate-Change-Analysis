import csv
import pdb
from twarc.client2 import Twarc2
from twarc.expansions import ensure_flattened

# Funzione per recuperare il testo del tweet utilizzando Twarc
def get_tweet_text(tweet_id):
    # Inizializza Twarc con il tuo bearer token
    t = Twarc2(bearer_token="AAAAAAAAAAAAAAAAAAAAAInksQEAAAAASNA7s%2FXHNuvVKxXf7Fxl102Lv3E%3DmWuZSgrGxBKt1WcTnzV9zBiPpefl9cuevV6gqIwdZvZihG0TKN")

    # Utilizza Twarc per ottenere il testo del tweet
    try:
        tweet = t.tweet(tweet_id)
        if "data" in tweet:
            return tweet["data"]["text"]
        else:
            return None
    except Exception as e:
        print("Errore durante il recupero del tweet:", e)
        return None

# Percorso completo del file CSV
csv_file_path = "C:/Users/checc/Desktop/api/The Climate Change Twitter Dataset.csv"

# Leggi il file CSV e recupera il testo dei tweet per gli ID forniti
try:
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Salta l'intestazione se presente
        for _ in range(10):  # Recupera solo le prime 10 righe
            row = next(csv_reader)
            tweet_id = row[1]  # Supponiamo che l'ID del tweet sia nella seconda colonna
            tweet_text = get_tweet_text(tweet_id)
            if tweet_text:
                print("Testo del tweet:", tweet_text)
            else:
                print("Impossibile recuperare il testo del tweet.")
except Exception as e:
    print("Errore durante la lettura del file CSV:", e)
