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
		  **- Retained english & hindi sentences : 76,22,024 sentences\
		    - Filtered english & hindi sentences : 3,39,586 sentences**\
  Similarly removing the corresponding parallel sentences from both English-Telugu (en-te) files which has **english text in telugu file** and **junk in both english text file and hindi text files.** \
  Below are the number of sentences extracted in each language pair.\
		  **- Retained english & telugu sentences : 29,68,429 sentences\
		    - Filtered english & telugu sentences : 68,394 sentences**\
**Filter 3 :** By finding **“average for Bleu, WER, Chrf++ scores”**, we extracted sentences which are **greater than the average scores** from En-Hi and En-Te corpora.\
		  **-Retained En-Hi sentences : 316 sentences (on 3000 sentences only)\
		    -Retained En-Te sentences : 333 sentences (on 3000 sentences only)**\
By finding the **average Cosine similarity scores**, we extracted sentences from **En-Hi and En-Te** corpora whose **average values are greater than the average value.\
		  -Retained En-Hi sentences: 98,149 sentences (on 1,50,000 lakh sentences only)\
		  -Retained En-Te sentences: 1,92,291 sentences (on 3,26,912 sentences only)**

		    
Link for all filtered text is mentioned in the below link :\
		    https://drive.google.com/drive/folders/1szGM1GcBNr1V7_aY-R3Jfasb6pGlG_R0?usp=sharing 
