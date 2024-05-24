
import os
from collections import defaultdict


emo_lexicon_file = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'NRC-Emotion-Lexicon-Wordlevel-v0.92.txt')
emo_lexicon = {}
with open(emo_lexicon_file, 'r', encoding='utf-8') as file:
    for line in file:
        word, emotion, value = line.strip().split('\t')
        if int(value) == 1:
            if word not in emo_lexicon:
                emo_lexicon[word] = []
            emo_lexicon[word].append(emotion)


def associate_emotions_to_topic(topic_keywords):
    emotion_counts = defaultdict(int)
    for keyword, _ in topic_keywords:
        if keyword in emo_lexicon:
            for emotion in emo_lexicon[keyword]:
                emotion_counts[emotion] += 1
    return emotion_counts


topics = {
"Topic name":[('keyword', 'cTf-idfScore')...]

}

topic_emotions = {}
for topic_name, topic_keywords in topics.items():
    emotion_counts = associate_emotions_to_topic(topic_keywords)
    topic_emotions[topic_name] = emotion_counts


for topic, emotions in topic_emotions.items():
    print(f"Emozioni associate al topic '{topic}':")
    for emotion, count in emotions.items():
        print(f"{emotion}: {count}")
    print()
