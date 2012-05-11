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

o = open('wordfreq.txt', 'w')

#counts freq of all words
all_data = []
for row in list:
	my_row = row[0]
	my_data = row[1]
	
	p = re.compile('\w+')	
	words = p.findall(my_data)

	c = Counter(words).items()
	#print c
	
	for x in range(len(c)):
		all_data.append(c[x][0])
		#o.write(str(c[x][0]) + " ")

cnt = Counter(all_data).items()
for x in range(len(cnt)):
	key = cnt[x][0]
	val = cnt[x][1]
	cursor.execute (""" 
		INSERT INTO my_tfidf (word, numOfDocs)
		VALUES (%s, %s) """, 
		(key, val))
	o.write(str(key)+" "+str(val)+"\n")
	#print str(key)+" "+str(val)
		
o.close()

print "Done"

cursor.close ()
conn.commit ()
conn.close ()