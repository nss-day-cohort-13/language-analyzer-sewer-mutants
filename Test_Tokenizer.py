import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer


text1 = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

text1 = text1.lower()

wordCount = (word_tokenize(text1))

punctuation_list = []
for i in wordCount:
   if i =="," or i=="." or i=="!" or i =="?" or i ==":" or i ==";":
    punctuation_list.append(i)

    print(punctuation_list)            # makes list of all punctuation marks in list of words

# ****SENTENCE COUNT******
SentCount = (sent_tokenize(text1))

print(len(SentCount)) # outputs  sentence count


#****** WORD FREQUENCY/ ALPHA NUMERIC/ WORD COUNT *******

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
tokenWords = tokenizer.tokenize(text1)  #converts initial string into list of words

print(tokenWords)



fd = nltk.FreqDist(tokenWords)
wordFreq = fd.items()                   #outputs word frequency

print(wordFreq)



wordPos = dict(enumerate(tokenWords))
print(wordPos)
