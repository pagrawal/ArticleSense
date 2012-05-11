#! /usr/bin/env python

class MyFetch:

	def fetch(self, words):
		import MySQLdb

		#connect to the database
		conn = MySQLdb.connect (host = "localhost", 
								user = "pagrawal", 
								passwd = "mypw", 
								db = "my_wiki")
		cursor = conn.cursor ()

		#for all the most commonly used words...
		output = []		
		for word in words:
			my_word = word[0]
			my_rank = word[1]

			cursor.execute ("""select text_id, rank, word from my_highfreq where word like %s;""",
				(my_word))
			list = cursor.fetchall()

			for x in list:
				id = str(x[0]).strip("L")
				rank = x[1]
				if(rank > 13 and my_rank > 13):
					weight = ((float(rank) + float(my_rank))/2)+3
				elif(rank > 11 and my_rank > 11):
					weight = ((float(rank) + float(my_rank))/2)+2
				elif(rank > 9 and my_rank > 9):
					weight = ((float(rank) + float(my_rank))/2)+1
				else:
					weight = ((float(rank) + float(my_rank))/2)
				output.append((id,weight))
		return output