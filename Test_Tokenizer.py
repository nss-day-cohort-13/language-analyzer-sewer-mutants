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


    # def test_list_contains_only_punctuation(self):
    #     self.assertEqual(self.tokenizer.)

    # def test_list_contains_only_sentences(self):

    # def test_sentence_length_value__is_integer(self):

    # def test_dict_returns_word_frequency(self):

    # def test_dict_contains_word_position(sself):



if __name__ == '__main__':
  unittest.main()

