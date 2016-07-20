import unittest
import behavior
from tokenizer import *

class TestBehaviorAnalyzer(unittest.TestCase):

  def test_that_behavior_analyzer_receives_list_from_tokenizer(self):
    self.assertEqual(self.tokenizer.words_are_tokenized()

  def test_behavior_input_is_a_list(self):
    pass

  def test_behavior_input_returns_a_list_of_integers(self):
    pass

  def test_input_list_contains_alphanumeric_characters(self):
    pass

  def test_input_list_contains_punctuation(self):
    pass

  def test_passive_sentence_contains_periods_and_commas(self):
    pass

  def test_aggressive_sentence_contains_exclamation(self):
    pass

  def test_sentence_contains_aggressive_words(self):
    pass

  def test_assertiveness_sentence_contains_periods(self):
    pass

  def test_inquisitiveness_sentence_contains_question_marks(self):
    pass

  def test_passive_aggressiveness_sentence_contains_question_marks_commas(self):
    pass

  def test_informative_sentence_contains_periods_and_semi_colons(self):
    pass


if __name__ == '__main__':
  unittest.main()
