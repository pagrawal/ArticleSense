Pooja Agrawal
Senior Design 2011-2012

System Requirements:

In order to run the code, the system needs Python2.7, WordNet Language Toolkit, Bottle 
(a python web framework), and a MySQL database. Python uses many libraries (MySQLdb, 
math, collections, sys, and operator).

System Contents:

ArticleSense -
 artsen.py - 
	- This is our GUI. We can access the GUI by "http://savannah.cs.gwu.edu:9080/"
	- Contains cache: Accesses and adds to cache.
	- Feedback: Takes upvotes and downvotes from user.

 Input/ -
	sync.py - 
		- Synchronizes all word tenses
	scanner -
		- Removes all stop words
	tfidf.py -
		- Calculates the high frequency words in the given article
	fetch.py -
		- Finds articles from the databasethat share any attribute with the input
	output.py -
		- Calculates the relevancy of each articles and 
	overview.py -
		- Integrates all modules
	Eval/ -
		eval.py - 
			- Assists in evaluating the system

 System/ -
	sync.py - 
		- Synchronizes all word tenses for each article in the database 
	scanner -
		- Removes all stop words for each article in the database
	aggregator.py - 
		- Get the high frequency words for each article in the database
	preprocess.py - 
		- Setting up database for TF-IDF
	