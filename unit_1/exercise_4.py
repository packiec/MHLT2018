import nltk
from nltk.book import text2

print("length of book, words and punctuations: " + str(len(text2)))
print("length of book, discrete words and punctuations: " + str(len(set(text2))))