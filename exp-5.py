import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

'''nltk.download('punkt')'''
text = input("Enter a text corpus:").lower()
tokens = word_tokenize(text)
tokens = [word for word in tokens if word.isalpha()]
word_count = Counter(tokens)
V = len(word_count)
N = sum(word_count.values())
print("\nWord\t\tCount\tSmoothed Probability")
print("-"*50)
for word in word_count:
    probability = (word_count[word]+1)/(N+V)
    print(f"{word:15}{word_count[word]:5}\t{probability:.4f}")

OUTPUT:-
Enter a sentence: I love Python I love NLP Python is easy

Word   Count   Smoothed Probability
--------------------------------------------------
i        2        0.1875
love     2        0.1875
python   2        0.1875
nlp      1        0.1250
is       1        0.1250
easy     1        0.1250
