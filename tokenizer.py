import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer


class Token:

  def phrase_to_string(self, phrase):
      #"assures the input is not an empty string, and converts input into lower case"

    text = phrase.lower()
    return text


  def words_are_tokenized(self):
    wordCount = text.lower()
    wordCount = word_tokenize(text)
    return wordCount


  def alpha_num_characters(self, text):
    aplhaNumText = "".join(c for c in text if c not in ('!','.',':','?',',',"'",'-',' '))
    aplhaNumText = aplhaNumText.lower()
    df = nltk.FreqDist(aplhaNumText)
    alphaNums = list(df.keys())
    alphaNums.sort()
    return alphaNums


  def list_of_punctuation(self,text):
    punctuation_list = []
    for i in text:
        if i =="," or i=="." or i=="!" or i =="?" or i ==":" or i ==";":
         punctuation_list.append(i)
    return punctuation_list


  def sentence_list(self, text):
    sentence_list = (sent_tokenize(text))
    return sentence_list


  def sentence_count(self, text):
    sentence_list = (sent_tokenize(text))
    sentence_count = len(sentence_list)
    return sentence_count


  def  word_frequency(self,text):
    text = text.lower()
    regex_tokenizer = RegexpTokenizer(r'\w+')
    token_words = regex_tokenizer.tokenize(text)
    fd = nltk.FreqDist(token_words)
    word_frequency = list(fd.items())
    word_frequency.sort()
    return word_frequency


  def word_position(phrase,text):
    word_position = dict(enumerate(text))
    word_position = {k+1:v for (k,v) in word_position.items()}
    return word_position

