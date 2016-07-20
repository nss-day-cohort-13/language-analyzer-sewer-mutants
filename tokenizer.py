import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer


def phrase_to_string(phrase):
    #"assures the input is not an empty string, and converts input into lower case"

  text = phrase.lower()
  return text


def words_are_tokenized(text):
  wordCount = text.lower()
  wordCount = word_tokenize(text)
  return wordCount


def alpha_num_characters(text):
    aplhaNumText = "".join(c for c in text if c not in ('!','.',':','?',',',"'",'-',' '))
    aplhaNumText = aplhaNumText.lower()
    df = nltk.FreqDist(aplhaNumText)
    alphaNums = list(df.keys())
    return alphaNums
