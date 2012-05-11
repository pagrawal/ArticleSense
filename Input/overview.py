#! /usr/bin/env python
import sys
sys.path.append('/home/pagrawal/demo/Input/')
import sync
import scanner
import tfidf
import fetch
import output

class MyOverview:
	
	def input(self):
		import re
		
		#get article
		return re.findall('\w+',open('/home/pagrawal/demo/Input/input.txt').read().lower())

	
if __name__ == '__main__':
	from operator import itemgetter
	
	start = MyOverview()
	words = start.input()
	
	#Sync
	one = sync.MySync()
	o_sync = one.sync(words)
	
	#Scanner
	two = scanner.MyScanner()
	o_scanner = two.scanner(o_sync)

	#Tf-idf
	three = tfidf.MyTfidf()
	words = three.main(o_scanner)
	o_tfidf = []
	x = 0
	my_words = []
	for item in sorted(words.items(), key=itemgetter(1), reverse=True):
		if(x == 15):
			break
		o_tfidf.append((item[0], (15-x)))
		my_words.append(item[0])
		x = x + 1
	
	#Fetch
	four = fetch.MyFetch()
	o_fetch = four.fetch(o_tfidf)

	#Output
	five = output.MyOutput()
	o_ouput = five.output(o_fetch, my_words)