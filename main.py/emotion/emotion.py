import pandas as pd
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud

emo_lexicon_file = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'NRC-Emotion-Lexicon-Wordlevel-v0.92.txt')
emo_lexicon = {}
with open(emo_lexicon_file, 'r', encoding='utf-8') as file:
    for line in file:
        word, emotion, value = line.strip().split('\t')
        if int(value) == 1:
            if word not in emo_lexicon:
                emo_lexicon[word] = []
            emo_lexicon[word].append(emotion)


file_csv = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'twitterv1.5_preprocessato.csv')
file_csv2 = os.path.join(os.path.expanduser('~'),'OneDrive', 'Desktop', 'reddit-parte-4-v1.2.csv')

df1 = pd.read_csv(file_csv, engine='python', encoding='utf-8')
df2 = pd.read_csv(file_csv2, engine='python', encoding='utf-8')
df= pd.concat([df1, df2], ignore_index=True)


text_list_list = df['testo_preprocessato'].apply(eval).tolist()


emotion_counts_total = {emotion: 0 for emotions in emo_lexicon.values() for emotion in emotions}


for text_list in text_list_list:
    for token in text_list:
        if token in emo_lexicon:
            for emotion in emo_lexicon[token]:
                emotion_counts_total[emotion] += 1


print(emotion_counts_total)

del emotion_counts_total['positive']
del emotion_counts_total['negative']

labels = list(emotion_counts_total.keys())
sizes = list(emotion_counts_total.values())

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Distribuzione delle emozioni')
plt.show()



wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(emotion_counts_total)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud delle Emozioni')
plt.show()

plt.figure(figsize=(10, 6))
plt.barh(labels, sizes)
plt.xlabel('Conteggio testi')
plt.ylabel('Emozioni')
plt.title('Conteggio delle emozioni')
plt.show()
