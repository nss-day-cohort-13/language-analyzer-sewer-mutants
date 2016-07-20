import unittest
from tokenizer import *
class TestTokenizer(unittest.TestCase):


    @classmethod
    def setUp(self):
      self.tokenizer = Token()

      self. test_string = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You should eat cardboard."

      self. test_string_tokenized = ['Hello', 'Mr.', 'Smith', ',', 'how', 'are', 'you', 'doing', 'today', '?', 'The', 'weather', 'is', 'great', ',', 'and', 'Python', 'is', 'awesome', '.', 'The', 'sky', 'is', 'pinkish-blue', '.', 'You', 'should', 'eat', 'cardboard', '.']


    def test_if_input_is_string(self):
        self.assertIsInstance(self.test_string,str)


    def test_string_is_tokenized(self):
       self.assertIsInstance(self.test_string_tokenized, list)


    def test_list_contains_only_alpha_numeric_characters(self):
        self.assertEqual(self.tokenizer.alpha_num_characters(self.test_string),['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y'])


    def test_list_contains_only_punctuation(self):
        self.assertEqual(self.tokenizer.list_of_punctuation(self.test_string_tokenized),[',', '?', ',', '.', '.', '.'])


    def test_list_contains_seperate_sentences(self):
        self.assertEqual(self.tokenizer.sentence_list(self.test_string),['Hello Mr. Smith, how are you doing today?', 'The weather is great, and Python is awesome.', 'The sky is pinkish-blue.', 'You should eat cardboard.'] )


    def test_sentence_length_value__is_integer(self):
        self.assertEqual(self.tokenizer.sentence_count(self.test_string), 4)


    def test_dict_returns_word_frequency(self):
        self.assertEqual(self.tokenizer.word_frequency(self.test_string), [('and', 1), ('are', 1), ('awesome', 1), ('blue', 1), ('cardboard', 1), ('doing', 1), ('eat', 1), ('great', 1), ('hello', 1), ('how', 1), ('is', 3), ('mr', 1), ('pinkish', 1), ('python', 1), ('should', 1), ('sky', 1), ('smith', 1), ('the', 2), ('today', 1), ('weather', 1), ('you', 2)])

    def test_dict_contains_word_position(self):
      self.assertEqual(self.tokenizer.word_position(self.test_string_tokenized),{1: 'Hello', 2: 'Mr.', 3: 'Smith', 4: ',', 5: 'how', 6: 'are', 7: 'you', 8: 'doing', 9: 'today', 10: '?', 11: 'The', 12: 'weather', 13: 'is', 14: 'great', 15: ',', 16: 'and', 17: 'Python', 18: 'is', 19: 'awesome', 20: '.', 21: 'The', 22: 'sky', 23: 'is', 24: 'pinkish-blue', 25: '.', 26: 'You', 27: 'should', 28: 'eat', 29: 'cardboard', 30: '.'})


if __name__ == '__main__':
  unittest.main()

