import spacy
import pandas as pd 
import os
import time
start_time = time.time()
nlp = spacy.load("en_core_web_sm")

# Rimozione menzioni (@user) e hashtag ( #tag )
def rimozione_menzioni_hashtag(testo):
    doc = nlp(testo)
    testo_pulito = ' '.join(token.text for token in doc if not token.text.startswith('@') and not token.text.startswith('#'))
    return testo_pulito

# Rimozione testi duplicati
def rimuovi_duplicati(testi):
    testi_senza_duplicati = list(set(testi))
    return testi_senza_duplicati

# Segmentazione del testo
def segmentazione(testo):
    doc = nlp(testo)
    frasi = [sent.text for sent in doc.sents]
    return frasi

# Lowercasing
def lower(testo):
    return testo.lower()

# Rimozione punteggiatura
def rimuovi_punteggiatura(testo):
    doc = nlp(testo)
    testo_senza_punteggiatura = ' '.join(token.text for token in doc if not token.is_punct)
    return testo_senza_punteggiatura

# Rimozione stop words
def rimozione_stopword(testo):
    doc = nlp(testo)
    testo_senza_stopword = ' '.join(token.text for token in doc if not token.is_stop)
    return testo_senza_stopword

# Lemmatizzazione
def lemmatizza_testo(testo):
    doc = nlp(testo)
    testo_lemmatizzato = ' '.join(token.lemma_ for token in doc)
    return testo_lemmatizzato

# Caricamento del dataset
file_csv = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'parte_5.csv')

try:
    dataframe = pd.read_csv(file_csv)
    print("Dataset trovato")
except FileNotFoundError:
    print(file_csv)
    print("File non trovato")
    exit()  
try:
    colonna_testo = 'body'
    testi = dataframe[colonna_testo].tolist()
    print("Colonna raggiunta")
except KeyError:
    print("Colonna non trovata")
    exit()

testi_preprocessati = []

for i, testo in enumerate(testi[:100]):
    testo = rimozione_menzioni_hashtag(testo)
    testo = rimuovi_duplicati([testo])[0]
    frasi = segmentazione(testo)
    testo = lower(testo)
    testo = rimuovi_punteggiatura(testo)
    testo = rimozione_stopword(testo)
    testo = lemmatizza_testo(testo)
    testi_preprocessati.append(testo)
    
    print(f"Dato elaborato: {i+1}/{len(testi[:100])}")

dataframe_preprocessato = pd.DataFrame({"Testo Preprocessato": testi_preprocessati})
file_csv_preprocessato = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'parte9_preprocessato.csv')
dataframe_preprocessato.to_csv(file_csv_preprocessato, index=False)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tempo totale di esecuzione: {elapsed_time} secondi")
