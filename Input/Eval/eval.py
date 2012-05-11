#! /usr/bin/env python
import re

var = raw_input("Enter rating of articles (1-10): ")
val = int(var)
tot = 0.0
curr = 0.0
while(val != -1):
	#good results -- get one point
	if(val >6 and val <=10):
		curr = curr + 1
	#average results -- get half of a point
	elif(val >3 and val <=6):
		curr = curr + 0.5
	#bad results -- get zero points
	tot = tot + 1
	if(tot%10 == 0):
		print curr, tot
	print float(curr)/float(tot)
	var = raw_input("Enter rating of articles (1-10): ")
	#print current statistic
	if(var == "all"):
		print curr, tot
		var = raw_input("Enter rating of articles (1-10): ")
	#If booted out of system, reset to last known values
	if(var == "add"):
		var = raw_input("New Tot: ")
		tot = int(var)		
		var = raw_input("New Curr: ")
		current = int(var)
		var = raw_input("Enter rating of articles (1-10): ")
	val = int(var)
print (curr/tot), curr, tot
