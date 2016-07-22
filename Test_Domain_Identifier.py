import unittest
from tokenizer import *
from domain_identifier import *
import lexicon
class TestDomainAnalyzer(unittest.TestCase):

    @classmethod
    def setUp(self):
        # self.domain_analyzer = Behave()
        self.test_list_all= ["Get", "the", "hell", "out", ",", "before", "I" ,"hammer", "stomp", "your", "ugly", "face", "in", "!",
        "Whatever", "it's", "meh", "they", "taste", "fine", ".",
        "OMG","1", "I", "love", "chocolate", "1",
        "Do", "you", "even", "lift", "bro", "?"]

        self.test_list_behavioral = ["Get", "the", "hell", "out", ",", "before", "I" ,"hammer", "stomp", "your", "ugly", "face", "in", "!"]
        self.test_list_political = ["Whatever", "it's", "meh", "they", "taste", "fine", "."]
        self.test_list_relational = ["OMG","1", "I", "love", "chocolate", "1"]


        self.test_dict_behavioral= {"behavioral": 5}
        self.test_dict_political= {"political": 4}
        self.test_dict_relational= {"relational": 5}


        # self.agro_nums= [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]
        # self.political_nums= [1, 0, 1, 0, 0, 1, 1]
        # self.relational_nums= [1,1,0,1,1,1]
        # self.inquisitive_nums= [1, 0, 1, 0, 0, 1]

        self.domain_analyzer= Domain(self.test_list_all)



    def test_domain_input_is_a_list(self):
        self.assertIsInstance(self.test_list_behavioral,list)
        self.assertIsInstance(self.test_list_political,list)
        self.assertIsInstance(self.test_list_relational,list)




    def test_domain_comprehension_returns_list_of_numbers_for_behavioral_domain(self):
        self.assertEqual(self.domain_analyzer.assign_behavioral_values(self.test_list_all),{'behavioral': 5})

    def test_domain_comprehension_returns_list_of_numbers_for_political_domain(self):
        self.assertEqual(self.domain_analyzer.assign_political_values(self.test_list_political),{'political':4})


    def test_domain_comprehension_returns_list_of_numbers_for_relational_domain(self):
        self.assertEqual(self.domain_analyzer.assign_relational_values(self.test_list_relational),{'relational': 0})


    # def test_list_of_numbers_converted_to_dictionary_for_aggresive_domain(self):
    #     self.assertEqual(self.domain_analyzer.behavioral_dictionary(self.agro_nums), {"behavioral": 5})

    # def test_list_of_numbers_converted_to_dictionary_for_political_domain(self):
    #     self.assertEqual(self.domain_analyzer.political_dictionary(self.political_nums), {"political": 4})

    # def test_list_of_numbers_converted_to_dictionary_for_relational_domain(self):
    #     self.assertEqual(self.domain_analyzer.relational_dictionary(self.relational_nums), {"relational": 5})


    def testIt1(self):
        self.assertEqual(self.domain_analyzer.behavioralDict, self.test_dict_behavioral)

    def testIt2(self):
        self.assertEqual(self.domain_analyzer.politicalDict, self.test_dict_political)

    def testIt3(self):
        self.assertEqual(self.domain_analyzer.relationalDict, self.test_dict_relational)




if __name__ == '__main__':
    unittest.main()



if __name__ == '__main__':
  unittest.main()



