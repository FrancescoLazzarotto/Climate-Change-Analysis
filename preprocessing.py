
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import string
import numpy as np
import pandas as pd 
import os



#accesso al csv 
file_csv = os.path.join(os.path.expanduser('~'),'OneDrive', 'Desktop', 'parte_1.csv')



try:
    dataframe = pd.read_csv(file_csv)
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


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
stopwords = nltk.corpus.stopwords.words('english')

#passaggi di preprocessing


#pulizia e anonimizzazione 

#rimozione menzioni (@user) e hashtag ( #tag )
def rimozione_menzioni_hashtag(testo):
    
    tokens = nltk.word_tokenize(testo)
    tokens_filtrati = []
    
    for parola in tokens:
        if not re.match(r'^[@#]\w+', parola):
            tokens_filtrati.append(parola)
            
    testo_pulito = ' '.join(tokens_filtrati)
    return testo_pulito

#rimozione testi duplicati
def rimuovi_duplicati(testi):
    
    testi_unici = set()
    testi_senza_duplicati = []
    
    for testo in testi:
        if testo not in testi_unici:
            testi_unici.add(testo)
            testi_senza_duplicati.append(testo)
    return testi_senza_duplicati


#segmentazione del testo

#suddivisione in frasi tramite la funzione nltk
def segmentazione(testo):
    frasi = nltk.sent_tokenize(testo)
    return frasi

#tokenizzazione
def tokenizzazione(testo):
    frasi_segmentate = testo
    testo_tokenizzato = []
    for frase in frasi_segmentate:
        token_frase = word_tokenize(frase)
        testo_tokenizzato.extend(token_frase)

    return testo_tokenizzato
 
#pos tagging
def pos_tagging(testo):
    parole_tokenizzate = testo
    pos_tagged = nltk.pos_tag(parole_tokenizzate)
    
    return pos_tagged

#lower casing
#lower casing
def lower(testo):
    testo_lower = [parola.lower() for parola in testo]
    return testo_lower


#rimozioni stopwords e punteggiatura

#rimozione punteggiatura
def rimuovi_punteggiatura(testo):
    testo_senza_punteggiatura = ""
    
    for carattere in testo:
        if carattere not in string.punctuation:  
            testo_senza_punteggiatura += carattere
            
    return testo_senza_punteggiatura
    
#rimozione stop words
def rimozione_stopword(testo, stopword):
    parole_filtrate = [parola for parola in testo if parola.lower() not in stopword]
    testo_senza_stopword = ' '.join(parole_filtrate)
    
    return testo_senza_stopword

#lemmatizzazione/stemming 
def lemmatizza_testo(testo):
    lemmatizzatore = WordNetLemmatizer()
    parole_lemmatizzate = [lemmatizzatore.lemmatize(parola) for parola in testo]
    testo_lemmatizzato = ' '.join(parole_lemmatizzate)
    
    return testo_lemmatizzato

#vettorizzazione ?

testi_preprocessati = []

for testo in testi:
    testo = rimozione_menzioni_hashtag(testo)
    testo = rimuovi_duplicati([testo])[0]
    frasi = segmentazione(testo)
    testo = tokenizzazione(frasi)
    testo = pos_tagging(testo)
    testo = lower(testo)
    testo = rimuovi_punteggiatura(testo)
    testo = rimozione_stopword(testo, stopwords)
    testo = lemmatizza_testo(testo)
    testi_preprocessati.append(testo)

dataframe_preprocessato = pd.DataFrame({"Testo Preprocessato": testi_preprocessati})
file_csv_preprocessato = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'parte_1_preprocessato.csv')
dataframe_preprocessato.to_csv(file_csv_preprocessato, index=False)

