import nltk

lexicon = [
  {
    "sentiment":
    {
      "positive": [{"happy": 1},{"nice": 1}],
      "negative": [{"terrible": 1},{"bad": 1}],
      "neutral": [{"okay": 1}]
    },
    "domain":
    {
      "financial": [],
      "behavioral": [],
      "scientific": [],
      "educational": [],
      "politics": [],
      "relationships": []
    },
    "behavior":
    {
      "aggressive": [],
      "passive": [],
      "mentoring": [],
      "inquisitive": [],
      "transaction": []
    }
  }
]

"Friendship is like money, easier made than kept."


# print(lexicon[0]["sentiment"]["positive"])

positive_sentiment ={"happy": 1, "nice": 1}
neutral_sentiment = {"okay": 1}
negative_sentiment = {"terrible": 1, "bad": 1}
    # {
    #   "positive": {{"happy": 1},{"nice": 1}},
    #   "negative": {{"terrible": 1},{"bad": 1}},
    #   "neutral": {{"okay": 1}}
    # }}
