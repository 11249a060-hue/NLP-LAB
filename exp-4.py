import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

'''nltk.download('punkt')'''

text = input("Enter a sentence:")
tokens = word_tokenize(text)
print("\nOriginal Tokens")
print(tokens)
print("\nUnigrams")
for gram in ngrams(tokens,1):
    print(gram)
print("\nBigrams")
for gram in ngrams(tokens, 2):
    print(gram)
print("\nTrigrams")
for gram in ngrams(tokens, 3):
    print(gram)


OUTPUT:-
Enter a sentence:Natural Language Processing is an exciting field.

Original Tokens
['Natural', 'Language', 'Processing', 'is', 'an', 'exciting', 'field', '.']

Unigrams
('Natural',)
('Language',)
('Processing',)
('is',)
('an',)
('exciting',)
('field',)
('.',)

Bigrams
('Natural', 'Language')
('Language', 'Processing')
('Processing', 'is')
('is', 'an')
('an', 'exciting')
('exciting', 'field')
('field', '.')

Trigrams
('Natural', 'Language', 'Processing')
('Language', 'Processing', 'is')
('Processing', 'is', 'an')
('is', 'an', 'exciting')
('an', 'exciting', 'field')
('exciting', 'field', '.')
