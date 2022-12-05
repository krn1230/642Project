import nltk
from nltk.parse.generate import generate
from nltk import CFG

def sentence(noun_list1, noun_list2, verb_list, adv_list, adj_list):
	
	# parse a list into 'a' | 'b' | ...
	nouns = ""
	for w in noun_list1:
		nouns += "'" + w + "' |"

	nouns2 = ""
	for w in noun_list2:
		nouns2 += "'" + w + "' |" 

	verbs = ""
	for w in verb_list:
		verbs += "'" + w + "' |"

	advs = ""
	for w in adv_list:
		advs += "'" + w + "' |"

	adjs = ""
	for w in adj_list:
		adjs += "'" + w + "' |"

	grammar2 = nltk.CFG.fromstring("""
	S -> N1 Adv V Adj N2
	""" 
	+ 
	"N1 ->" + nouns
	+ 
	"\nN2 ->" + nouns2
	+ 
	"\nV ->" + verbs
	+
	"\nAdv ->" + advs
	+
	"\nAdj ->" + adjs
	)

	for sentence in generate(grammar2, depth = 5, n = 1):
		return ' '. join(sentence)
