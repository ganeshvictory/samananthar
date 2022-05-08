import argparse
from collections import defaultdict

# Write all the relavent methods that proccess data

def load_doc(filename):
    # open the file as read only
    with open(filename, mode='rt', encoding='utf-8') as file:
        text = file.read()
    # close the file
    return text

def to_sentences(doc):
    return doc.strip().split('\n')

def sentence_lengths(sentences):
    lengths = [len(s.split()) for s in sentences]
    return min(lengths), max(lengths)

def load_doc(filename):
    # open the file as read only
    with open(filename, mode='rt', encoding='utf-8') as file:
    # read all text
        text = file.read()
    # close the file
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


def savefile(filename_en, filename_xx, sentences_en, sentences_xx, length_indices_in):

    #based on indic sentences, we take indic sentences
    sentences_indices = []
    for i in range(5,101):
        sentences_indices+=length_indices_in.get(i)
    with open(filename_en, 'w', encoding='utf8') as of1, open(filename_xx, 'w', encoding='utf8') as of2:
        for sent in sentences_indices:
            of1.write(sentences_en[sent]+'\n')
            of2.write(sentences_xx[sent]+'\n')





if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', help='second languages in MT', required=True)

    arguments = parser.parse_args()

    languages = arguments.lang
    #print(languages)


    common_path = '/Users/apple/Documents/samanantar research/en-'
    filename_1 = common_path+languages+'/train.en'
    filename_2 = common_path+languages+'/train.'+languages

    savefile_1 = './clean_en_'+languages+'.txt'
    savefile_2 = './clean_'+languages+'_en.txt'
    
    #eng
    doc = load_doc(filename_1)
    sentences_en = to_sentences(doc)
    length_indices_en = create_dictionary(sentences_en)

    #indic
    doc = load_doc(filename_2)
    sentences_in = to_sentences(doc)
    length_indices_in = create_dictionary(sentences_in)

    l = sentences_en[ :2]
    print (l)

    #print(filename_1)
    #print(filename_2)

  

    # do all the things necessary to prepare cleaned sentence

    savefile_1 = './clean_en_'+languages+'.txt'
    savefile_2 = './clean_'+languages+'_en.txt'

    savefile(savefile_1, savefile_2, sentences_en, sentences_in, length_indices_in) 

    
    
