import nltk
from nltk.tokenize import word_tokenize

'''nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')'''

sentence = input("Enter a sentence:")
tokens = word_tokenize (sentence)
tagged = nltk.pos_tag(tokens)
grammar = r"""
NP:{<DT>?<JJ>*<NN.*>+}
"""
chunk_parser = nltk.RegexpParser(grammar)
chunk_tree = chunk_parser.parse(tagged)
print("\nChunk Tree")
print(chunk_tree)
chunk_tree.draw()

OUTPUT:-
Enter a sentence: The intelligent student won the coding competition.
POS Tagged Sentence

[('The', 'DT'),
('intelligent', 'JJ'),
('student', 'NN'),
('won', 'VBD'),
('the', 'DT'),
('coding', 'NN'),
('competition', 'NN'),
('.', '.')]

Chunk Tree

(S
(NP The/DT intelligent/JJ student/NN)
won/VBD
(NP the/DT coding/NN competition/NN)
./.)
