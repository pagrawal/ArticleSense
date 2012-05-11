#! /usr/bin/env python
from nltk.corpus import wordnet as wn
import re
import MySQLdb

#connect to the database
conn = MySQLdb.connect (host = "localhost", 
						user = "pagrawal", 
						passwd = "mypw", 
						db = "my_wiki")
cursor = conn.cursor ()

print 14
cursor.execute ("select * from my_table limit 140000,10000;")
#cursor.execute ("select * from my_table limit 10000;")
list = cursor.fetchall()

#synchronize the word tenses
for row in list:
	my_row = row[0]
	my_data = row[1].lower()
	
	p = re.compile('\w+')	
	words = p.findall(my_data)
	my_output = ""
	for x in words:
		if(len(x) <= 2):
			continue
		if(wn.synsets(x, wn.VERB) != []):
			x = wn.morphy(x, wn.VERB)
		elif(wn.synsets(x, wn.NOUN) != []):
			x = wn.morphy(x, wn.NOUN)
		if(len(x) <= 2):
			continue
		my_output = my_output + str(x) + " "
		
	#put the manipulated article back into the database			
	cursor.execute (""" 
		UPDATE my_table SET old_text = %s
		WHERE old_id = %s
		""", (my_output, my_row))	

print "Done"
cursor.close ()
conn.commit ()
conn.close ()