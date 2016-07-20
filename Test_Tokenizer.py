import unittest
import tokenizer

class TestTokenizer(unittest.TestCase):

    def test_if_input_is_string(self):
        test_string = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
        self.assertIsInstance(tokenizer.phrase_to_string(test_string),str)

    def test_cannot_equal_empty_string(self):
        test_string = ""

        self.assertRaises(TypeError, tokenizer.phrase_to_string(test_string))
    def test_string_is_tokenized(self):
        test_string = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
        self.assertIsInstance(tokenizer.words_are_tokenized(test_string),list)


    def test_list_contains_only_alpha_numeric_characters(self):
        test_string = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
        self.assertIsInstance(tokenizer.alpha_num_characters(test_string),list)

    def test_list_contains_only_punctuation(self):

    def test_list_contains_only_sentences(self):

    def test_sentence_length_value__is_integer(self):

    def test_dict_returns_word_frequency(self):

    def test_dict_contains_word_position(sself):



if __name__ == '__main__':
  unittest.main()

