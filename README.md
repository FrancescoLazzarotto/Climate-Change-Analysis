# Climate-Change-Analysis

Research Project: ClimateChangeSentiments

Introduction:
This repository hosts the code and documentation for my ongoing research project focused on sentiment analysis and text-mining within the context of climate change discourse. The project integrates innovative approaches to analyze opinions expressed on social media platforms, particularly Twitter, regarding the topic of climate change.

Objective:
The primary objective is to develop an advanced text-mining model capable of extracting valuable insights from large-scale datasets of climate change-related tweets. By leveraging natural language processing (NLP) techniques and sentiment analysis, the project aims to understand public sentiments, identify key themes, and contribute to a comprehensive understanding of the ongoing discourse surrounding climate change.

Key Features:

Text-Mining Pipeline: The project implements a robust text-mining pipeline that includes data collection, preprocessing, sentiment analysis, and visualization components.

Sentiment Analysis: Utilizing state-of-the-art sentiment analysis techniques, the model categorizes tweets into positive, negative, or neutral sentiments, providing a nuanced perspective on public opinions.

Data Integration: The project integrates diverse datasets, combining social media data with authoritative climate change statistics. This holistic approach enables a more comprehensive analysis of the relationship between public sentiment and actual climate change data. -- 


Files: 

-Preprocessing.py is the script I am using to preprocess data (NLTK).

-preprocessingspacy.py is the script I am using to preprocess data (SpaCy).

-suddividi.py is the script I used to separate the reddit dataset in 5 different dataset to split the work on my machine.

-twarc.py is the script (https://twarc-project.readthedocs.io/en/latest/twarc2_en_us/) I am trying to use to re-hydrate some tweerìts from this dataset 
(https://www.kaggle.com/datasets/deffro/the-climate-change-twitter-dataset) ... I guess it isn't working anymore after the changing at the twitter API.

Currently, preprocessing is being performed on two different datasets (https://www.kaggle.com/datasets/pavellexyr/the-reddit-climate-change-dataset) (https://www.kaggle.com/datasets/edqian/twitter-climate-change-sentiment-dataset) using the NLTK and SpaCy libraries in Python.
The next step will probably be some topic anlysis using BerTOPIC (https://huggingface.co/MaartenGr/BERTopic_ArXiv/tree/main)

Contact:
email: francesco.lazzarotto@edu.unito.it

