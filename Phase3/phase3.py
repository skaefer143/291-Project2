# CMPUT 291 - Mini Project 2
# Group 13 - Ken Li, Noah Kryzanowski, Storm Kaefer
# Phase 3
# Last Change By: Ken
# Time Changed: 4:13 PM
# ----

from bsddb3 import db 
#Get an instance of BerkeleyDB
import xml.etree.ElementTree as ET

def XMLformatter(byteTweetXML):
	root = ET.fromstring(byteTweetXML)
	dateString = "Created on: " + root.find("created_at").text
	textString = root.find("text").text
	retweetString = "Retweets: " + root.find("retweet_count").text
	user = root.find("user")
	nameString = user.find("name").text
	locationString = user.find("location").text
	urlString = user.find("url").text

	return dateString + "\t" + textString + "\t\n" + retweetString + "\t" + nameString + "\t" + locationString + "\t" + urlString
	
	# Other way to print out, looks ugly though
	# for element in root.iter():
	# 	print(element.tag + " " + element.text, end=' ')
	# print()

def printResult(result):
	print("ID: " + result[0].decode("utf-8") + "\t" + XMLformatter(result[1]) +"\n")
	return

def intersectResults(termResults):
	#Given results for each term, intersect the results to obtain the final result
	#termResults is a list of byte literal results, with termResults[0][0] containing the tweet ID,
	#and termResults[0][1] containing the result
	
	if ((len(termResults) == 1 and len(termResults[0]) == 0) or (len(termResults) == 3 and len(termResults[0]) == 0 and len(termResults[1]) == 0 and len(termResults[2]) == 0)):
		print('\nNo results found.\n') 
	else:
		print("\nResults:\n")
		for term in termResults:
			for result in term:
				printResult(result)
				#XMLformatter(result[1]) other way to print out, looks ugly though

def searchByTerm(termQuery):
	# Search by a t- n- or l- term, with termQuery already encoded as a byte literal
	results = []

	# Look for term in text
	tweetID = termsCur.set(termQuery)
	if tweetID == None:
		#Term Not Found!
		return results
	#get tweets using tweetID
	tweetXML = tweetsCur.set(tweetID[1])
	if tweetXML == None:
		print("\nCouldn't find tweet id " + tweetID[1].decode("utf-8") + " in tweets database.\n")
	else:
		results.append([tweetXML[0], tweetXML[1]])

	while True:
		tweetID = termsCur.next_dup()
		if tweetID == None:
			#next term not found, we're done
			break
		#get tweets using tweetID
		tweetXML = tweetsCur.set(tweetID[1])
		if tweetXML == None:
			print("\nCouldn't find tweet id " + tweetID[1].decode("utf-8") + " in tweets database.\n")
		else:
			results.append([tweetXML[0], tweetXML[1]])
	return results

def searchByDate(dateQuery):
	# Search by date, with termQuery already encoded as a byte literal
	results = []

	# Look for term in text
	tweetID = dateCur.set(dateQuery)
	if tweetID == None:
		#Date Not Found!
		return results
	# print("\ncount: " + str(dateCur.count()))
	#get tweets using tweetID
	tweetXML = tweetsCur.set(tweetID[1])
	if tweetXML == None:
		print("Couldn't find tweet id " + tweetID[1].decode("utf-8") + " in tweets database.")
	else:
		results.append([tweetXML[0], tweetXML[1]])

	while True:
		tweetID = dateCur.next_dup()
		if tweetID == None:
			#next term not found, we're done
			break
		#get tweets using tweetID
		tweetXML = tweetsCur.set(tweetID[1])
		if tweetXML == None:
			print("Couldn't find tweet id " + tweetID[1].decode("utf-8") + " in tweets database.")
		else:
			results.append([tweetXML[0], tweetXML[1]])
	return results

def exitProgram():
	#close up everything
	tweetsCur.close()
	termsCur.close()
	dateCur.close()
	tweetsDatabase.close()
	termsDatabase.close()
	dateDatabase.close()
	exit()

#open everything 
tweetsDatabase = db.DB() 
tweetsDatabase.open("tw.idx")
termsDatabase = db.DB() 
termsDatabase.open("te.idx")
dateDatabase = db.DB() 
dateDatabase.open("da.idx")

tweetsCur = tweetsDatabase.cursor() 
termsCur = termsDatabase.cursor() 
dateCur = dateDatabase.cursor()


while True:
	print('-'*20)
	userInput = input("Please type your query or '\exit' to exit: ").lower()
	print('-'*20)

	# Exit
	if userInput == '\exit':
		exitProgram()

	valid = True
	for char in userInput:
		if char.isalnum() or char in (':','<','>','%', ' ', '/' , '_'):
			continue
		else:
			valid = False
			break

	if not valid:
		print('\nIncorrect Input, Please Try Again.\n')
		continue

	# Check each query split by spaces
	userInputTerms = userInput.split(' ')
	termResults = []

	for term in userInputTerms:
		fullMatch = 0
		partMatch = 0
		rangeMatch = 0
		correctInput = True

		# Check each character in term
		for char in term:
			if char == ':':
				fullMatch += 1
			if char in ('<', '>'):
				rangeMatch += 1
			if char in ('%'):
				partMatch += 1

		# Term contains ':' and/or '<' or '>' and/or '%'
		if ((partMatch and fullMatch) or (partMatch and rangeMatch) or (fullMatch and rangeMatch)) :
			print('\nIncorrect Input "' +  term + '", Please Try Again.\n')
			correctInput = False

		# Term contains more than 1 ':' and/or '<' or '>' and/or '%'
		elif (partMatch > 1 or fullMatch > 1 or rangeMatch > 1):
			print('\nIncorrect Input "' +  term + '", Please Try Again.\n')
			correctInput = False

		# Full Match "CONDITION:TERM"
		elif fullMatch:
			# Split query at ':'
			userInputFormatted = term.split(':')

			if userInputFormatted[0] == "text":
				termQuery = str.encode("t-"+userInputFormatted[1])
				termResults.append(searchByTerm(termQuery))

			elif userInputFormatted[0] == "name":
				termQuery = str.encode("n-"+userInputFormatted[1])
				termResults.append(searchByTerm(termQuery))

			elif userInputFormatted[0] == "location":
				termQuery = str.encode("l-"+userInputFormatted[1])
				termResults.append(searchByTerm(termQuery))

			elif userInputFormatted[0] == 'date':
				dateQuery = str.encode(userInputFormatted[1])
				termResults.append(searchByDate(dateQuery))
			else:
				print('\nIncorrect Input "' +  userInputFormatted[0] + '", Please Try Again.\n')
				correctInput = False
				continue

		# Partial Match
		elif partMatch:
			print('\nPART MATCH\n')

		# Range Match
		elif rangeMatch:
			print('\nRANGE MATCH\n')

		# All 3
		else:
			#search by everything with userInputFormatted[0]
			#text
			termQuery = str.encode("t-"+term)
			termResults.append(searchByTerm(termQuery))
			#name
			termQuery = str.encode("n-"+term)
			termResults.append(searchByTerm(termQuery))
			#location
			termQuery = str.encode("l-"+term)
			termResults.append(searchByTerm(termQuery))

	if correctInput:
		intersectResults(termResults) #To find final result