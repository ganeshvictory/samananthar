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

#Function for filtration
def isindicValid(indicSentence) -> bool:
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

def filter1(sentences_en, sentence_xx):
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


        if not isindicValid(indicSentence) or not isEnglishValid(englishSentence):
            deletedindicSentences.append(indicSentence)
            deletedEnglishSentences.append(englishSentence)
        else:
            retainedindicSentences.append(indicSentence)
            retainedEnglishSentences.append(englishSentence)

    print (len(deletedindicSentences))
    print (len(deletedindicSentences))
    print (len(retainedindicSentences))
    print (len(retainedEnglishSentences))

    return (deletedEnglishSentences, deletedindicSentences, retainedEnglishSentences, retainedindicSentences)

def writefile(filename, sentences):
    with open(filename, 'w') as outfile:
        for sent in sentences:
            outfile.write(sent+'\n')



#call in main function
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', help='second languages in MT', required=True)

    arguments = parser.parse_args()

    languages = arguments.lang
    #print(languages)


    #common_path = '/Users/apple/Documents/samananthar/clean_'
    #filename_1 = common_path+'en_'+languages+'_filter1.txt'
    #filename_2 = common_path+languages+'_en_filter1.txt'

    common_path = '/Users/apple/Documents/samananthar/filter1/en-'+languages+'/clean_'
    filename_1 = common_path+'en_'+languages+'_filter1.txt'
    filename_2 = common_path+languages+'_en_filter1.txt'

    
    #eng
    doc = load_doc(filename_1)
    sentences_en = to_sentences(doc)
    length_indices_en = create_dictionary(sentences_en)

    #indic
    doc = load_doc(filename_2)
    sentences_in = to_sentences(doc)
    length_indices_in = create_dictionary(sentences_in)
    

    
    print(filename_1)
    print(filename_2)
     
    
    save_path = '/Users/apple/Documents/samananthar/filter2/en-'+languages
    savefile_1 = save_path+'/pruned_en_'+languages+'_filter2.txt'
    savefile_2 = save_path+'/pruned_'+languages+'_en_filter2.txt'
    savefile_3 = save_path+'/clean_en_'+languages+'_filter2.txt'
    savefile_4 = save_path+'/clean_'+languages+'_en_filter2.txt'

    print(savefile_1)
    print(savefile_2)
    print(savefile_3)
    print(savefile_4)

    
    a, b, c, d = filter1(sentences_en, sentences_in)

    writefile(savefile_1, a)
    writefile(savefile_2, b)
    writefile(savefile_3, c)
    writefile(savefile_4, d)

    with open(savefile_1,"r") as f:
        print('./pruned_en_'+languages+'_filter2.txt', len(f.readlines()))  # This would give length of files.

    with open(savefile_2,"r") as f1:
        print('./pruned_'+languages+'_en_filter2.txt', len(f1.readlines()))  # This would give length of files.

    with open(savefile_3,"r") as f2:
        print('./clean_en_'+languages+'_filter2.txt', len(f2.readlines()))  # This would give length of files.

    with open(savefile_4,"r") as f3:
        print('./clean_'+languages+'_en_filter2.txt', len(f3.readlines()))  # This would give length of files.

    

    #print (./clean_en_'+languages+'_filter1.txt, len(savefile_1))
    #print ('./clean_'+languages+'_en_filter1.txt', len(savefile_2))

    

      
