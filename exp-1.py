import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter

'''nltk.download('punkt')
nltk.download('stopwords')'''
text = input("Enter a paragraph:")
text = text.lower()
tokens = word_tokenize(text)
tokens = [word for word in tokens if word not in string.punctuation]
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in tokens if word not in stop_words]
ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_words]
frequency = Counter(filtered_words)
print("\nOriginal Tokens:")
print(tokens)
print("\nFiltered Words:")
print(filtered_words)
print("\nStemmed Words:")
print(stemmed_words)
print("\nWord Frequency:")
for word, count in frequency.items():
 print(word,":",count)




OUTPUT:-
enter a sentence:Natural Language Processing helps computers understand human language and process text
efficiently.
Original Tokens:
['natural', 'language', 'processing', 'helps', 'computers', 'understand', 'human', 'language', 'and',
'process', 'text', 'efficiently']
Filtered Words:
['natural', 'language', 'processing', 'helps', 'computers', 'understand', 'human', 'language', 'process',
'text', 'efficiently']
Stemmed Words:
['natur', 'languag', 'process', 'help', 'comput', 'understand', 'human', 'languag', 'process', 'text', 'effici']

Word Frequency:
natural : 1
language : 2
processing : 1
helps : 1
computers : 1
understand : 1
human : 1
process : 1
text : 1
efficiently : 1
