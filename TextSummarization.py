import re
import heapq
import nltk
import pandas as pd

# nltk.download('punkt')
# nltk.download('stopwords')

# Read comment from CSV file
path = 'C:\\Users\\Tanachart\\Desktop\\AsianFacts\\Project\\'
csvdf = pd.read_csv(path +"asian_facts_comment.csv",header=None)
article_text = ' '.join(csvdf[0])

# Removing Square Brackets and Extra Spaces
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)
article_text = re.sub(r'\"', ' ', article_text)

# Removing special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

# Return a sentence-tokenized copy of *text*,
# using NLTK's recommended sentence tokenizer
sentence_list = nltk.sent_tokenize(article_text)

# Get list of stopword
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

# Calculating Sentence Scores
sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]




# Calculate number of line to be display after summarization
numberOfLine = round(len(nltk.word_tokenize(formatted_article_text))/50)
print(numberOfLine)
summary_sentences = heapq.nlargest(numberOfLine, sentence_scores, key=sentence_scores.get)

print("========== ORIGINAL SENTENCES ==========")
print(sentence_list)
print(len(nltk.word_tokenize(formatted_article_text)))
summary = ' '.join(summary_sentences)
print("========== SUMMARY SENTENCES ==========")
print(summary)
