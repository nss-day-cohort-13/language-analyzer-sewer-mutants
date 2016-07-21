import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer


class Token:


    def __init__(self, text):
        self.words_list=[]
        self.alphaNumeric = []
        self.punctuation = []
        self.sentences = []
        self.number_of_sentences = 0
        self.word_frequencies = []

        self.words_are_tokenized(text)
        self.alpha_num_characters(text)
        self.list_of_punctuation(text)
        self.sentence_list(text)
        self.sentence_count(text)
        self.word_frequency(text)




    def phrase_to_string(self, phrase):
        #"assures the input is not an empty string, and converts input into lower case"

        text = phrase.lower()
        return text


    def words_are_tokenized(self, text):
        wordCount = text.lower()
        wordCount = word_tokenize(text)

        self.words_list = wordCount
        return wordCount


    def alpha_num_characters(self, text):
        aplhaNumText = "".join(c for c in text if c not in ('!','.',':','?',',',"'",'-',' '))
        aplhaNumText = aplhaNumText.lower()
        df = nltk.FreqDist(aplhaNumText)
        alphaNums = list(df.keys())
        alphaNums.sort()

        self.alphaNumeric = alphaNums
        return alphaNums


    def list_of_punctuation(self,text):
        punctuation_list = []
        for i in text:
            if i =="," or i=="." or i=="!" or i =="?" or i ==":" or i ==";":
                punctuation_list.append(i)

        self.punctuation = punctuation_list
        return punctuation_list


    def sentence_list(self, text):
        sentence_list = (sent_tokenize(text))

        self.sentences = sentence_list
        return sentence_list


    def sentence_count(self, text):
        sentence_list = (sent_tokenize(text))
        sentence_count = len(sentence_list)

        self.number_of_sentences = sentence_count
        return sentence_count


    def  word_frequency(self,text):
        text = text.lower()
        regex_tokenizer = RegexpTokenizer(r'\w+')
        token_words = regex_tokenizer.tokenize(text)
        fd = nltk.FreqDist(token_words)
        word_frequency = list(fd.items())
        word_frequency.sort()

        self.word_frequencies = word_frequency
        return word_frequency


    def word_position(phrase,text):
        word_position = dict(enumerate(text))
        word_position = {k+1:v for (k,v) in word_position.items()}
        return word_position

