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
	print("Results:")
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
	print("count: " + str(termsCur.count()))
	#get tweets using tweetID
	tweetXML = tweetsCur.set(tweetID[1])
	if tweetXML == None:
		print("Couldn't find tweet id " + tweetID[1].decode("utf-8") + " in tweets database.")
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
	userInput = input("Please type your query: ").lower()

	userInputTerms = userInput.split(' ')
	termResults = []
	# subqueries are separated by a ' '

	for term in userInputTerms:
		userInputFormatted = term.split(':')
		# get first term by splitting with ':'

		if userInputFormatted[0] == "text":
			termQuery = str.encode("t-"+userInputFormatted[1])
			termResults.append(searchByTerm(termQuery))

		elif userInputFormatted[0] == "name":
			termQuery = str.encode("n-"+userInputFormatted[1])
			termResults.append(searchByTerm(termQuery))

		elif userInputFormatted[0] == "location":
			termQuery = str.encode("l-"+userInputFormatted[1])
			termResults.append(searchByTerm(termQuery))

		elif userInputFormatted[0] == "\exit":
			exitProgram()

		else:
			#search by everything with userInputFormatted[0]
			#text
			termQuery = str.encode("t-"+userInputFormatted[0])
			termResults.append(searchByTerm(termQuery))
			#name
			termQuery = str.encode("n-"+userInputFormatted[0])
			termResults.append(searchByTerm(termQuery))
			#location
			termQuery = str.encode("l-"+userInputFormatted[0])
			termResults.append(searchByTerm(termQuery))




	intersectResults(termResults) #To find final result