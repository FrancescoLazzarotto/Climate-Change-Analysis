import pandas as pd
import matplotlib.pyplot as plt
import os
file_csv = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'twitterv1.5_preprocessato.csv')

df = pd.read_csv(file_csv, engine='python')


label_mapping = {-1: 'Negativo', 0: 'Neutro', 1: 'Positivo', 2: 'Altro'}


df['sentiment'] = df['sentiment'].map(label_mapping)


sentiment_counts = df['sentiment'].value_counts(normalize=True) * 100



colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']


plt.figure(figsize=(8, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Distribuzione Sentiment', fontsize=16, fontweight='bold', pad=20)  # Titolo con formattazione
plt.axis('equal')
plt.show()
