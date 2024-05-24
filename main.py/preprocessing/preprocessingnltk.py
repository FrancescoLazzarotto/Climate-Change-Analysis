import re
import nltk
import pandas as pd
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import time 

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

start_time = time.time()
def preprocess_text(text):
    
    text = re.sub(r'@\w+', '', text)  
    text = re.sub(r'#\w+', '', text)  
    text = re.sub(r'http\S+', '', text)  
    text = re.sub(r'[^a-zA-Z\s]', '', text) 
    text = re.sub(r'\b\w{1,2}\b', '', text)  
    
    
    tokens = word_tokenize(text) 
    stop_words = set(stopwords.words('english')) 
    tokens_filtered = [word for word in tokens if word.lower() not in stop_words]  
    lemmatizer = WordNetLemmatizer() 
    tokens_lemmatized = [lemmatizer.lemmatize(word) for word in tokens_filtered]
    
    return tokens_lemmatized

file_csv = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'parte_3.csv')

try:
    dataframe = pd.read_csv(file_csv, nrows=100000)
    print("Dataset trovato")
except FileNotFoundError:
    print("File non trovato")
    exit()
try:
    colonna_testo = dataframe['dati'].tolist()
    print("Colonna raggiunta")
except KeyError:
    print("Colonna non trovata")
    exit()

preprocessed_texts = []
for index, row in dataframe.iterrows():
    preprocessed_text = preprocess_text(row[colonna_testo])
    preprocessed_texts.append(preprocessed_text)
    print(f"Riga {index + 1} processata")

dataframe['testo_preprocessato'] = preprocessed_texts
output_csv = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'reddit-parte-4-v1.2.csv')
dataframe.to_csv(output_csv, index=False)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tempo totale di esecuzione: {elapsed_time} secondi")