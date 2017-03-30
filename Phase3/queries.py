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


def intersectResults(termResults):
	#Given results for each term, intersect the results to obtain the final result
	#termResults is a list of byte literal results, with termResults[0][0] containing the tweet ID,
	#and termResults[0][1] containing the result
	print("Results:")
	for term in termResults:
		for results in term:
			print("ID: " + results[0].decode("utf-8") + "\t" + XMLformatter(results[1]))


def searchByTerm(termQuery):
	# Search by a t- n- or l- term, with termQuery already encoded as a byte literal
	results = []

	# Look for term in text
	tweetID = termsCur.set(termQuery)
	if tweetID == None:
		print("Term Not Found!")
		return results
	print("count: " + str(termsCur.count()))
	print(tweetID)

	#get tweets using tweetID
	tweetXML = tweetsCur.set(tweetID[1])
	if tweetXML == None:
		print("Couldn't find tweet id " + tweetID[1].decode("utf-8") + " in tweets database.")
	else:
		results.append([tweetXML[0], tweetXML[1]])

	while True:
		tweetID = termsCur.next_dup()
		if tweetID == None:
			break
		print(tweetID)

		#get tweets using tweetID
		tweetXML = tweetsCur.set(tweetID[1])
		if tweetXML == None:
			print("Couldn't find tweet id " + tweetID[1].decode("utf-8") + " in tweets database.")
		else:
			results.append([tweetXML[0], tweetXML[1]])

	return results


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

		print("First term: " + userInputFormatted[0])

		if userInputFormatted[0] == "text":
			termQuery = str.encode("t-"+userInputFormatted[1])
			termResults.append(searchByTerm(termQuery))

		elif userInputFormatted[0] == "name":
			termQuery = str.encode("n-"+userInputFormatted[1])
			termResults.append(searchByTerm(termQuery))

		elif userInputFormatted[0] == "location":
			termQuery = str.encode("l-"+userInputFormatted[1])
			termResults.append(searchByTerm(termQuery))

		#else:
			#search by term with userInputFormatted[0]



	intersectResults(termResults) #To find final result






#close up everything
tweetsCur.close()
termsCur.close()
dateCur.close()
tweetsDatabase.close()
termsDatabase.close()
dateDatabase.close()