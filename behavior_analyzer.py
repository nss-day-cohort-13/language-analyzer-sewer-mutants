import tokenizer
import lexicon

class Behave:

  # passive_list=[]
  # excited_list=[]
  # inquisitive_list=[]
  def __init__(self,text1, text2, text3, text4):
    self.aggressiveDict = {}
    self.passiveDict = {}
    self.excitedDict = {}
    self.inquisitiveDict = {}

    self.aggressive_dictionary(text1)
    self.passive_dictionary(text2)
    self.excited_dictionary(text3)
    self.inquisitive_dictionary(text4)

  def input_is_list(self, phrase):
    #"assures the input is not an empty string, and converts input into lower case"

    text = phrase
    return text


  def assign_aggressive_values(self, phrase):
    aggressive_list=[]
    for item in phrase:
          value = lexicon.aggressive_behavior.get(item, 0)
          aggressive_list.append(value)
    print(aggressive_list)
    Behave.aggressive_dictionary(self, aggressive_list)
    return aggressive_list


  def assign_passive_values(self, phrase):
    passive_list=[]
    for item in phrase:
          value = lexicon.passive_behavior.get(item, 0)
          passive_list.append(value)
    print(passive_list)
    Behave.passive_dictionary(self, passive_list)
    return passive_list


  def assign_excited_values(self,phrase):
    excited_list=[]
    for item in phrase:
          value = lexicon.excited_behavior.get(item, 0)
          excited_list.append(value)
    print(excited_list)
    Behave.excited_dictionary(self, excited_list)
    return excited_list


  def assign_inquisitive_values(self,phrase):
    inquisitive_list=[]
    for item in phrase:
          value = lexicon.inquisitive_behavior.get(item, 0)
          inquisitive_list.append(value)
    print(inquisitive_list)
    Behave.inquisitive_dictionary(self, inquisitive_list)

    return inquisitive_list


  def aggressive_dictionary(self,agro):
    aggressive_dict = {}
    aggressive_nums = agro

    aggressive_sum = sum(aggressive_nums)

    aggressive_dict['aggressive'] = aggressive_sum # update existing entry
    self.aggressiveDict = aggressive_dict
    return aggressive_dict


  def passive_dictionary(self,passive):
    passive_dict = {}
    passive_nums = passive

    passive_sum = sum(passive_nums)

    passive_dict['passive'] = passive_sum # update existing entry
    self.passiveDict = passive_dict
    print (passive_dict)
    return passive_dict


  def excited_dictionary(self,excited):
    excited_dict = {}
    excited_nums = excited

    excited_sum = sum(excited_nums)

    excited_dict['excited'] = excited_sum # update existing entry
    self.excitedDict = excited_dict
    return excited_dict


  def inquisitive_dictionary(self,inquisitive):
    inquisitive_dict = {}
    inquisitive_nums = inquisitive

    inquisitive_sum = sum(inquisitive_nums)

    inquisitive_dict['inquisitive'] = inquisitive_sum # update existing entry
    self.inquisitiveDict = inquisitive_dict
    return inquisitive_dict
