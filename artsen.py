#coding: utf-8
from bottle import route, error, post, get, run, static_file, abort, redirect, response, request, template
import urllib2
import re
import MySQLdb
my_url = ""

@route('/')
@route('/index.html')
def index():
	#return '<a href="/upload">Welcome to ArticleSense</a>'
	return template('results', data = "")

@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='/home/pagrawal/demo/')
	
@route('/output')
def serve_static():
	return static_file('output.txt', root='/home/pagrawal/demo/Input/')

@route('/words')
def serve_static():
	return static_file('words.txt', root='/home/pagrawal/demo/Input/')

@error(404)
def error404(error):
	return 'Nothing Here, Try Again'

###
#	Check to see if Article is already in cache
###
@route('/cache')
def check(url):
	#connect to the database
	conn = MySQLdb.connect (host = "localhost", 
							user = "pagrawal", 
							passwd = "mypw", 
							db = "my_wiki")
	cursor = conn.cursor ()
	
	#check if URL inputted is in cache
	cursor.execute ("""select output from my_cache where url like %s;""",
			(url))
	list = cursor.fetchall()
		
	#no it hasn't...
	if(len(list) == 0):
		return 0
	#yes it has...
	else:
		return 1
	
@get('/upload')
def upload_view():
	return template('results', data = "")

###
#	Check cache. If not in cache, then find article submitted, caclulate similar articles and then display them.
###	
@post('/upload')
def do_upload():
	#get url
	url = request.forms.get('my_url')
	if(url == ""):
		redirect("/upload")
	global my_url
	my_url = url
	
	#check if url has been already submitted:
	if(check(url) == 1):		
		#connect to the database
		conn = MySQLdb.connect (host = "localhost", 
								user = "pagrawal", 
								passwd = "mypw", 
								db = "my_wiki")
		cursor = conn.cursor ()
		#get all entries related to URL
		cursor.execute ("""select rank, output from my_cache where url like %s order by rank asc;""",
			(url))
		list = cursor.fetchall()
		my_rank = list[0]
		my_output = list[1]
		
		#return values in cache
		output = ""
		for element in list:
			output += str(element[1])
		
		final = '<table border="0">' + output + '</table>'
		return template('results', data = final)
	#if the url has not been submitted before:
	else:
		return alt()
	
@get('/upvote')
def upvote_view():
	return template('results', data = "")

###
#	Vote articles vs contextual topic based on user rating
###
@post('/vote')
def do_vote():
	import MySQLdb
	#connect to the database
	conn = MySQLdb.connect (host = "localhost", 
							user = "pagrawal", 
							passwd = "mypw", 
							db = "my_wiki")
	cursor = conn.cursor ()

	#figure out if the request is for upvotes or downvotes
	one = request.forms.get('UP')
	two = request.forms.get('DOWN')
	
	#get the most frequent words in the article
	words = open('/home/pagrawal/demo/Input/words.txt',"r").read()
	my_words = words.split(';')
	my_words.pop(-1)
	
	#clear cache for that url
	cursor.execute ("""DELETE FROM my_cache WHERE url = %s;""", (my_url))
	
	#Upvotes -- add 1 to the value stored in the feedback table
	if(one != None):
		for x in my_words:
			cursor.execute ("""select score from my_feedback where id = %s and word = %s;""",
				(one, x))
			list = cursor.fetchall()
			if(len(list) == 0):
				score = 0
			else:
				score = float(list[0][0])
			cursor.execute ("""UPDATE my_feedback SET score = %s where id = %s and word = %s;""", 
			((score+1),one, x))		
	#Downvotes -- substract 1 to the value stored in the feedback table
	else:
		for x in my_words:
			cursor.execute ("""select score from my_feedback where id = %s and word = %s;""",
				(two, x))
			list = cursor.fetchall()
			if(len(list) == 0):
				score = 0
			else:
				score = float(list[0][0])
			cursor.execute ("""UPDATE my_feedback SET score = %s where id = %s and word = %s;""", 
			((score-1),two, x))
	
	#redirect("/upload")
	return alt()

