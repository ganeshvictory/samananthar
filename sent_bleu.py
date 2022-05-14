# BLEU for segment by segment with arguments
# Run this file from CMD/Terminal
# Example Command: python3 compute-bleu-sentence-args.py test_file_name.txt mt_file_name.txt

import sys
import datasets
from sacremoses import MosesDetokenizer
sacrebleu = datasets.load_metric("sacrebleu")
md = MosesDetokenizer(lang='te')

target_test = sys.argv[1]  # Test file argument
target_pred = sys.argv[2]  # MTed file argument

# Open the test dataset human translation file and detokenize the references
'''
refs = []

with open(target_test) as test:
    for line in test: 
        line = line.strip().split() 
        line = md.detokenize(line) 
        refs.append(line)
print(len(refs), 'lines==')    
#print("Reference 1st sentence:", refs[0])

# Open the translation file by the NMT model and detokenize the predictions
preds = []

with open(target_pred) as pred:  
    for line in pred: 
        line = line.strip().split() 
        line = md.detokenize(line) 
        preds.append(line)
print(len(preds), 'line==')
'''

bleu_in = []
with open(target_test) as test:
    for l in test:
        bleu_in.append(l.strip())
print(len(bleu_in), 'lines=')
#print("Reference 1st sentence:", line1[0])

# Open the translation file by the NMT model
bleu_ou =[]
with open(target_pred) as pred:
    for line in pred:
        bleu_ou.append(line.strip())
print(len(bleu_ou), 'lines=')

bleu_file = "bleu-" + target_pred 
# Calculate BLEU for sentence by sentence and save the result to a file
a = []
with open(bleu_file, "w+") as output:
    for line in zip(bleu_in, bleu_ou):
        test = [line[0]]
        pred = [[line[1]]]
        #print(test, pred)
        #print(test, "\t--->\t", pred)
        bleu_score = sacrebleu.compute(predictions=test, references=pred)
        s1 = (bleu_score["score"])/100
        #print(list(bleu_score.keys()))
        
        #print(min(bleu_score))
        #print(bleu.score, "\n")
        #output.write(str(bleu_score["score"]) + "\n")
        output.write(str(s1) + "\n")
