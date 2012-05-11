#!/usr/bin/env python

class MyTfidf:

	#count words in the document -- one word
	def freq(self, word, doc):
		return doc.split(None).count(word)

	#count words in the document -- all words
	def wordCount(self, doc):
		return len(doc.split(None))

	#count words in the document
	def numDocsContaining(self, word):
		import MySQLdb
		#connect to the database
		conn = MySQLdb.connect (host = "localhost", user = "pagrawal", passwd = "mypw", db = "my_wiki")
		cursor = conn.cursor ()
		
		amt = cursor.execute("""select numOfDocs from my_tfidf where word = %s;""", (word))
		if(amt == 0):
			amt = 1
		return int(amt)

	#text frequency
	def tf(self, word, doc):
		return (self.freq(word,doc) / float(self.wordCount(doc)))

	#inverse document frequency
	def idf(self, word):
		import math
		return float(math.log(136882) / float(self.numDocsContaining(word)))

	#calculates the tf-idf value
	def tfidf(self, word, doc):
		return (self.tf(word,doc) * self.idf(word))

	#main function takes input and evaluates the tf-idf value for every unique word
	def main(self, list):
		from collections import Counter
		
		cnt_key = []
		cnt_val = []
		cnt = Counter(list.split(None)).items()
		
		for x in range(len(cnt)):
			cnt_key.append(cnt[x][0])
			cnt_val.append(cnt[x][1])
	
		words = {}
		for word in cnt_key:
			words[word] = self.tfidf(word,list)
		return words