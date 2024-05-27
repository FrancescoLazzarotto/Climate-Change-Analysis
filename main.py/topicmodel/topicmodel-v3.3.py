import os
import pandas as pd
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from bertopic import BERTopic
from bertopic.vectorizers import ClassTfidfTransformer
from umap import UMAP
from bertopic.representation import KeyBERTInspired
from bertopic.representation import MaximalMarginalRelevance

#carica il dataset
file_csv = os.path.join(os.path.expanduser('~'),'OneDrive', 'Desktop', 'corpus.csv')


try:
    df = pd.read_csv(file_csv, engine='python')
    print("Dataset trovato")
except FileNotFoundError:
    print(file_csv)
    print("File non trovato")
    exit()  

#verifica se la colonna 'testo_preprocessato' esiste nel DataFrame
if 'testo_preprocessato' not in df.columns:
    print("La colonna 'testo_preprocessato' non è presente nel DataFrame.")
    exit()

#addestramento del modello
docs = df['testo_preprocessato'].tolist() 
umap_model = UMAP(n_neighbors=15, n_components=5, min_dist=0.0, metric='cosine')
ctfidf_model = ClassTfidfTransformer()
representation_model = KeyBERTInspired().MaximalMarginalRelevance(diversity=0.3)
model = BERTopic(verbose=True, nr_topics="auto", ctfidf_model=ctfidf_model, umap_model=umap_model, representation_model=representation_model)
topics, probabilities = model.fit_transform(docs)

#salva il modello addestrato
model.save("topic_modeling") 

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

