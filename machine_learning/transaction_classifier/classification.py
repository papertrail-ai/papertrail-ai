from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from math import log, sqrt
import pandas as pd
import numpy as np
import re



class GLClassifier(object):
    def __init__(self, trainData, method = 'tf-idf'):
        self.transactions, self.labels = trainData['account'], trainData['label']
        self.method = method

    def train(self):
        self.calc_TF_and_IDF()
        if self.method == 'tf-idf':
            self.calc_TF_IDF()
        else:
            self.calc_prob()

    def calc_prob(self):
        self.prob_negative = dict()
        self.prob_positive = dict()
        for word in self.tf_negative:
            self.prob_negative[word] = (self.tf_negative[word] + 1) / (self.negative_words + \
                                                                len(list(self.tf_negative.keys())))
        for word in self.tf_positive:
            self.prob_positive[word] = (self.tf_positive[word] + 1) / (self.positive_words + \
                                                                len(list(self.tf_positive.keys())))
        self.prob_negative_mail, self.prob_positive_mail = self.negative_transactions / self.total_transactions, self.positive_transactions / self.total_transactions 


    def calc_TF_and_IDF(self):
        noOfaccounts = self.transactions.shape[0]
        self.negative_transactions, self.positive_transactions = self.labels.value_counts()[1], self.labels.value_counts()[0]
        self.total_transactions = self.negative_transactions + self.positive_transactions
        self.negative_words = 0
        self.positive_words = 0
        self.tf_negative = dict()
        self.tf_positive = dict()
        self.idf_negative = dict()
        self.idf_positive = dict()
        for i in range(noOfaccounts):
            account_processed = process_account(self.transactions[i])
            count = list() #To keep track of whether the word has ocured in the account or not.
                           #For IDF
            for word in account_processed:
                if self.labels[i]:
                    self.tf_negative[word] = self.tf_negative.get(word, 0) + 1
                    self.negative_words += 1
                else:
                    self.tf_positive[word] = self.tf_positive.get(word, 0) + 1
                    self.positive_words += 1
                if word not in count:
                    count += [word]
            for word in count:
                if self.labels[i]:
                    self.idf_negative[word] = self.idf_negative.get(word, 0) + 1
                else:
                    self.idf_positive[word] = self.idf_positive.get(word, 0) + 1

    def calc_TF_IDF(self):
        self.prob_negative = dict()
        self.prob_positive = dict()
        self.sum_tf_idf_negative = 0
        self.sum_tf_idf_positive = 0
        for word in self.tf_negative:
            self.prob_negative[word] = (self.tf_negative[word]) * log((self.negative_transactions + self.positive_transactions) \
                                                          / (self.idf_negative[word] + self.idf_positive.get(word, 0)))
            self.sum_tf_idf_negative += self.prob_negative[word]
        for word in self.tf_negative:
            self.prob_negative[word] = (self.prob_negative[word] + 1) / (self.sum_tf_idf_negative + len(list(self.prob_negative.keys())))
            
        for word in self.tf_positive:
            self.prob_positive[word] = (self.tf_positive[word]) * log((self.negative_transactions + self.positive_transactions) \
                                                          / (self.idf_negative.get(word, 0) + self.idf_positive[word]))
            self.sum_tf_idf_positive += self.prob_positive[word]
        for word in self.tf_positive:
            self.prob_positive[word] = (self.prob_positive[word] + 1) / (self.sum_tf_idf_positive + len(list(self.prob_positive.keys())))
            
    
        self.prob_negative_mail, self.prob_positive_mail = self.negative_transactions / self.total_transactions, self.positive_transactions / self.total_transactions 
                    
    def classify(self, processed_account):
        pnegative, ppositive = 0, 0
        for word in processed_account:                
            if word in self.prob_negative:
                pnegative += log(self.prob_negative[word])
            else:
                if self.method == 'tf-idf':
                    pnegative -= log(self.sum_tf_idf_negative + len(list(self.prob_negative.keys())))
                else:
                    pnegative -= log(self.negative_words + len(list(self.prob_negative.keys())))
            if word in self.prob_positive:
                ppositive += log(self.prob_positive[word])
            else:
                if self.method == 'tf-idf':
                    ppositive -= log(self.sum_tf_idf_positive + len(list(self.prob_positive.keys()))) 
                else:
                    ppositive -= log(self.positive_words + len(list(self.prob_positive.keys())))
            pnegative += log(self.prob_negative_mail)
            ppositive += log(self.prob_positive_mail)
        return pnegative >= ppositive
    
    def predict(self, testData):
        result = dict()
        for (i, account) in enumerate(testData):
            processed_account = process_account(account)
            result[i] = int(self.classify(processed_account))
        return result


transactions = pd.read_csv('negative.csv', encoding = 'latin-1')
#n=transactions.head()
#print(n)
transactions.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis = 1, inplace = True)
transactions.rename(columns = {'v1': 'labels', 'v2': 'account'}, inplace = True)
transactions['label'] = transactions['labels'].map({'positive': 0, 'negative': 1})
transactions.drop(['labels'], axis = 1, inplace = True)
n=transactions.head()
#print(n)

m=transactions['account'].shape[0]
#print(m)
totaltransactions = m
trainIndex, testIndex = list(), list()
#randomly selects a sample from the data
for i in range(transactions.shape[0]):
    x=np.random.uniform(0, 1)
    #print(x)
    if x < 0.75:
        #trainIndex += [i]
        #print([i])
        trainIndex=trainIndex+[i]
    else:
        #testIndex += [i]
        testIndex=testIndex+[i]
#print(trainIndex)
#print(testIndex)
#print(testIndex)
trainData = transactions.loc[trainIndex]
#print(trainIndex)
testData = transactions.loc[testIndex]
n=testData[testData['label'] == 1]
testData.reset_index(inplace = True)
#print(testData)
print(testData[8][1])

#l=list(transactions[transactions['label'] == 1])
#print(l)
negative_words = ' '.join(list(transactions[transactions['label'] == 1]['account']))
#print(negative_words)

positive_words = ' '.join(list(transactions[transactions['label'] == 0]['account']))
#print(positive_words)+-6

def process_account(account, lower_case = True, stem = True, stop_words = True, gram = 2):
    if lower_case:
        account = account.lower()
    words = word_tokenize(account)
    words = [w for w in words if len(w) > 2]
    if gram > 1:
        w = []
        for i in range(len(words) - gram + 1):
            w += [' '.join(words[i:i + gram])]
        return w
    if stop_words:
        sw = stopwords.words('english')
        words = [word for word in words if word not in sw]
    if stem:
        stemmer = PorterStemmer()
        words = [stemmer.stem(word) for word in words]   
    return words

sc_tf_idf = negativeClassifier(trainData, 'tf-idf')
sc_tf_idf.train()
preds_tf_idf = sc_tf_idf.predict(testData['account'])
metrics(testData['label'], preds_tf_idf)

pm = process_account('Congratulations')
sc_tf_idf.classify(pm)


