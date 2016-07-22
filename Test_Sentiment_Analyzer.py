import unittest
from tokenizer import *
from sentiment_analyzer import *
import lexicon
class TestSentimentAnalyzer(unittest.TestCase):

    @classmethod
    def setUp(self):
        # self.sentiment_analyzer = Behave()
        self.test_list_all= ["Get", "the", "hell", "out", ",", "before", "I" ,"hammer", "stomp", "your", "ugly", "face", "in", "!",
        "Whatever", "it's", "meh", "they", "taste", "fine", ".",
        "OMG","1", "I", "love", "chocolate", "1",
        "Do", "you", "even", "lift", "bro", "?"]

        self.test_list_negative = ["Get", "the", "hell", "out", ",", "before", "I" ,"hammer", "stomp", "your", "ugly", "face", "in", "!"]
        self.test_list_neutral = ["Whatever", "it's", "meh", "they", "taste", "fine", "."]
        self.test_list_positive = ["OMG","1", "I", "love", "chocolate", "1"]


        self.test_dict_negative= {"negative": 5}
        self.test_dict_neutral= {"neutral": 4}
        self.test_dict_positive= {"positive": 5}


        # self.agro_nums= [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]
        # self.neutral_nums= [1, 0, 1, 0, 0, 1, 1]
        # self.positive_nums= [1,1,0,1,1,1]
        # self.inquisitive_nums= [1, 0, 1, 0, 0, 1]

        self.sentiment_analyzer= Sentiment(self.test_list_all)



    def test_sentiment_input_is_a_list(self):
        self.assertIsInstance(self.test_list_negative,list)
        self.assertIsInstance(self.test_list_neutral,list)
        self.assertIsInstance(self.test_list_positive,list)




    def test_sentiment_comprehension_returns_list_of_numbers_for_negative_sentiment(self):
        self.assertEqual(self.sentiment_analyzer.assign_negative_values(self.test_list_all),{'negative': 5})

    def test_sentiment_comprehension_returns_list_of_numbers_for_neutral_sentiment(self):
        self.assertEqual(self.sentiment_analyzer.assign_neutral_values(self.test_list_neutral),{'neutral':4})


    def test_sentiment_comprehension_returns_list_of_numbers_for_positive_sentiment(self):
        self.assertEqual(self.sentiment_analyzer.assign_positive_values(self.test_list_positive),{'positive': 5})


    # def test_list_of_numbers_converted_to_dictionary_for_aggresive_sentiment(self):
    #     self.assertEqual(self.sentiment_analyzer.negative_dictionary(self.agro_nums), {"negative": 5})

    # def test_list_of_numbers_converted_to_dictionary_for_neutral_sentiment(self):
    #     self.assertEqual(self.sentiment_analyzer.neutral_dictionary(self.neutral_nums), {"neutral": 4})

    # def test_list_of_numbers_converted_to_dictionary_for_positive_sentiment(self):
    #     self.assertEqual(self.sentiment_analyzer.positive_dictionary(self.positive_nums), {"positive": 5})


    def testIt1(self):
        self.assertEqual(self.sentiment_analyzer.negativeDict, self.test_dict_negative)

    def testIt2(self):
        self.assertEqual(self.sentiment_analyzer.neutralDict, self.test_dict_neutral)

    def testIt3(self):
        self.assertEqual(self.sentiment_analyzer.positiveDict, self.test_dict_positive)




if __name__ == '__main__':
    unittest.main()


