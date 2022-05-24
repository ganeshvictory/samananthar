# samananthar
Samananthar v1\
**Samanantar dataset** which is the largest publicly available parallel corpora collection for Indic languages.\
Below is the link provide to download the parallel corpus data of required English-X (indic-language) :\
         **https://indicnlp.ai4bharat.org/samanantar/**   \
In our work we considered the below language pairs :\
	**• English-Hindi (en-hi) :** This contains **8.56 million sentence pairs.**\
	**• English-Telugu (en-te) :** This contains **4.82 million sentence pairs.**\
Before getting into the wider spectrum of work we performed two levels of filtration over the two language pair corpora to get the filtered data.\
**Filtration levels :**\
	**Filter 1 :** Extraction of sentences between **sentence (word) length of threshold 5 to 100.** \
	Below are the number of sentences extracted in each language pair.\
	      **- English-Hindi (en-hi) : 79,61,610 sentences\
		    - English-Telugu (en-te) : 30,36,823 sentences**\
	**Filter 2 :** Removing the corresponding parallel sentences from both English-Hindi (en-hi) files which has **english text in hindi file** and **junk in both english text file and hindi text files.**\
		  **- Clean english & hindi sentences : 76,22,024 sentence pairs\
		    - Pruned english & hindi sentences : 3,39,586 sentence pairs**\
  Similarly removing the corresponding parallel sentences from both English-Telugu (en-te) files which has **english text in telugu file** and **junk in both english text file and hindi text files.** \
  Below are the number of sentences extracted in each language pair.\
		  **- Clean english & telugu sentences : 29,68,429 sentence pairs\
		    - Pruned english & telugu sentences : 68,394 sentence pairs**\
**Filter 3 :** By finding **“average for Bleu, Chrf++ scores”**, we extracted sentences which are **greater than the average scores** from En-Hi and En-Te corpora.\
		  **-Clean En-Hi sentences : 2312 sentence pairs (on 15,000 sentence pairs only)\
		    -Clean En-Te sentences : 1985 sentence pairs (on 15,000 sentence pairs only)**\
By finding the **average Cosine similarity scores**, we extracted sentences from **En-Hi and En-Te** corpora whose **average values are greater than the average value.\
		  -Clean En-Hi sentences: 98,149 sentence pairs (on 1,50,000 lakh sentence pairs only)\
		  -Clean En-Te sentences: 1,92,291 sentence pairs (on 3,26,912 sentence pairs only)**\
Below are the number of sentences extracted from **15,000 sentences whose LaBSE Cosine similarity score is greater than it's average LaBSE cosine similarity score.\
		  -Clean En-Hi sentences: 2061 sentence pairs (on 15,000 sentence pairs)\
		  -Pruned En-Hi sentences : 251 sentence pairs\
		  -Clean En-Te sentences: 1607 sentence pairs (on 15,000 sentence pairs)\
		  -Pruned En-Te sentences: 378 sentence pairs**

		    
Link for all filtered text is mentioned in the below link :\
		    **https://drive.google.com/drive/folders/1er8tHCn99ETbQabD7MaA_KLBgTn8d5IC?usp=sharing**
