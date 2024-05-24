from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import os
import pandas as pd
from tqdm import tqdm


file_csv = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'twitterv1.5_preprocessato.csv')
df = pd.read_csv(file_csv, engine='python')



grouped_texts = df.groupby('sentiment')['testo_preprocessato'].apply(lambda x: ' '.join(x))


vectorizer = CountVectorizer()


word_counts = vectorizer.fit_transform(grouped_texts)


words_per_sentiment = {}
for sentiment, text in tqdm(grouped_texts.items(), desc="Estrazione delle parole per ogni sentimento"):

    words_count = word_counts[grouped_texts.index.get_loc(sentiment), :].toarray().flatten()

    words_freq = [(word, count) for word, count in zip(vectorizer.get_feature_names_out(), words_count)]

    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)[:20]

    words_per_sentiment[sentiment] = words_freq


plt.figure(figsize=(12, 8))


num_plots = min(len(words_per_sentiment), 4)


colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
alpha_base = 0.45
alpha_step = 0.55


for i, (sentiment, words_freq) in enumerate(words_per_sentiment.items(), 1):

    words, counts = zip(*words_freq)


    plt.subplot(2, 2, i) if num_plots > 1 else plt.subplot(1, 1, i)

    for j, (word, count) in enumerate(zip(words, counts)):

        alpha = alpha_base + alpha_step * (j / len(words))


        plt.barh(word, count, color=colors[i-1], alpha=alpha)


    plt.title(f'Parole più comuni per il sentiment "{sentiment}"')
    plt.xlabel('Conteggio delle parole')
    plt.ylabel('Parola')
    plt.gca().invert_yaxis()

plt.tight_layout()

plt.show()
