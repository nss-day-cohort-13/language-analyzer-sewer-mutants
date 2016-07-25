# Language Analyzer Group Project

## Information

For this group project, design is of utmost importance. Team discussion, white boarding, and Trello cards will take up the majority of the time. You must consider the relationships between the different components. You must consider the inputs for behavior and the expected output.

Also put significant thought into how inheritance, composition, and aggregation patterns will be used to create the relationships between all the modules.

## Requirements

1. A full test suite. There should be no logic in your project for which there is not a test.
1. Documentation. Every class, and every method should have a docstring.

# Language Analyzer

The language analyzer is the main module that will use sentiment analysis, and behavior prediction to produce a report for each person's message.

##### Example output

```
# Yours **does not** have to look like this. It's just an example

Message: "Suzy sells seashells by the seashore"

Sentiment:
    0.52 (Positive)

Behavior(s):
    0.58 (Aggressive)
    0.88 (Transaction)

Domain(s):
    0.925 (Financial)
```

## Sentiment Analysis

Sentiment analysis is a complex topic, but for this project you will use these basic criteria in your module.

1. Words stored in the `sentiment` key of the lexicon.
1. Punctuation (e.g. exclamation points may increase the sentiment value)
1. Behavior value

Given these criteria, produce a sentiment value between 0 and 1 for each message.

## Behavior Predictor

This module will determine what behavior is expressed in a message. Use the following criteria.

1. Words stored in the `behavior` key of the lexicon.
1. Punctuation (e.g. question marks may indicate inquisitiveness, exclamation point may indicate aggressiveness)

Given these criteria, produce a behavior value between 0 and 1 for each message, for each behavior identified.

> **Instructor guidance:** You may want to add more behaviors to the lexicon as you identify them.

## Tokenizer

The tokenizer module will produce the following results for each message.

1. Alphanumeric Characters
1. Word count
1. Word position
1. Sentence count
1. Punctuation

## Domain Identifier

The domain identification module will determine the subject matter of the message. Use the following criteria.

1. Words stored in the `domain` key of the lexicon.
1. Punctuation
1. Word count

Given these criteria, produce a domain value between 0 and 1 for each message, for each domain identified.

> **Instructor guidance:** You may want to add more domains to the lexicon as you identify them.

##### Example

> Friendship is like money, easier made than kept.

There are two domains in this small quote.

1. Relationships
1. Financial

However, the word position of `friendship`, being at the beginning of the sentence, may indicate that is has a higher weight.
