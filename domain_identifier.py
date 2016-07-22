from tokenizer import *
import lexicon

class Domain:

  # political_list=[]
  # relational_list=[]
  # inquisitive_list=[]
  def __init__(self, text):
    self.tokenizer = Token(" ".join(text))
    self.behavioralDict = {}
    self.politicalDict = {}
    self.relationalDict = {}


    self.tokenizer.words_are_tokenized(" ".join(text))
    print(self.tokenizer.words_are_tokenized(" ".join(text)))
    self.assign_behavioral_values(text)
    print(self.assign_behavioral_values(text))
    self.assign_political_values(text)
    print(self.assign_political_values(text))
    self.assign_relational_values(text)
    print(self.assign_relational_values(text))


  def input_is_list(self, phrase):
    #"assures the input is not an empty string, and converts input into lower case"

    text = phrase
    return text


  def assign_behavioral_values(self, phrase):
    behavioral_list=[]
    for item in phrase:
          value = lexicon.behavioral_sentiment.get(item, 0)
          behavioral_list.append(value)
    # Analyze.behavioral_dictionary(self, behavioral_list)

          behavioral_dict = {}
          behavioral_nums = behavioral_list

          behavioral_sum = sum(behavioral_nums)

          behavioral_dict['behavioral'] = behavioral_sum # update existing entry
          self.behavioralDict = behavioral_dict
    return behavioral_dict




  def assign_political_values(self, phrase):
    political_list=[]
    for item in phrase:
          value = lexicon.political_sentiment.get(item, 0)
          political_list.append(value)

          political_dict = {}
          political_nums = political_list

          political_sum = sum(political_nums)

          political_dict['political'] = political_sum # update existing entry
          self.politicalDict = political_dict
    return political_dict





  def assign_relational_values(self,phrase):
    relational_list=[]
    for item in phrase:
          value = lexicon.relational_sentiment.get(item, 0)
          relational_list.append(value)


          relational_dict = {}
          relational_nums = relational_list

          relational_sum = sum(relational_nums)

          relational_dict['relational'] = relational_sum # update existing entry
          self.relationalDict = relational_dict
    return relational_dict




  def spitsentiment(self, text):
    if self.assign_behavioral_values(text) >= self.assign_political_values(text):
      print(self.assign_behavioral_values(text))
    elif self.assign_political_values(text) >= self.assign_behavioral_values(text):
      print(self.assign_political_values(text))

    if self.assign_relational_values(text) >= self.assign_inquisitive_values(text):
      print(self.assign_relational_values(text))
    elif self.assign_inquisitive_values(text) >= self.assign_relational_values(text):
      print(self.assign_inquisitive_values(text))
