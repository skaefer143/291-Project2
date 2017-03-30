from bsddb3 import db 
#Get an instance of BerkeleyDB

def searchByTerm(userInputFormatted):
	if userInputFormatted[0] == "text":
		# Look for term in text
		iter = termsCur.first()
		while iter:
			print(iter[0].decode("utf-8") + "\t\t" + iter[1].decode("utf-8"))
			iter = termsCur.next()

		tweetID = termsCur.get(str.encode("t-"+userInputFormatted[1]), db.DB_FIRST)
		if tweetID == None:
			print("not found!")
		print("count: " + str(termsCur.count()))
		print(tweetID)
		#tweetXML = tweetsDatabase.get(tweetID)

		while True:
			tweetID = termsCur.next_dup()
			if tweetID == None:
				print("not found!")
				break
			print(tweetID)
			#tweetXML = tweetsDatabase.get(tweetID)

	if userInputFormatted[0] == "name":
		# Look for term in name
		tweetID = termsDatabase.get("n-"+userInputFormatted[1])
	if userInputFormatted[0] == "location":
		# Look for term in location
		tweetID = termsDatabase.get("l-"+userInputFormatted[1])

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
			searchByTerm(userInputFormatted)

		if userInputFormatted[0] == "name":
			searchByTerm(userInputFormatted)

		if userInputFormatted[0] == "location":
			searchByTerm(userInputFormatted)



#close up everything
tweetsCur.close()
termsCur.close()
dateCur.close()
tweetsDatabase.close()
termsDatabase.close()
dateDatabase.close()