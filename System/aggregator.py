#! /usr/bin/env python
import re
import MySQLdb
from collections import *

#connect to server
conn = MySQLdb.connect (host = "localhost", 
						user = "pagrawal", 
						passwd = "mypw", 
						db = "my_wiki")
cursor = conn.cursor ()

#query the database for all articles
cursor.execute ("select * from my_table;")
list = cursor.fetchall ()

#find the most common words in all articles
all_words = []
my_row = 0
my_data = ""
for row in list:
	my_row = row[0]
	my_data = " " + row[1]

	words = re.findall(r"\w+", my_data)
	c = Counter(words).most_common(15)
	
	#insert all the information into the my_highfreq table
	for x in range(len(c)):
		my_word = c[x][0]
		cursor.execute (""" 
			INSERT INTO my_highfreq (text_id, word, rank)
			VALUES (%s, %s, %s) """, 
			(my_row, my_word, (15-x)))

print "Done"
cursor.close ()
conn.commit ()
conn.close ()