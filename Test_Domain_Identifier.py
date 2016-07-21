import unittest
import tokenizer

class TestDomainIdentifier(unittest.Testcase)

@classmethod
  def domain_set_up(self):
    self.test_list_financial= ["Money", ";", "it's", "a", "gas", "."]
    self.test_list_behavioral= ["S", "T", "F", "U", "!"]
    self.test_list_scientific= ["I", "have", "become", "capable", "of", "bestowing", "animation", "upon", "lifeless", "matter", "!"]
    self.test_list_educational= ["R", "T", "F", "M", "!"]
    self.test_list_political= ["Cthulhu", "for", "President", "!", "No", "lives", "matter", "."]
    self.test_list_relational= ["G", "T", "F", "O", "!"]

    self.test_dict_financial= {"finance": 1}
    self.test_dict_behavioral= {"behavior": 2}
    self.test_dict_scientific= {"science": 3}
    self.test_dict_educational= {"educatory": 2}
    self.test_dict_political= {"politics": 2}
    self.test_dict_relational= {"relationship": 2}

  def test_domain_input_is_a_list(self):
    self.assertIsInstance(self.test_string_financial, list)
    self.assertIsInstance(self.test_string_behavioral, list)
    self.assertIsInstance(self.test_string_scientific, list)
    self.assertIsInstance(self.test_string_educational, list)
    self.assertIsInstance(self.test_string_political, list)
    self.assertIsInstance(self.test_string_realtional, list)

  # This test group ensures that each domain-specific high-value word
  # (e.g.-'money' for financial domain) receives a value of 1 and that
  # other non-essential words in the test input string receive a value of 0.

  def test_domain_comprehension_returns_list_of_numbers_for_financial_domain(self):
    self.assertEqual(self.domain.assign_fiancial_values(self.test_list_financial),[1,0,0,0,0,0])

  def test_domain_comprehension_returns_list_of_numbers_for_behavioral_domain(self):
    self.assertEqual(self.domain.assign_behavioral_values(self.test_list_behavioral),[1,0,0,1,0])

  def test_domain_comprehension_returns_list_of_numbers_for_scientific_domain(self):
    self.assertEqual(self.domain.assign_scientific_values(self.test_list_scientific),[0,0,0,0,0,0,1,0,1,1,0])

  def test_domain_comprehension_returns_list_of_numbers_for_educational_domain(self):
    self.assertEqual(self.domain.assign_educational_values(self.test_list_educational),[1,0,0,1,0])

  def test_domain_comprehension_returns_list_of_numbers_for_political_domain(self):
    self.assertEqual(self.domain.assign_political_values(self.test_list_political),[0,0,1,0,0,0,1,0])

  def test_domain_comprehension_returns_list_of_numbers_for_relational_domain(self):
    self.asserEequal(self.domain.assign_realtional_values(self.test_list_relational),[1,0,0,1,0])

if __name__ == '__main__':
    unittest.main()

  # def test_that_domain_identifier_receives_master_word_list_from_tokenizer(self):
  #   self.assertEqual(lexicon.master.list, list)

  # def test_that_domain_identifier_receives_word_count_from_tokenizer(self):
  #   self.assertEqual(tokenizer.word_count, int)

  # def test_that_domain_identifier_receives_punctuation_list_from_tokenizer(self):
  #   self.assertIsInstance(tokenizer.punc_list, list)

  # def test_that_domain_identifier_returns_zero_or_greater_for_each_message_in_each_domain(self):
  #   self.assertLessEqual(tokenizer.number, 0)

  # def test_that_domain_identifier_returns_one_or_less_for_each_message_in_each_domain(self):
  #   self.assertLessEqual(tokenizer.number, 1)

  # def test_that_domain_comprehension_returns_a_list_of_number_values_from_each_input_message_for_each_individual_domain(self):
  #   self.assertEqual(self....., list)

  # def test_that_domain_identifier_returns_word_count_for_input_message(self):
  #   self.assertIsInstance(self....., int)

  # def test_that_domain_identifier_adds_word_values_together_for_a_given_input_message(self):
  #   self.assertIsInstance(self....., num1)

  # def test_that_domain_identifier_uses_word_value_sum_to_set_base_domain_value(self):
  #   self.assertEqual(self.num1, DV)


  #   def test_each_domains_dictionary_is_combined(self):
    # self.assertequal(domain.combined_dictionary(self.test_dict_positive,self.test_dict_neutral,self.test_dict_negative),)


