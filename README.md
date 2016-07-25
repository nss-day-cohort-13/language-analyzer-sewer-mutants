# Language Analyzer in Python
___
#### A Group Project
#### for Nashville Software School's Full-Stack Dev Bootcamp
___
## Description
___
##### Welcome!
This Language Analyzer is written in Python 3.3 according to the [PROJECT_DIRECTIONS.md](https://github.com/nss-day-cohort-13/language-analyzer-sewer-mutants/pull/28 "Language Analyzer Project Directions"). It takes a user-supplied text string and
* breaks that string down through a Tokenizer,
* analyzes the text through three separate modules (the Behavior Analyzer, the Sentiment Analyzer, and the Domain (subject matter) Identifier),
* and makes those outputs available to the final Language Analyzer module.

The Language Analyzer then prints a brief report, in plain English, telling the user what behavior the author or speaker of the input string was likely exhibiting (aggressive or passive, excited or inquisitive), whether the overall sentiment of the input string is positive, negative, or neutral,  and what subject matter dominated the input string.

##### Accuracy
The project goal is to work out the basic logic of multiple Python modules that depend on and interact with one another and to provide some reasonable output. Accuracy of that output is not a priority.  That is, we do not employ the latest behavioral science (nor, indeed, any science at all) to arrive at our output.


## Getting Started
___
### SETUP

Click the link below and fork the repo, make sure you are signed into GitHub. If you do not have an account you will need to create one.

<https://github.com/nss-day-cohort-13/language-analyzer-sewer-mutants>

Go into your terminal and clone down the forked repo into your destination folder of choice.

```git clone https://github.com/nss-day-cohort-13/language-analyzer-sewer-mutants.git ```

#### In your terminal run the commands listed below:

Check to see if Python is installed .

```which python```

Check which version is installed. Most likely it will be version 2.7.x.

```python -V```

Once have confirmed that Python is installed and your machine is running the latest version, you will then need to install NLTK(Natural Language Toolkit):

```pip install nltk```

If your machine is NOT running the latest version of python, please refer to the Installing Python section below.
### Installing Python:

##### Windows Users:

Windows does not come with Python installed. You need to visit the Python downloads site and grab version 3.3.6 and install it. It will get installed to the C:\Python33 directory.

After it is installed, you must add C:\Python to your system path. Here's how.

Press your Windows key.
Start typing Control.
The search results should have the Windows Control Panel as the first result. Press enter.
When the control panel screen appears, start typing in environment in the search bar in the upper right corner.
Select the option to change environment variables. If you are presented with two options, choosing either one is fine.
When the screen appears, click the button at the bottom for environment variables.
Next, click on the PATH variable and choose to edit it.
Go to the end of the string, and enter a semi-colon, and the new path entry. ;C:\Python33

##### Osx/Pyenv:

If you don't have Homebrew installed then run these commands in order.

```brew install pyenv ``` \
```pyenv install 3.3.6```

After Pyenv is installed, you can make version 3.3.6 the new, globally accepted version by typing the following.

```pyenv global 3.3.6``` \
Now, when you check the version of Python with the command below, it should return 3.3.6.

```python -V```

##### NLTK:

Once you have confirmed that Python is installed and your machine is running the latest version, you will then need to install NLTK(Natural Language Toolkit).

``` pip install nltk ```

## Testing
___
This Language Analyzer was built using test-driven development. If you would like to run our unit tests, type the following commands in your command line:
* ```python Test_Behavior_Analyzer.py```
* ```python Test_Sentiment_Analyzer.py```
* ```python Test_Domain_Identifier.py```
* ```python Test_Tokenizer.py```

## Running The Program
___
In order to run the Language Analyzer Program, open up your command line & make sure you’re running Python 3. To check which version of Python you are currently using, type
```python -V```
. (If you do have an older version of Python, please refer to our instructions on installing the latest version of Python in the ‘Getting Started’ section of this README.)

Once you are sure that you are using the latest version of Python, you can use our Language Analyzer to test your sentences.  Type
```run_program('sentence')```

The Language Analyzer will then give you an output in detail of the Sentiment, Behavior & Domain broken down with information on word frequency, sentence count & word position.

## Authors
___
Castle Crawford, Mark Easterling, John Green, and Damon Romano.

## Acknowledgements
___
**Castle** would like to thank the Dread Cthulhu for its timely advice regarding hair conditioner.

**Mark** offers a remembrance of his adopted grandmother, Grob'lokx of The Nwar'Dee, who took him in and raised him as her own after accidentally killing and eating his Earth parents.

**John** remains eternally grateful for the remarkably accurate and verbose fortune cookie he received nine years ago and which has guided him since.

**Damon** would like to thank The Academy.

## Copyright & License
___
This project is (c) 2016 by the authors and is licensed for use under the MIT License (MIT). Please see the [LICENSE.md](https://github.com/nss-day-cohort-13/language-analyzer-sewer-mutants/blob/master/LICENSE "Language Analyzer License") file for details
