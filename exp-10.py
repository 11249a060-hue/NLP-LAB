
import nltk
from nltk.tokenize import word_tokenize

'''nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')'''

sentence = input("Enter a sentence:")
tokens = word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
grammar = r"""
NP: {<DT>?<JJ>*<NN.*>+}
VP: {<VB.*><DT>?<JJ>*<NN.*>+}
"""
chunker = nltk.RegexpParser(grammar)
chunk_tree = chunker.parse(tagged_words)
print("\nPOS Tagged Sentence")
print(tagged_words)
print("\nChunk Tree")
print(chunk_tree)
chunk_tree.draw()

OUTPUT:-
Enter a sentence: The intelligent student completed the machine learning project.
POS Tagged Sentence
[('The', 'DT'),
('intelligent', 'JJ'),
('student', 'NN'),
('completed', 'VBD'),
('the', 'DT'),
('machine', 'NN'),
('learning', 'NN'),
('project', 'NN'),
('.', '.')]

Chunk Tree

(S
(NP The/DT intelligent/JJ student/NN)
 (VP completed/VBD the/DT machine/NN learning/NN project/NN)
./.)
