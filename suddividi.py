import pandas as pd
df = pd.read_csv('the-reddit-climate-change-dataset-comments.csv')
dimensione_parte = 1000000
numero_parti = len(df) // dimensione_parte + 1
parti = [df[i * dimensione_parte:(i + 1) * dimensione_parte] for i in range(numero_parti)]
for i, parte in enumerate(parti):
    parte.to_csv(f'parte_{i+1}.csv', index=False)
