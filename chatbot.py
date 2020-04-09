# %% [code] {"_kg_hide-input":false}
import pandas as pd

# Matplot
import matplotlib.pyplot as plt
%matplotlib inline

# Scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer

# Keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout, Embedding, Flatten, Conv1D, MaxPooling1D, LSTM
from keras import utils
from keras.callbacks import ReduceLROnPlateau, EarlyStopping

# nltk
import nltk
from nltk.corpus import stopwords
from  nltk.stem import SnowballStemmer

# Word2vec
import gensim
from gensim.models import KeyedVectors
from gensim.models import Word2Vec

# Utility
import re
import numpy as np
import os
from collections import Counter
import logging
import time
import pickle


# As of Gensim 3.7.3 it's using some deprecated function and we don't care about it
import warnings
warnings.filterwarnings("ignore")

# %% [code]
DATASET_COLUMNS = ["target", "ids", "date", "flag", "user", "text"]
DATASET_ENCODING = "ISO-8859-1"
TRAIN_SIZE = 0.8

# TEXT CLENAING
TEXT_CLEANING_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

# WORD2VEC 
W2V_SIZE = 300
W2V_WINDOW = 7
W2V_EPOCH = 32
W2V_MIN_COUNT = 10

# KERAS
SEQUENCE_LENGTH = 300
EPOCHS = 8
BATCH_SIZE = 1024

# SENTIMENT
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
NEUTRAL = "NEUTRAL"
SENTIMENT_THRESHOLDS = (0.4, 0.7)

# %% [code] {"_kg_hide-input":false}
model = KeyedVectors.load("/kaggle/input/gensim-embeddings-dataset/glove.twitter.27B.200d.gensim")

# %% [code]
def most_similar_list(s, l):
    temp= []
    for i in l:
        x = (i, model.n_similarity(s.split(), i.split()))
        print(x)
        temp.append(x)
    temp = sorted(temp, key = lambda x: x[1], reverse = True)  
    return temp
l = ["delete", "unsubscribe", "subscribe", " poll", "schedule", "post", "leave"]

# %% [code]
#Pre Condition: Given 4 inputs: New Text, Set of Users, 
#Set of Channels and queue of previous texts and predictions
# 1) Sentiment Analysis
# 2) User and Channel Look Up
# 3) POS Tagging
# 4) USer, Channel, and Verb findinf
# 5) Action determination using weights
# Post Condition: Returns a dicitonary with original text, recommended action list, recommended action
# sentiment value,set of found users and set of found channels
class FixedQueue():
    def __init__(self,s):
        self.queue = []
        self.capacity = s
    def push(self, x):
        if(len(sel.queue) < 5):
            self.queue.append(x)
        else:
            self.queue.pop(0)
            self.queue.append(x)
    def get(self,ind):
        return self.queue[-1*ind - 1]
    def size(self):
        return len(self.queue)
class NLPPipeline():
    def __init__(self,user, channel):
        self.past_texts = FixedQueue(3)
        self.users = user
        self.channels = channel
        with open("/kaggle/input/sentimentanalysis/tokenizer.pkl", 'rb') as f:
            self.tokenizer = pickle.load(f)
            self.model = load_model("/kaggle/input/sentimentanalysis/model.h5")
        
    def process_text(self, text):
        previous_sentiment_value = self.__processPrevSentiment() # type: int context: value representing weighted average of previous sentiment values
        currentSentiment = self.__sentimentAnalysis(text) # type: int context: value representing this text's sentiment
        uc_look_up = self.__userChannelLookUp(text) # type: dictionary with keys = {user, channel} and values = {list(users), list(channels)}
        POS_dict = self.__POSTagging(text)
        found_user_dict = self.__findUsers(uc_look_up, POS_dict, text)
        found_channel_dict = self.__findChannels(uc_look_up, POS_dict, text)
        verbRecommendations = self.__verbFinding(POS_dict, text)
        actionDetermination = self.__determineAction()
        print(POS_dict)
        return ("Current Sentiment: {}, Previous Sentiment Average: {}".format(currentSentiment, previous_sentiment_value), POS_dict)
        
    def __processPrevSentiment(self):
        try:
            if(self.past_texts.size() == 0):
                return 0
        except:
            return 0
        weight_counter = 0
        for_counter = 0
        this_weight =1
        rate = 0.66
        threshold = 0.025
        sentCounter = 0
        while(for_counter < self.past_texts.size() and this_weight > threshold):
            sentCounter += self.past_texts.get(for_counter)["Sentiment"]*this_weight
            weight_counter += this_weight
            this_weight *= rate
            for_counter += 1
        return sentCounter/weight_counter
    
    def __decode_sentiment(self,score, include_neutral=True):
        if include_neutral:        
            label = NEUTRAL
            if score <= SENTIMENT_THRESHOLDS[0]:
                label = NEGATIVE
            elif score >= SENTIMENT_THRESHOLDS[1]:
                label = POSITIVE

            return label
        else:
            return NEGATIVE if score < 0.5 else POSITIVE
    def __sentimentAnalysis(self,text):
        start_at = time.time()
        # Tokenize text
        x_test = pad_sequences(self.tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
        # Predict
        score = self.model.predict([x_test])[0]
        # Decode sentiment
        label = self.__decode_sentiment(score, include_neutral=True)

        return {"label": label, "score": float(score),
           "elapsed_time": time.time()-start_at}
    def __userChannelLookUp(self, text):
        return ""
    def __POSTagging(self,text):
        text = nltk.word_tokenize(text)
        text = nltk.pos_tag(text)
        chunker = nltk.RegexpParser('''
                            KEYWORDS: {<DT>? <JJ>* <NN.*>+}
                            P: {<IN>}
                            V: {<V.*>}
                            PHRASES: {<P> <KEYWORDS>}
                            ACTIONS: {<V> <KEYWORDS|PHRASES>*}
                            ''') 
        chunked = chunker.parse(text) 
        return chunked
    def __findUsers(self,uc_look_up, POS_dict, text):
        
        return ""
    def __findChannels(self,uc_look_up, POS_dict, text):
        return ""
    def __verbFinding(self,POS_dict, text):
        return ""
    def __determineAction(self):
        return ""

# %% [code]
nlp = NLPPipeline(1,2)
x, d = nlp.process_text("hello, my name is anant. this is a trial phrase. before the cat jumped over the dog, he ran across the lawn")
print(x)
print("POS and Chunking":d)
            
            

# %% [code]
