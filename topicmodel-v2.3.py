import os
from bertopic import BERTopic
import pandas as pd
import matplotlib.pyplot as plt
import io

# carico il dataset
file_csv = os.path.join(os.path.expanduser('~'),'OneDrive', 'Desktop', '')

try:
    df = pd.read_csv(file_csv, engine='python')
    print("Dataset trovato")
except FileNotFoundError:
    print(file_csv)
    print("File non trovato")
    exit()  

# addestramento modello
docs = df[0:10000].text.to_list()
model = BERTopic(verbose=True)
topics, probabilities = model.fit_transform(docs)

model.save("modello1prova") 

# file di output per le keyword scritte
output_file = os.path.join(os.path.expanduser('~'),'onedrive', 'Desktop', 'output', 'resultsv1.2.txt')

with open(output_file, "w") as f:
    f.write("Topic Analysis Results:\n\n")
    for topic_id, keywords in model.get_topics().items():
        f.write(f"Topic {topic_id}:\n")
        for keyword, importance in keywords[:10]:
            f.write(f"- {keyword}: {importance}\n")
        f.write("\n")

# visualizzazione dei risultati
def plot_topic_distribution(topics):
    topic_counts = pd.Series(topics).value_counts().sort_index()
    plt.bar(topic_counts.index, topic_counts.values)
    plt.xlabel('Topic')
    plt.ylabel('Number of Documents')
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


# chiamate delle funzioni
plot_topic_distribution(topics)
plot_topic_keywords(model)

# chiamate funzioni bertopic di visualizzazione
model.visualize_barchart()
model.visualize_topics()
model.visualize_heatmap()
