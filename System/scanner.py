#! /usr/bin/env python
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
my_data = cursor.fetchall ()

#remove unncessary words
for row in my_data:
	my_row = row[0]
	my_data = " " + row[1]
	
	#numbers and syntax
	my_data = " " + my_data
	my_data = re.sub(r'[0-9]+', r' ',my_data)

	#most common words in english
	my_data = re.sub(r' the ', r' ', my_data )
	my_data = re.sub(r' too ', r' ', my_data )
	my_data = re.sub(r' and ', r' ', my_data )
	my_data = re.sub(r' all ', r' ', my_data )
	my_data = re.sub(r' that ', r' ', my_data )
	my_data = re.sub(r' for ', r' ', my_data )
	my_data = re.sub(r' not ', r' ', my_data )
	my_data = re.sub(r' don ', r' ', my_data ) #for don't
	my_data = re.sub(r' didn ', r' ', my_data ) #for didn't
	my_data = re.sub(r' with ', r' ', my_data )
	my_data = re.sub(r' you ', r' ', my_data )
	my_data = re.sub(r' your ', r' ', my_data )
	my_data = re.sub(r' day ', r' ', my_data )
	my_data = re.sub(r' this ', r' ', my_data )
	my_data = re.sub(r' here ', r' ', my_data )
	my_data = re.sub(r' but ', r' ', my_data )
	my_data = re.sub(r' his ', r' ', my_data )
	my_data = re.sub(r' seem ', r' ', my_data )
	my_data = re.sub(r' from ', r' ', my_data )
	my_data = re.sub(r' cannot ', r' ', my_data )
	my_data = re.sub(r' they ', r' ', my_data )
	my_data = re.sub(r' say ', r' ', my_data )
	my_data = re.sub(r' her ', r' ', my_data )
	my_data = re.sub(r' she ', r' ', my_data )
	my_data = re.sub(r' will ', r' ', my_data )
	my_data = re.sub(r' keep ', r' ', my_data )
	my_data = re.sub(r' would ', r' ', my_data )
	my_data = re.sub(r' near ', r' ', my_data )
	my_data = re.sub(r' there ', r' ', my_data )
	my_data = re.sub(r' other ', r' ', my_data )
	my_data = re.sub(r' need ', r' ', my_data )
	my_data = re.sub(r' sure ', r' ', my_data )
	my_data = re.sub(r' their ', r' ', my_data )
	my_data = re.sub(r' what ', r' ', my_data )
	my_data = re.sub(r' out ', r' ', my_data )
	my_data = re.sub(r' over ', r' ', my_data )
	my_data = re.sub(r' about ', r' ', my_data )
	my_data = re.sub(r' who ', r' ', my_data )
	my_data = re.sub(r' get ', r' ', my_data )
	my_data = re.sub(r' which ', r' ', my_data )
	my_data = re.sub(r' when ', r' ', my_data )
	my_data = re.sub(r' make ', r' ', my_data )
	my_data = re.sub(r' can ', r' ', my_data )
	my_data = re.sub(r' like ', r' ', my_data )
	my_data = re.sub(r' just ', r' ', my_data )
	my_data = re.sub(r' him ', r' ', my_data )
	my_data = re.sub(r' know ', r' ', my_data )
	my_data = re.sub(r' take ', r' ', my_data )
	my_data = re.sub(r' same ', r' ', my_data )
	my_data = re.sub(r' every ', r' ', my_data )
	my_data = re.sub(r' very ', r' ', my_data )
	my_data = re.sub(r' really ', r' ', my_data )
	my_data = re.sub(r' still ', r' ', my_data )
	my_data = re.sub(r' while ', r' ', my_data )
	my_data = re.sub(r' into ', r' ', my_data )
	my_data = re.sub(r' year ', r' ', my_data )
	my_data = re.sub(r' good ', r' ', my_data )
	my_data = re.sub(r' some ', r' ', my_data )
	my_data = re.sub(r' someone ', r' ', my_data )
	my_data = re.sub(r' something ', r' ', my_data )
	my_data = re.sub(r' already ', r' ', my_data )
	my_data = re.sub(r' able ', r' ', my_data )
	my_data = re.sub(r' let ', r' ', my_data )
	my_data = re.sub(r' could ', r' ', my_data )
	my_data = re.sub(r' should ', r' ', my_data )
	my_data = re.sub(r' them ', r' ', my_data )
	my_data = re.sub(r' feel ', r' ', my_data )
	my_data = re.sub(r' see ', r' ', my_data )
	my_data = re.sub(r' than ', r' ', my_data )
	my_data = re.sub(r' then ', r' ', my_data )
	my_data = re.sub(r' now ', r' ', my_data )
	my_data = re.sub(r' look ', r' ', my_data )
	my_data = re.sub(r' only ', r' ', my_data )
	my_data = re.sub(r' come ', r' ', my_data )
	my_data = re.sub(r' think ', r' ', my_data )
	my_data = re.sub(r' also ', r' ', my_data )
	my_data = re.sub(r' back ', r' ', my_data )
	my_data = re.sub(r' after ', r' ', my_data )
	my_data = re.sub(r' how ', r' ', my_data )
	my_data = re.sub(r' our ', r' ', my_data )
	my_data = re.sub(r' well ', r' ', my_data )
	my_data = re.sub(r' way ', r' ', my_data )
	my_data = re.sub(r' want ', r' ', my_data )
	my_data = re.sub(r' because ', r' ', my_data )
	my_data = re.sub(r' use ', r' ', my_data )
	my_data = re.sub(r' any ', r' ', my_data )
	my_data = re.sub(r' these ', r' ', my_data )
	my_data = re.sub(r' one ', r' ', my_data )
	my_data = re.sub(r' two ', r' ', my_data )
	my_data = re.sub(r' three ', r' ', my_data )
	my_data = re.sub(r' once ', r' ', my_data )
	my_data = re.sub(r' since ', r' ', my_data )
	my_data = re.sub(r' give ', r' ', my_data )
	my_data = re.sub(r' first ', r' ', my_data )
	my_data = re.sub(r' second ', r' ', my_data )
	my_data = re.sub(r' third ', r' ', my_data )
	my_data = re.sub(r' new ', r' ', my_data )
	my_data = re.sub(r' page ', r' ', my_data )
	my_data = re.sub(r' call ', r' ', my_data )
	my_data = re.sub(r' tell ', r' ', my_data )
	my_data = re.sub(r' another ', r' ', my_data )
	my_data = re.sub(r' away ', r' ', my_data )
	my_data = re.sub(r' between ', r' ', my_data )
	my_data = re.sub(r' find ', r' ', my_data )
	my_data = re.sub(r' until ', r' ', my_data )
	my_data = re.sub(r' may ', r' ', my_data )
	my_data = re.sub(r' many ', r' ', my_data )
	my_data = re.sub(r' have ', r' ', my_data )
	my_data = re.sub(r' off ', r' ', my_data )
	my_data = re.sub(r' big ', r' ', my_data )
	my_data = re.sub(r' better ', r' ', my_data )
	my_data = re.sub(r' best ', r' ', my_data )
	my_data = re.sub(r' worse ', r' ', my_data )
	my_data = re.sub(r' worst ', r' ', my_data )
	my_data = re.sub(r' badge ', r' ', my_data )
	my_data = re.sub(r' never ', r' ', my_data )
	my_data = re.sub(r' ever ', r' ', my_data )
	my_data = re.sub(r' better ', r' ', my_data )
	my_data = re.sub(r' more ', r' ', my_data )
	my_data = re.sub(r' most ', r' ', my_data )
	my_data = re.sub(r' each ', r' ', my_data )
	my_data = re.sub(r' consistent ', r' ', my_data )
	my_data = re.sub(r' class ', r' ', my_data )
	my_data = re.sub(r' byline ', r' ', my_data )
	my_data = re.sub(r' heading ', r' ', my_data )
	my_data = re.sub(r' eachother ', r' ', my_data )
	my_data = re.sub(r' such ', r' ', my_data )
	my_data = re.sub(r' category ', r' ', my_data )
	my_data = re.sub(r' timely ', r' ', my_data )
	my_data = re.sub(r' info ', r' ', my_data )
	my_data = re.sub(r' date ', r' ', my_data )
	my_data = re.sub(r' comment ', r' ', my_data )
	my_data = re.sub(r' consistently ', r' ', my_data )
	my_data = re.sub(r' top ', r' ', my_data )
	my_data = re.sub(r' both ', r' ', my_data )
	my_data = re.sub(r' sir ', r' ', my_data )
	my_data = re.sub(r' mrs ', r' ', my_data )
	my_data = re.sub(r' miss ', r' ', my_data )
	
	#code syntax
	my_data = re.sub(r' head ', r' ', my_data )
	my_data = re.sub(r' blog ', r' ', my_data )
	my_data = re.sub(r' post ', r' ', my_data )
	my_data = re.sub(r' quot ', r' ', my_data )
	my_data = re.sub(r' nbsp ', r' ', my_data )
	my_data = re.sub(r' ref ', r' ', my_data )
	my_data = re.sub(r' http ', r' ', my_data )
	my_data = re.sub(r' name ', r' ', my_data )
	my_data = re.sub(r' www ', r' ', my_data )
	my_data = re.sub(r' org ', r' ', my_data )
	my_data = re.sub(r' edu ', r' ', my_data )
	my_data = re.sub(r' isbn ', r' ', my_data )
	my_data = re.sub(r' align ', r' ', my_data )
	my_data = re.sub(r' echo ', r' ', my_data )
	my_data = re.sub(r' rowspan ', r' ', my_data )
	my_data = re.sub(r' html ', r' ', my_data )
	my_data = re.sub(r' cite ', r' ', my_data )
	my_data = re.sub(r' url ', r' ', my_data )
	my_data = re.sub(r' htm ', r' ', my_data )
	my_data = re.sub(r' gif ', r' ', my_data )
	my_data = re.sub(r' jpg ', r' ', my_data )
	my_data = re.sub(r' png ', r' ', my_data )
	my_data = re.sub(r' txt ', r' ', my_data )
	my_data = re.sub(r' aspx ', r' ', my_data )
	my_data = re.sub(r' valign ', r' ', my_data )
	my_data = re.sub(r' div ', r' ', my_data )
	my_data = re.sub(r' cur ', r' ', my_data )
	my_data = re.sub(r' ldquo ', r' ', my_data )
	my_data = re.sub(r' rdquo ', r' ', my_data )
	my_data = re.sub(r' rsquo ', r' ', my_data )
	my_data = re.sub(r' chr ', r' ', my_data )
	my_data = re.sub(r' var ', r' ', my_data )
	my_data = re.sub(r' varchar ', r' ', my_data )
	my_data = re.sub(r' int ', r' ', my_data )
	my_data = re.sub(r' null ', r' ', my_data )
	my_data = re.sub(r' usigned ', r' ', my_data )
	my_data = re.sub(r' usigned ', r' ', my_data )
	my_data = re.sub(r' last ', r' ', my_data )
	my_data = re.sub(r' accessdate ', r' ', my_data )
	my_data = re.sub(r' title ', r' ', my_data )
	my_data = re.sub(r' com ', r' ', my_data )
	my_data = re.sub(r' font ', r' ', my_data )	
	my_data = re.sub(r' etc ', r' ', my_data )	
	my_data = re.sub(r' web ', r' ', my_data )
	my_data = re.sub(r' cnnblurbtxt ', r' ', my_data )

	#Months
	my_data = re.sub(r' jan ', r' ', my_data )
	my_data = re.sub(r' feb ', r' ', my_data )
	my_data = re.sub(r' mar ', r' ', my_data )
	my_data = re.sub(r' apr ', r' ', my_data )
	my_data = re.sub(r' may ', r' ', my_data )
	my_data = re.sub(r' jun ', r' ', my_data )
	my_data = re.sub(r' jul ', r' ', my_data )
	my_data = re.sub(r' aug ', r' ', my_data )
	my_data = re.sub(r' sep ', r' ', my_data )
	my_data = re.sub(r' sept ', r' ', my_data )
	my_data = re.sub(r' oct ', r' ', my_data )
	my_data = re.sub(r' nov ', r' ', my_data )
	my_data = re.sub(r' dec ', r' ', my_data )

	#randoms
	my_data = re.sub(r' xyz ', r' ', my_data )
	my_data = re.sub(r' bcc ', r' ', my_data )
	my_data = re.sub(r' wiki ', r' ', my_data )
	my_data = re.sub(r' non ', r' ', my_data )
	my_data = re.sub(r' amp ', r' ', my_data )
	my_data = re.sub(r'[ ]+', r' ', my_data )	
		
	#put the manipulated article back into the database
	cursor.execute (""" 
		UPDATE my_table SET old_text = %s
		WHERE old_id = %s
		""", (my_data, my_row))	

print "Done"
cursor.close ()
conn.commit ()
conn.close ()