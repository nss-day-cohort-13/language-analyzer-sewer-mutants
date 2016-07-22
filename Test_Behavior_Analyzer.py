import unittest
from tokenizer import *
from behavior_analyzer import *
import lexicon
class TestBehaviorAnalyzer(unittest.TestCase):

    @classmethod
    def setUp(self):
        # self.behavior_analyzer = Behave()
        self.test_list_aggressive = ["Get", "the", "hell", "out", ",", "before", "I" ,"hammer", "stomp", "your", "ugly", "face", "in", "!"]
        self.test_list_passive = ["Whatever", "it's", "meh", "they", "taste", "fine", "."]
        self.test_list_excited = ["OMG","!", "I", "love", "chocolate", "!"]
        self.test_list_inquisitive = ["Do", "you", "even", "lift", "bro", "?"]

        self.test_dict_aggressive= {"aggressive": 5}
        self.test_dict_passive= {"passive": 4}
        self.test_dict_excited= {"excited": 5}
        self.test_dict_inquisitive = {"inquisitive": 3}

        self.agro_nums= [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]
        self.passive_nums= [1, 0, 1, 0, 0, 1, 1]
        self.excited_nums= [1,1,0,1,1,1]
        self.inquisitive_nums= [1, 0, 1, 0, 0, 1]

        self.behavior_analyzer= Behave(self.agro_nums, self.passive_nums, self.excited_nums, self.inquisitive_nums)


    def test_behavior_input_is_a_list(self):
        self.assertIsInstance(self.test_list_aggressive,list)
        self.assertIsInstance(self.test_list_passive,list)
        self.assertIsInstance(self.test_list_excited,list)
        self.assertIsInstance(self.test_list_inquisitive,list)



    def test_behavior_comprehension_returns_list_of_numbers_for_aggressive_behavior(self):
        # self.behavior_analyzer = Behave(self.test_list_aggressive)
        self.assertEqual(self.behavior_analyzer.assign_aggressive_values(self.test_list_aggressive),[0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1])

    def test_behavior_comprehension_returns_list_of_numbers_for_passive_behavior(self):
        self.assertEqual(self.behavior_analyzer.assign_passive_values(self.test_list_passive),[1, 0, 1, 0, 0, 1, 1])


    def test_behavior_comprehension_returns_list_of_numbers_for_excited_behavior(self):
        self.assertEqual(self.behavior_analyzer.assign_excited_values(self.test_list_excited),[1,1,0,1,1,1])

    def test_behavior_comprehension_returns_list_of_numbers_for_inquisitive_behavior(self):
        self.assertEqual(self.behavior_analyzer.assign_inquisitive_values(self.test_list_inquisitive),[1, 0, 1, 0, 0, 1])


    def test_list_of_numbers_converted_to_dictionary_for_aggresive_behavior(self):
        self.assertEqual(self.behavior_analyzer.aggressive_dictionary(self.agro_nums), {"aggressive": 5})

    def test_list_of_numbers_converted_to_dictionary_for_passive_behavior(self):
        self.assertEqual(self.behavior_analyzer.passive_dictionary(self.passive_nums), {"passive": 4})

    def test_list_of_numbers_converted_to_dictionary_for_excited_behavior(self):
        self.assertEqual(self.behavior_analyzer.excited_dictionary(self.excited_nums), {"excited": 5})

    def test_list_of_numbers_converted_to_dictionary_for_inquisitive_behavior(self):
        self.assertEqual(self.behavior_analyzer.inquisitive_dictionary(self.inquisitive_nums), {"inquisitive": 3})

    def testIt1(self):
        self.assertEqual(self.behavior_analyzer.aggressiveDict, self.test_dict_aggressive)

    def testIt2(self):
        self.assertEqual(self.behavior_analyzer.passiveDict, self.test_dict_passive)

    def testIt3(self):
        self.assertEqual(self.behavior_analyzer.excitedDict, self.test_dict_excited)

    def testIt4(self):
        self.assertEqual(self.behavior_analyzer.inquisitiveDict, self.test_dict_inquisitive)



if __name__ == '__main__':
  unittest.main()

