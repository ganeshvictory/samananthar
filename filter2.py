#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from collections import defaultdict


# In[2]:


def load_doc(filename):
    #open the file as read only
    file = open(filename, mode='rt', encoding='utf-8')
    text = file.read()
    #close the file
    file.close()
    return text
    
def to_sentences(doc):
    return doc.strip().split('\n')
    
def sentence_lengths(sentences):
    lengths = [len(s.split()) for s in sentences]
    return min(lengths), max(lengths)
def load_doc(filename):
	# open the file as read only
    file = open(filename, mode='rt', encoding='utf-8')
	# read all text
    text = file.read()
	# close the file
    file.close()
    return text

def create_dictionary(sentences):
    # Create a dictionary whose key is sentence length and value is the sentence indices
    length_ind_dict = defaultdict(list)
    
    for index, sentence in enumerate(sentences):
        no_of_words = len(sentence.split(' '))
        # Sentences are binned into bins according to the number of words 100:
        # If key value is 10, it contains all the sentences that have 10 words in it
        key = no_of_words
        
        length_ind_dict[key].append(index)
    
    return length_ind_dict
    
 
# split a loaded document into sentences
def to_sentences(doc):
    return doc.strip().split('\n')
 
# shortest and longest sentence lengths
def sentence_lengths(sentences):
    lengths = [len(s.split()) for s in sentences]
    return min(lengths), max(lengths)
 


# In[3]:


filename = 'samanantar_hindi.txt'
doc = load_doc(filename)
sentences_in = to_sentences(doc)
length_indices_in = create_dictionary(sentences_hi)

filename = 'samanantar_english_hi.txt'
doc = load_doc(filename)
sentences_en = to_sentences(doc)
length_indices_en = create_dictionary(sentences)


# In[5]:


filename = 'samanantar_english_hi.txt'
doc = load_doc(filename)
sentences_en = to_sentences(doc)

#length_indices_en = create_dictionary(sentences)


# In[62]:


#def isTeluguValid(teluguSentence) -> bool:
def isIndicValid(indicSentence) -> bool:
    for c in indicSentence:
        if c >= 'A' and c <= 'Z':
            return False
        if c >= 'a' and c <= 'z':
            return False
        if ord(c) >= 161 and ord(c) <= 255:
            return False
    return True
    
def isEnglishValid(englishSentence) -> bool:
    for c in englishSentence:
        if ord(c) >= 161 and ord(c) <= 255:
            return False
        else:
            return True

            
       
        
#teluguList =  ["నేను K G శ్రీవత్స","నేను శ్రీవత్స","నేను <^;`~శ్రీవత్స", "నేను రీవత్స.", "నేను éäశ్రీవత్స"]
#englishList = ["I am K G Srivatsa","I am Srivatsa", "I am Srivatsa", "I €am gænesh££", "I am Ganesh"]
##Assuming that there is a 1-1 mapping between telugu and english

deletedindicSentences = []
deletedEnglishSentences = []
retainedindicSentences = []
retainedEnglishSentences = []

n = len(sentences_in)

for i in range(0,n):
    indicSentence = sentences_in[i]
    englishSentence = sentences_en[i]
    
    #print(isTeluguValid(teluguSentence))
    #print(isEnglishValid(englishSentence))
    

    if not isIndicValid(indicSentence) or not isEnglishValid(englishSentence):
        deletedindicSentences.append(indicSentence)
        deletedEnglishSentences.append(englishSentence)
    else:
        retainedHindiSentences.append(indicSentence)
        retainedEnglishSentences.append(englishSentence) 


# In[69]:


with open("filtered_hindi.txt",'w') as outfile:
    for sentence in deletedindicSentences:
        outfile.write(sentence+'\n')


# In[70]:


with open("filtered_english.txt",'w') as outfile:
    for sentence in deletedEnglishSentences:
        outfile.write(sentence+'\n')


# In[71]:


with open("retained_hindi.txt",'w') as outfile:
    for sentence in retainedindicSentences:
        outfile.write(sentence+'\n')


# In[72]:


with open("retained_english.txt",'w') as outfile:
    for sentence in retainedEnglishSentences:
        outfile.write(sentence+'\n')

