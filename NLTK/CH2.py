
#4

import nltk
from nltk.corpus import state_union

for speech in state_union.fileids():
    words = state_union.words(fileids=[speech])
    fdist = nltk.FreqDist(w.lower() for w in words)
    print(speech)
    print("she: ", fdist["she"], end='\n')
    print("he: ", fdist["he"], end='\n')
    print("people: ", fdist["people"], end='\n')

