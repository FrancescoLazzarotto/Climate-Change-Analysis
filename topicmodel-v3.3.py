import os
import pandas as pd
import matplotlib.pyplot as plt
from bertopic import BERTopic

#carica il dataset
file_csv = os.path.join(os.path.expanduser('~'),'OneDrive', 'Desktop', 'reddit-parte-4-v1.2.csv')
file_csv2 = os.path.join(os.path.expanduser('~'),'OneDrive', 'Desktop', 'twitterv1.5_preprocessato.csv')

try:
    df1 = pd.read_csv(file_csv, engine='python')
    df2 = pd.read_csv(file_csv2, engine='python')
    print("Dataset trovato")
except FileNotFoundError:
    print(file_csv)
    print("File non trovato")
    exit()  

#unisco i due dataset
df = pd.concat([df1, df2], ignore_index=True)

#verifica se la colonna 'testo_preprocessato' esiste nel DataFrame
if 'testo_preprocessato' not in df.columns:
    print("La colonna 'testo_preprocessato' non è presente nel DataFrame.")
    exit()

#addestramento del modello
docs = df['testo_preprocessato'].tolist() 
model = BERTopic(verbose=True, nr_topics="auto")
topics, probabilities = model.fit_transform(docs)

#salva il modello addestrato
model.save("modello_twitter_provav1.6") 

#file di output per le keyword
output_file = os.path.join(os.path.expanduser('~'),'onedrive', 'Desktop', 'output', 'resultsv1.6.txt')

with open(output_file, "w") as f:
    f.write("Topic Analysis Results:\n\n")
    for topic_id, keywords in model.get_topics().items():
        f.write(f"Topic {topic_id}:\n")
        for keyword, importance in keywords[:10]:
            f.write(f"- {keyword}: {importance}\n")
        f.write("\n")

#funzioni per grafici e chiamate di funzioni
def plot_topic_distribution(topics):
    topic_counts = pd.Series(topics).value_counts().sort_index()
    plt.bar(topic_counts.index, topic_counts.values)
    plt.axis
    plt.xlabel('Topic')
    plt.ylabel('Number of Document')
    plt.title('Topic Distribution')
    plt.savefig("topic_distribution.png")  
    plt.close()

def plot_topic_keywords(model):
    for topic_id, keywords in model.get_topics().items():
        keyword_list = [keyword[0] for keyword in keywords[:10]]  
        importance_list = [importance[1] for importance in keywords[:10]] 
        plt.barh(range(len(keyword_list)), importance_list[::-1])
        plt.xlabel('Keyword Importance')
        plt.yticks(range(len(keyword_list)), keyword_list[::-1])
        plt.title(f'Topic {topic_id}') 
        plt.savefig(f"topic_{topic_id}_keywords.png")  
        plt.close()


plot_topic_distribution(topics)
plot_topic_keywords(model)


