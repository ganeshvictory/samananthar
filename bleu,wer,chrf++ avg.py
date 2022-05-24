#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict
import numpy as np
def load_doc(filename):
	# open the file as read only
    file = open(filename, mode='rt', encoding='utf-8')
    text = file.read()
	# close the file
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


# In[9]:


f1 = 'clean_te_en_filter2.txt'
doc = load_doc(f1)
sentences_te = to_sentences(doc)


# In[10]:


f1 = 'clean_en_te_filter2.txt'
doc = load_doc(f1)
sentences_en = to_sentences(doc)


# In[11]:


with open('te1_te.txt', 'r') as f1, open('chrf++_te1_te.txt', 'r') as f3, open('en1(te)_en.txt', 'r') as f4, open('chrf++_en1(te)_en.txt', 'r') as f6:
    #n = len(f1)
    n = len(f1.readlines())
    f1.seek(0)
    eng_ls=[]
    tel_ls=[]
    threshold_1 = np.array([0.14008, 0.33933]) #avg{bleu, chrf++}
    threshold_2 = np.array([0.18536, 0.41375])
    for i in range(n):
        lang1_bleu = float(f1.readline())
        lang1_chrf = float(f3.readline())
        lang2_bleu = float(f4.readline())
        lang2_chrf = float(f6.readline())
        if threshold_1[0]<= lang1_bleu and threshold_1[1] <= lang1_chrf and threshold_2[0] <= lang2_bleu and threshold_2[1] <= lang2_chrf:
            eng_ls.append(sentences_en[i])
            tel_ls.append(sentences_te[i])


# In[13]:


len(tel_ls)


# In[14]:


with open("clean_en_te_filter3.txt",'w') as outfile:
    for sentence in eng_ls:
        outfile.write(sentence+'\n')


# In[15]:


with open("clean_te_en_filter3.txt",'w') as outfile:
    for sentence in tel_ls:
        outfile.write(sentence+'\n')


# In[ ]:




