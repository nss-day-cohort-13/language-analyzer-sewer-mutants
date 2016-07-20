# text = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

# text1 = text.lower()
# wordCount = word_tokenize(text1)
# #print(wordCount)

# aplhaNumText = "".join(c for c in text1 if c not in ('!','.',':','?',',',"'",'-',' '))
# aplhaNumText = out.lower()
# df = nltk.FreqDist(out)
# alphaNums = df.keys()
# #print(alphaNums)

# punctuation_list = []
# for i in wordCount:
#     if i =="," or i=="." or i=="!" or i =="?" or i ==":" or i ==";":
#         punctuation_list.append(i)
# #print(punctuation_list)

# sentence_list = (sent_tokenize(text1))
# sentence_count = len(sentence_list)
# # print(sentence_count)

# regex_tokenizer = RegexpTokenizer(r'\w+')
# token_words = regex_tokenizer.tokenize(text1)
# fd = nltk.FreqDist(token_words)
# word_frequency = fd.items()
# # print(word_frequency)

# word_position = dict(enumerate(token_words))
# word_position = {k+1:v for (k,v) in word_position.items()}
# print(word_position)
# #converts list of words into dictionary
