#! /usr/bin/env python

class MySync:
	def sync(self,words):
		from nltk.corpus import wordnet as wn
		import re

		o = ""
		#convert words in the english dictionary to present tense
		for x in range(len(words)):
			temp = ""
			if(len(words[x]) <= 2):
				continue
			words[x] = re.sub(r'\'', r' ',words[x])
			if(wn.synsets(words[x], wn.VERB) != []):
				temp = wn.morphy(words[x], wn.VERB)
			elif(wn.synsets(words[x], wn.NOUN) != []):
				temp = wn.morphy(words[x], wn.NOUN)
			else:
				temp = words[x]
			if(len(temp) <= 2):
				continue
			o = o + str(temp) + " "
			#print words[x], str(temp)
		return o