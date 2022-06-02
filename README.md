# samananthar
Samananthar v1\
**Samanantar dataset** which is the largest publicly available parallel corpora collection for Indic languages.\
Below is the link provide to download the parallel corpus data of required English-X (indic-language) :\
         **https://indicnlp.ai4bharat.org/samanantar/**   \
In our work we considered the below language pairs :
 Samanantar En-X(indic) corpus       | Number of sentence pairs | 
| ------------- |:-------------:|
| English-Hindi (en-hi)      | 8.56 million  | 
| English-Telugu (en-te)      | 4.82 million     | 


Before getting into the wider spectrum of work we performed two levels of filtration over the two language pair corpora to get the filtered data.\
\
**Filtration levels :**\
\
	**Filter 1 :** Extraction of sentences between **sentence (word) length of threshold 5 to 100.** Below are the number of sentences extracted in each language pair.
	 Samanantar En-X(indic) corpus        | Number of sentence pairs      |
| ------------- |:-------------:|
| English-Hindi (en-hi)    | 79,61,610 | 
| English-Telugu (en-te)   | 30,36,823    |  

	      
**Filter 2 :** Removing the corresponding parallel sentences from both English-Hindi (en-hi) files which has **english text in hindi file** and **junk in both english text file and hindi text files.**  Similarly removing the corresponding parallel sentences from both English-Telugu (en-te) files which has **english text in telugu file** and **junk in both english text file and hindi text files.** \

 Samanantar En-X(indic) corpus      | Number of clean sentence pairs           | Number of pruned sentence pairs  |
| ------------- |:-------------:| :-----:|
| English-Hindi (en-hi)      | 76,22,024 | 3,39,586 |
| English-Telugu (en-te)     | 29,68,429      |   68,394 |

		  
**Filter 3 :** By finding **“average for Bleu, Chrf++ scores”**, we extracted sentences which are **greater than the average scores** from En-Hi and En-Te corpora. The below number of sentences are only on 15,000 sentence pairs only.
Samanantar En-X(indic) corpus      | Number of clean sentence pairs           | Number of pruned sentence pairs  |
| ------------- |:-------------:| :-----:|
| English-Hindi (en-hi)      | 2312 | 12,688 |
| English-Telugu (en-te)     | 1985      |   13,015 |

		  
By finding the **average Cosine similarity scores**, we extracted sentences from **En-Hi and En-Te** corpora whose **average values are greater than the average value.

 Samanantar En-X(indic) corpus        | Number of sentence pairs       |
| ------------- |:-------------:|
| English-Hindi (en-hi)    | 98,149 (calculated scores only for 1,50,000 sentence pairs only)| 
| English-Telugu (en-te)   | 1,92,291 (calculated scores only for 3,26,912 sentence pairs only)    |

		  
Below are the number of sentences extracted from **above filter3 i.e sentences greater than the average value of chrf++ and bleu scores and extracted sentences whose LaBSE Cosine similarity score is greater than it's average LaBSE cosine similarity score.**

Samanantar En-X(indic) corpus      | Number of clean sentence pairs          | Number of pruned sentences pairs |
| ------------- |:-------------:| :-----:|
| English-Hindi (en-hi)      | 2061 | 251 |
| English-Telugu (en-te)     | 1607      |   378 |

		  
		    
Link for all filtered text is mentioned in the below link :\
		    **https://drive.google.com/drive/folders/1er8tHCn99ETbQabD7MaA_KLBgTn8d5IC?usp=sharing**
