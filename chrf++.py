
# Run this file from CMD/Terminal
# Example Command: python3 sentence-wer.py test_file_name.txt mt_file_name.txt

import sys
import sacrebleu
from sacrebleu.metrics import CHRF
from datasets import load_metric
chrf = load_metric("chrf")


target_test = sys.argv[1]	#  Test file argument
target_pred = sys.argv[2]	#  MTed file argument


# Open the test dataset human translation file
chrf_in = []
with open(target_test) as test:
    for l in test:
        chrf_in.append(l.strip())
print(len(chrf_in), 'lines=')
#print("Reference 1st sentence:", line1[0])

# Open the translation file by the NMT model
chrf_ou =[]
with open(target_pred) as pred:
    for line in pred:
        chrf_ou.append(line.strip())
print(len(chrf_ou), 'lines=')


chrf_file = "chrf++-" + target_pred 

# Calculate Chrf++ for sentence by sentence and save the result to a file
with open(chrf_file, "w+") as output:
    for line in zip(chrf_in, chrf_ou):
        test = [line[0]]
        pred = [[line[1]]]
        #print(test, pred)
        chrf_score = chrf.compute(predictions=test, references=pred, word_order=2)
        s1 = (chrf_score["score"])/100
        #print(list(chrf_score.keys()))
        
        #print("min score", chrf_score)
        #print("max score", chrf_score)
        #ter_score = ter(test, pred, standardize=True)  # "standardize" expands abbreviations
        #print(wer_score, "\n")
        output.write(str(s1) + "\n")
    #chrf_score = chrf.compute(predictions=chrf_in, references=[chrf_out])
print("Done! Please check the Chrf++ file '" + chrf_file + "' in the same folder!")
