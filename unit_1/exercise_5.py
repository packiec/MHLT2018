import nltk
from nltk.corpus import brown
from utils import lexical_diversity

print("Lexical diverstity score for humour (Brown Corpus)")
print(lexical_diversity(brown.words(categories='humor')))

print("Lexical diverstity score for romance (Brown Corpus)")
print(lexical_diversity(brown.words(categories='romance')))