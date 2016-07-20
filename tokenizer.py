import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer


class Token:

  def phrase_to_string(self, phrase):
      #"assures the input is not an empty string, and converts input into lower case"

    self.text = phrase.lower()
    return text


  def words_are_tokenized(self):
    self.wordCount = text.lower()
    self.wordCount = word_tokenize(text)
    return wordCount


  def alpha_num_characters(self, text):
      aplhaNumText = "".join(c for c in text if c not in ('!','.',':','?',',',"'",'-',' '))
      aplhaNumText = aplhaNumText.lower()
      df = nltk.FreqDist(aplhaNumText)
      alphaNums = list(df.keys())
      alphaNums.sort()
      return alphaNums
