from tokenizer import *
import lexicon

class Sentiment:
# feedback: DocStrings needed

  # neutral_list=[]
  # positive_list=[]
  # inquisitive_list=[]
  def __init__(self, text):
  # feedback: DocStrings needed
    self.tokenizer = Token(" ".join(text))
    self.negativeDict = {}
    self.neutralDict = {}
    self.positiveDict = {}


    self.tokenizer.words_are_tokenized(" ".join(text))
    print(self.tokenizer.words_are_tokenized(" ".join(text)))
    self.assign_negative_values(text)
    print(self.assign_negative_values(text))
    self.assign_neutral_values(text)
    print(self.assign_neutral_values(text))
    self.assign_positive_values(text)
    print(self.assign_positive_values(text))


  def input_is_list(self, phrase):
    # feedback: DocStrings needed
    #"assures the input is not an empty string, and converts input into lower case"

    text = phrase
    return text


  def assign_negative_values(self, phrase):
    # feedback: DocStrings needed
    negative_list=[]
    for item in phrase:
          value = lexicon.negative_sentiment.get(item, 0)
          negative_list.append(value)
    # Analyze.negative_dictionary(self, negative_list)

          negative_dict = {}
          negative_nums = negative_list

          negative_sum = sum(negative_nums)

          negative_dict['negative'] = negative_sum # update existing entry
          self.negativeDict = negative_dict
    return negative_dict




  def assign_neutral_values(self, phrase):
        # feedback: DocStrings needed

    neutral_list=[]
    for item in phrase:
          value = lexicon.neutral_sentiment.get(item, 0)
          neutral_list.append(value)

          neutral_dict = {}
          neutral_nums = neutral_list

          neutral_sum = sum(neutral_nums)

          neutral_dict['neutral'] = neutral_sum # update existing entry
          self.neutralDict = neutral_dict
    return neutral_dict





  def assign_positive_values(self,phrase):
    # feedback: DocStrings needed

    positive_list=[]
    for item in phrase:
          value = lexicon.positive_sentiment.get(item, 0)
          positive_list.append(value)


          positive_dict = {}
          positive_nums = positive_list

          positive_sum = sum(positive_nums)

          positive_dict['positive'] = positive_sum # update existing entry
          self.positiveDict = positive_dict
    return positive_dict




  def spitsentiment(self, text):
    # feedback: DocStrings needed
    if self.assign_negative_values(text) >= self.assign_neutral_values(text):
      print(self.assign_negative_values(text))
    elif self.assign_neutral_values(text) >= self.assign_negative_values(text):
      print(self.assign_neutral_values(text))

    if self.assign_positive_values(text) >= self.assign_inquisitive_values(text):
      print(self.assign_positive_values(text))
    elif self.assign_inquisitive_values(text) >= self.assign_positive_values(text):
      print(self.assign_inquisitive_values(text))