###
#	Find, calcualte and Display articles results 
###
@route('/alt')
def alt():
	import MySQLdb
	#connect to the database
	conn = MySQLdb.connect (host = "localhost", 
							user = "pagrawal", 
							passwd = "mypw", 
							db = "my_wiki")
	cursor = conn.cursor ()
	#open web page and get text
	page = urllib2.urlopen(my_url)
	my_page = page.read()

	#get all <p>
	all_text = re.findall(r'<p(?:[^>]*)>(?:[^<]*)<\/p>', my_page)
	alt_text = ""
	for x in all_text:
		x = re.sub(r'<p(?:[^>]*)>', r' ', x)
		x = re.sub(r'<\/p>', r' ', x)
		alt_text += x + " "
	o = open('/home/pagrawal/demo/Input/input.txt',"w")
	o.write(alt_text)
	o.close()
	
	#run ArticleSense
	execfile("/home/pagrawal/demo/Input/overview.py")

	#output from ArticleSense
	output = open('/home/pagrawal/demo/Input/output.txt',"r").read()	
	lines = output.split('\n')
	lines.pop(-1)
	final = ""
	for x in lines:
		words = x.split(';')
		
		#get all the text from the output
		cursor.execute ("""select old_text from my_text where old_id = %s;""",
			(str(words[3])))
		list = cursor.fetchall()
		text = list[0]
		
		#remove extraneous data
		my_sentence = re.sub(r' {{(Infobox .*) }} The ', r' ', text[0])
		my_sentence = re.sub(r'\|(birth_place = .*) }} \'\'', r'', my_sentence)
		my_sentence = re.sub(r'\|(birth_place = .*) }} \'\'\'', r'', my_sentence)
		testing = re.findall(r'birth_place', my_sentence)
		
		my_sentence = re.sub(r'\{\{(.*?)\}\}', r'', my_sentence)
		my_sentence = re.sub(r'\[\[Image:(.*?)\]\]', r'', my_sentence)
		my_sentence = re.sub(r'\[\[Category:(.*?)\]\]', r'', my_sentence)
		my_sentence = re.sub(r'\[\[File:(.*?)\]\]', r'', my_sentence)
		my_sentence = re.sub(r'[\[]*', r'', my_sentence)
		my_sentence = re.sub(r'[\]]*', r'', my_sentence)
		my_sentence = re.sub(r'<!--', r'', my_sentence)
		
		#article preview
		sentence = my_sentence.split()			
		my_text = ""
		if(len(testing) == 0):
			for y in range(len(sentence)):
				if(y <= 55):
					my_text += sentence[y] + " "
				else:
					break
		else:
			for y in range(len(sentence)):	
				if(y >= 130):
					my_text += sentence[y] + " "
				if(y == len(sentence) or y == 185):
					break
		
		# get all the data related to an article printout and cache it
		cache_output = '<tr><td>' + str(words[0]) +' <a href="' +  str(words[2]) + '">' +  str(words[1]) +' </a>' + '<p><font size="1">'+ str(my_text) +'</font></p><br></td>'
		cache_output = cache_output + '<td><form action="/vote" method="post"><button name="UP" type="submit" value="' + words[3] + '"><img width="25" height="25" src="/static/upvote.png" /></button><button name="DOWN" type="submit" value="' + words[3] + '"><img width="25" height="25" src="/static/downvote.png" /></button></form></td></tr>'
		#cache_output = '<tr><td>' + '<form action="/vote" method="post"><button name="UP" type="submit" value="' + words[3] + '"><img width="25" height="25" src="/static/upvote.png" /></button><button name="DOWN" type="submit" value="' + words[3] + '"><img width="25" height="25" src="/static/downvote.png" /></button></form></td>'
		#cache_output = cache_output + '<td>' + str(words[0]) + '<a href="' +  str(words[2]) + '">' +  str(words[1]) +' </a>' + '<p><font size="1">'+ str(my_text) +'</font></p><br></td></tr>'		
		
		cursor.execute (""" INSERT INTO my_cache (url, rank, output) VALUES (%s, %s, %s) """, 
			(my_url, words[0], cache_output))
		final = final + cache_output
	
	#output all data to GUI
	final = '<table border="0">' + final + '</table>'
	return template('results', data = final)

run(host='0.0.0.0', port=9080)
