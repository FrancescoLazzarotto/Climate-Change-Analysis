import csv
import pdb
from twarc.client2 import Twarc2
from twarc.expansions import ensure_flattened


def get_tweet_text(tweet_id):
    #put your brearer token from your twitter developer account
    t = Twarc2(bearer_token="")

    #using twarc to get the text 
    try:
        tweet = t.tweet(tweet_id)
        if "data" in tweet:
            return tweet["data"]["text"]
        else:
            return None
    except Exception as e:
        print("Errore durante il recupero del tweet:", e)
        return None

#path of the dataset
csv_file_path = "C:/Users/checc/Desktop/api/The Climate Change Twitter Dataset.csv"

#read the csv file and extract the text from the ids
try:
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) 
        for _ in range(10): 
            row = next(csv_reader)
            tweet_id = row[1] #put the column where the ids of the tweets are
            tweet_text = get_tweet_text(tweet_id)
            if tweet_text:
                print("Testo del tweet:", tweet_text)
            else:
                print("Impossibile recuperare il testo del tweet.")
except Exception as e:
    print("Errore durante la lettura del file CSV:", e)
