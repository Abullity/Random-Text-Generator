# Random-Text-Generator
Program generates random sentences from a text file (corpus).

## Description
The program takes text file and number of wanted senteces to be generated as an input
and outpus random sentences with variable length based on the provided text's content.

More specifically,  program generates bigrams or trigrams (default) using [nltk](https://www.nltk.org/) library (a dictionary data-structure with two words as a key and the third word as a value, for every three word in the text), gets probabilities for each trigrams and creates random sentence based on the probabilities.

## Dependencies
The module required for the program is nltk
you could install it either by running:

`pip install nltk`

or

`pip install -r requirements.txt`

## Running the program

The program takes a text file path and number of wanted sentences as an input,
so the proper usage is the following:

`python TextGeneratorAI.py [text file] [n of sentences]`

`corpus.txt` contains script from [Game Of Thrones](https://www.imdb.com/title/tt0944947/?ref_=ttfc_fc_tt) , so you could use that as a text file.
