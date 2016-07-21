import tokenizer
import lexicon
from behavior_analyzer import *

# print(lexicon.positive_sentiment)

class Sentiment_analyzer:


	def assign_positive_values(self, sentence_list):
		positive_list=[]


		for item in sentence_list:
			value = lexicon.positive_sentiment.get(item, 0)
			positive_list.append(value)
		# print(positive_list)

		return positive_list

	def assign_neutral_values(self, sentence_list):
		neutral_list=[]


		for item in sentence_list:
			value = lexicon.neutral_sentiment.get(item, 0)
			neutral_list.append(value)


		# print(neutral_list)

		return neutral_list

	def assign_negative_values(self, sentence_list):
		negative_list=[]


		for item in sentence_list:
			value = lexicon.negative_sentiment.get(item, 0)
			negative_list.append(value)
		# print(negative_list)

		return negative_list



# assign_positive_values(["it", "is", "nice", "to", "be", "happy", "."])


