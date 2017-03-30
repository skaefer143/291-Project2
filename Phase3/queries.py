from bsddb3 import db 
#Get an instance of BerkeleyDB

def searchByTerm(termQuery):
	# Search by a t- n- or l- term, with termQuery already encoded as a byte literal
	results = []

	# Look for term in text
	tweetID = termsCur.set(termQuery)
	if tweetID == None:
		print("Term Not Found!")
		return
	print("count: " + str(termsCur.count()))
	print(tweetID)

	#get tweets using tweetID
	tweetXML = tweetsCur.set(tweetID[1])
	if tweetXML == None:
		print("Couldn't find tweet id " + tweetID[1].decode("utf-8") + " in tweets database.")
	else:
		results.append(tweetXML[1].decode("utf-8"))

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
			results.append(tweetXML[1].decode("utf-8"))

	print("Results:\n" + str(results))
	return


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
	# subqueries are separated by a ' '

	for term in userInputTerms:
		userInputFormatted = term.split(':')
		# get first term by splitting with ':'

		print("First term: " + userInputFormatted[0])

		if userInputFormatted[0] == "text":
			termQuery = str.encode("t-"+userInputFormatted[1])
			searchByTerm(termQuery)

		if userInputFormatted[0] == "name":
			termQuery = str.encode("n-"+userInputFormatted[1])
			searchByTerm(termQuery)

		if userInputFormatted[0] == "location":
			termQuery = str.encode("l-"+userInputFormatted[1])
			searchByTerm(termQuery)



#close up everything
tweetsCur.close()
termsCur.close()
dateCur.close()
tweetsDatabase.close()
termsDatabase.close()
dateDatabase.close()