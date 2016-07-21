import unittest
from sentiment_analyzer import *

class TestSentiment(unittest.TestCase):

    @classmethod
    def sentiment_set_up(self):
        self.test_list_positive= ["it", "is", "nice", "to", "be", "happy", "."]
        self.test_list_neutral= ["everything", "is", "okay", "."]
        self.test_list_negative= ["being", "bad", "is", "terrible", "."]
        self.test_dict_positive= {"positive": 2}
        self.test_dict_neutral= {"neutral": 1}
        self.test_dict_negative= {"negative": 2}

    def test_seniment_input_is_a_list(self):
        self.assertIsInstance(self.test_string_positive,list)
        self.assertIsInstance(self.test_string_neutral,list)
        self.assertIsInstance(self.test_string_negative,list)



    def test_sentiment_comprehension_returns_list_of_numbers_for_positive_sentiment(self):
        self.assertequal(sentiment.assign_positive_values(self.test_list_positive),[0,0,1,0,0,1,0])

    def test_sentiment_comprehension_returns_list_of_numbers_for_neutral_sentiment(self):
        self.assertequal(sentiment.assign_neutral_values(self.test_list_neutral),[0,0,1,0])

    def test_sentiment_comprehension_returns_list_of_numbers_for_negative_sentiment(self):
        self.assertequal(sentiment.assign_negative_values(self.test_list_negative),[0,1,0,1,0])



    def test_list_of_numbers_converted_to_dictionary_for_positive_sentiment(self):
        self.assertequal(sentiment.positive_dictionary(test_list_positive, {"positive": 2}))

    def test_list_of_numbers_converted_to_dictionary_for_neutral_sentiment(self):
        self.assertequal(sentiment.neutral_dictionary(test_list_neutral, {"neutral": 1}))

    def test_list_of_numbers_converted_to_dictionary_for_negative_sentiment(self):
        self.assertequal(sentiment.negative_dictionary(test_list_negative, {"negative": 2}))



  #   def test_each_sentiments_dictionary_is_combined(self):
		# self.assertequal(sentiment.combined_dictionary(self.test_dict_positive,self.test_dict_neutral,self.test_dict_negative),)



if __name__ == '__main__':
    unittest.main()


