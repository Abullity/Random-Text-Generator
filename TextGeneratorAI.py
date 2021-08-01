from sys import argv, exit
import random
from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams, trigrams


def get_tokens(corpus):
	wst = WhitespaceTokenizer()
	return wst.tokenize(corpus.read())
	

def get_bigrams(tokens):
	return list(bigrams(tokens))


def get_trigrams(tokens):
	return list(trigrams(tokens))

# get probabilities for each bigram or trigram specified
def get_probabilities(bis=None, tris=None):
	probs = {}
	if bis:
		for head, tail in bis:
			probs.setdefault(head, {}).setdefault(tail, 0)
			probs[head][tail] += 1
	elif tris:
		for head1, head2, tail in tris:
			head = (head1, head2)
			probs.setdefault(head, {}).setdefault(tail, 0)
			probs[head][tail] += 1
	return probs
	
	
def generate_sentence(probs, head=None):
	sentence = []
	punctuation = ["!", "?", "."]
	
	while len(sentence) <= 5 or word_latter[-1] not in punctuation:
		if not sentence:
			word_former, word_latter = random.choice(list(probs))
			while not word_former[0].isupper() or word_former[-1] in punctuation:
				word_former, word_latter = random.choice(list(probs))
			sentence += [word_former, word_latter]
		else:
			head = (word_former, word_latter)
			tails = list(probs[head])
			weights = list(probs[head].values())
			word_former = word_latter
			word_latter = random.choices(tails, weights=weights)[0]
			sentence.append(word_latter)
	return " ".join(sentence)
		
		
if len(argv) != 3:
	print("Usage: python3 TextGeneratorAI.py [corpus file] [num of sentences]")
	exit(1)
try:
	with open(argv[1], "r", encoding="utf-8") as corpus:
		tokens = get_tokens(corpus)
	n_senteces = int(argv[2])
except FileNotFoundError:
	print("Make sure to specify valid file for the corpus!")
	exit(2)
except ValueError:
	print("Make sure that the second arguement is a number!")
	exit(3)
	
tris = get_trigrams(tokens)
probs = get_probabilities(tris=tris)
for _ in range(n_senteces):
	sentence = generate_sentence(probs)
	print(sentence)
		
