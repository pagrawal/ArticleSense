#! /usr/bin/env python

class MyOutput:

	def feedback(self, score):
		import math
		#feedback calculations
		if(score > 11 or score < -11):
			# score < -11
			if(score < 0):
				return (-10 - math.log((score* -1)))
			# score > 11
			else:
				return(10 + math.log(score))
		# 11> score > -11
		else:
			return score
	
	def output(self, list, words):
		import re
		import MySQLdb

		#connect to database
		conn = MySQLdb.connect (host = "localhost", 
								user = "pagrawal", 
								passwd = "mypw", 
								db = "my_wiki")
		cursor = conn.cursor ()

		#sort list by ids
		list.sort()
		
		#calcualte weight of articles based on ranking of words's rank
		temp = 0
		final_id = [] 
		final_weight = []
		for x in list:
			if(int(x[0]) != temp):
				temp = int(x[0])
				#see if there is any feedback information for each results
				cursor.execute ("""select score, word from my_feedback where id = %s and score <> 0;""", (x[0]))
				results = cursor.fetchall()
				num = 0
				my_score = 0.0
				#calc feedback information for all words associated with each article
				if(len(results) != 0):
					for y in results:
						for z in words:
							#print (z == y[1])
							if(z == y[1]):
								my_score = my_score + float(y[0])
								num = num + 1
				final_id.append(temp)
				if(num == 0):
					num = 1
				#if(my_score != 0):
				#	print my_score, num,(my_score/num) 
				final_weight.append(x[1] + float(self.feedback((my_score/num))))
			else:
				final_weight[-1] = final_weight[-1] + x[1]
		
		#put ids and weight of word in a tuple to easily sort by weight
		tup = []	
		for x in range(len(final_id)):
			tup.append((final_weight[x], final_id[x]))
		tup.sort()
		tup.reverse()
		
		#get top ten articles
		final = []
		for x in range(0,10):
			final.append(tup[x])
		
		#get list of article titles based id of article
		title = []
		page_list = []
		for page_id in final:
			page = page_id[1]
			page_list.append(page)
			cursor.execute ("""select page_title from my_page where page_latest = %s;""", (page))
			output = cursor.fetchall()
			title.append(output[0][0])
			
			#adding information to feedback if it does not already have an entry
			for word in words:
				amt = cursor.execute ("""select score from my_feedback where id = %s AND word = %s;""", (page, word))
				if(amt == 0):
					url = "http://www.en.wikipedia.org/wiki/" + output[0][0]
					cursor.execute (""" INSERT INTO my_feedback (id, url, word, score) VALUES (%s, %s, %s, %s) """, 
					(page, url, word, 0))

			
		#print out list for user to view easily
		b = open('/home/pagrawal/demo/Input/output.txt', 'w')
		for x in range(len(title)):
			my_title = str(title[x])
			title[x] = re.sub(r'\_', r' ',title[x])
			b.write(str(x+1) + ".;" + str(my_title + "; http://www.en.wikipedia.org/wiki/" + my_title) + ";" + str(page_list[x]) + "\n")	

			
		a = open('/home/pagrawal/demo/Input/words.txt', 'w')
		for x in words:
			a.write(x + ";")
		a.close()
