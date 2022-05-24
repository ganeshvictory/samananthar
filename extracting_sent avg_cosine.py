#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import defaultdict
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


# In[12]:


filename = 'labse_cosine_en_te_15000.txt'
doc = load_doc(filename)
sentences_index = to_sentences(doc)
float_lst = []
for item in sentences_index:
    float_lst.append(float(item))


# In[13]:


f1 = 'clean_en_te_filter3.txt'
doc = load_doc(f1)
sentences_en = to_sentences(doc)


# In[14]:


f2 = 'clean_te_en_filter3.txt'
doc = load_doc(f1)
sentences_in = to_sentences(doc)


# In[16]:


sen_index=[]
te_lst=[]
en_lst=[]
for i in range(len(float_lst)):
        if float_lst[i] >= 0.825:
            sen_index.append(float_lst[i])
            te_lst.append(sentences_in[i])
            en_lst.append(sentences_en[i])


# In[18]:


len(te_lst)
#en_lst


# In[19]:


with open("clean_te_en_cosine_filter3.txt",'w') as outfile:
    for sentence in te_lst:
        outfile.write(sentence+'\n')


# In[20]:


with open("clean_en_te_cosine_filter3.txt",'w') as outfile:
    for sentence in en_lst:
        outfile.write(sentence+'\n')

