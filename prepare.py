import requests
import bs4
import pandas as pd
import os


import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords


########################## Function File For NLP Prepare Exercises ############################

def basic_clean(string):
    '''
    This function takes in a string and performs some basic cleaning.
    
    Converts all alphabet characters to lowercase
    Normalize unicode characters
    recplace anything that is not a letter, number, whitespace or a single quote
    '''
    ## convert all alphabet characters to lowercase
    string = string.lower()
    
    ## normalizing the unicode characters
    string = unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')
    
    ## removing special characters
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    
    return string

def tokenize(string):
    '''
    This function is designed to take in a string and tokenize all 
    the words in the string
    '''
    #create the tokenizer
    tokenizer = nltk.tokenize.ToktokTokenizer()
    
    #use the tokenizer
    string = tokenizer.tokenize(string, return_str=True)
    
    return string   

def stem(string):
    '''
    This function is designed to take in a string as input and stems the words 
    in the string 
    '''
    ## create the nltk stemmer object, then use it
    ps = nltk.porter.PorterStemmer()
    
    ## used list comprehension on our split string to stem the words
    stems = [ps.stem(word) for word in string.split()]
    string_stemmed = ' '.join(stems)
    
    return string_stemmed

def lemmatize(string):
    '''
    This function is designed to take in a string as input and lemmatize the words 
    in the string 
    '''
    ## create the nltk lemmatizer object
    wnl = nltk.stem.WordNetLemmatizer()
    
    ## use the lemmatizer object
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    string_lemmatized = ' '.join(lemmas)
    
    return string_lemmatized

def remove_stopwords(string, extra_words = [], exclude_words = []):
    '''
    This function is designed to take in a string as input and return the words 
    in the string after removing all the stopwords
    '''
    
    ## creating our stop word list from the english word list
    stopword_list = stopwords.words('english')
    
    ## removing excluded words
    for word in exclude_words:
        stopword_list.remove(word)
    
    ## adding extra words
    for word in extra_words:
        stopword_list.append(word)
    
    ## creating a list of words from the original inputted string after splitting them
    words = string.split()
    
    ## removing stop words and setting it equal to filtered_words
    filtered_words = [w for w in words if w not in stopword_list]
    
    ## recreating our string without stopwords
    article_without_stopwords = ' '.join(filtered_words)
    
    return article_without_stopwords


def prep_content_columns(df):
    '''
    This function will apply clean, stem, and lemmatize to a df.content and
    create new columns.
    '''
    df['clean'] = df.content.apply(basic_clean)
    df['stemmed'] = df.content.apply(stem)
    df['lemmatized'] = df.content.apply(lemmatize)

    return df

######################## Complete Prep