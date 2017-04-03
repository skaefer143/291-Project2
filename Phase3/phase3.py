# CMPUT 291 - Mini Project 2
# Group 13 - Ken Li, Noah Kryzanowski, Storm Kaefer
# Phase 3
# Last Change By: Ken
# Time Changed: Apirl 2 - 2:03AM
# ----

from bsddb3 import db 
#Get an instance of BerkeleyDB
import xml.etree.ElementTree as ET
# import math

def XMLformatter(byteTweetXML):
	root = ET.fromstring(byteTweetXML)
	dateString = "Created on: " + root.find("created_at").text
	if dateString == None:
		dateString = '-Blank-'

	textString = root.find("text").text
	if textString == None:
		textString = '-Blank-'

	retweetString = "Retweets: " + root.find("retweet_count").text
	if retweetString == None:
		retweetString = '0'

	user = root.find("user")
	nameString = user.find("name").text
	if nameString == None:
		nameString = '-Blank-'

	locationString = user.find("location").text
	if locationString == None:
		locationString = '-Blank-'

	urlString = user.find("url").text
	if urlString == None:
		urlString = '-None-'

	return dateString + "\tTweet: " + textString + "\t\n" + retweetString + "\t Name: " + nameString + "\tLocation: " + locationString + "\tLink: " + urlString
	
	# Other way to print out, looks ugly though
	# for element in root.iter():
	# 	print(element.tag + " " + element.text, end=' ')
	# print()

def printResult(result):
	print("ID: " + result[0].decode("utf-8") + "\t" + XMLformatter(result[1]) +"\n")
	return

def intersectResults(termResults, multipleQueries):
	#Given results for each term, intersect the results to obtain the final result
	#termResults is a list of byte literal results, with termResults[0][0] containing the tweet ID,
	#and termResults[0][1] containing the result

	# DEBUGGING PRINTS
	# for queries in termResults:
	# 	for entries in queries:
	# 		print(entries)		

	if ((len(termResults) == 1 and len(termResults[0]) == 0) or (len(termResults) == 3 and len(termResults[0]) == 0 and len(termResults[1]) == 0 and len(termResults[2]) == 0)):
		print('\nNo results found.\n') 
	else:
		if multipleQueries > 1:
			# Find all ID that match all queries
			# Calculate how many times ID is found
			allID = {}
			for queries in termResults:
				for entries in queries:
					if entries[0] in allID:
						allID[entries[0]] += 1
					else:
						allID[entries[0]] = 1

			# Find all ID that match number of queries
			allIDMatching = []
			for key in allID:
				if allID[key] == multipleQueries:
					allIDMatching.append(key)

			if len(allIDMatching) > 0:
				print("\nResults:\n")
				# Print all results with duplicates
				alreadyDisplayed = []
				for term in termResults:
					for result in term:
						if result[0] in allIDMatching and result[0] not in alreadyDisplayed:
							alreadyDisplayed.append(result[0])
							printResult(result)
						#XMLformatter(result[1]) other way to print out, looks ugly though
			else:
				print('\nNo results found.\n') 
		else:
			print("\nResults:\n")
			alreadyDisplayed = []
			for term in termResults:
				for result in term:
					if result[0] not in alreadyDisplayed:
						alreadyDisplayed.append(result[0])
						printResult(result)

def searchByTerm(termQuery):
	# Search by a t- n- or l- term, with termQuery already encoded as a byte literal
	results = []

	# Look for term in text
	tweetID = termsCur.set(termQuery)
	if tweetID == None:
		#Term Not Found!
		return results
	# Get tweets using tweetID
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

def partialSearch(partialQuery, termType):
	# Search by a partial term, with partialQuery already encoded as a byte literal
	results = []
	resultlist = []
	#partialQuery = partialQuery.strip('%')
	#print(partialQuery)

	#Get start of tree
	current = termsCur.first()

	end = False
	if current == None:
		end = True

	temp = []
	#Appending the entire list of terms to be used to check partial
	while not end and current != None:
		temp.append(current)
		current = termsCur.next()

	#Check for partial matches
	# for term in temp:
	# 	if partialQuery in term[0] and termType in term[0]:
	# 		resultlist.append(term)

	for term in temp:
		if term[0].decode("utf-8").find("-"+partialQuery.decode("utf-8")) >= 0 and termType in term[0]:
			resultlist.append(term)
	
	for word in range(len(resultlist)):
		#term = resultlist[word]
		if word == None:
			# Next term not found, we're done
			break

		# Get tweets using tweetID
		tweetXML = tweetsCur.set(resultlist[word][1])
		if tweetXML == None:
			print("Couldn't find tweet id " + term[1].decode("utf-8") + " in tweets database.")
		else:
			results.append([tweetXML[0], tweetXML[1]])
	
	return results

def searchByDate(dateQuery):
	# Search by date, with dateQuery already encoded as a byte literal
	results = []

	# Look for date in date
	tweetID = dateCur.set(dateQuery)

	if tweetID == None:
		#Date Not Found!
		return results

	# print("\ncount: " + str(dateCur.count()))

	# Get tweets using tweetID
	tweetXML = tweetsCur.set(tweetID[1])
	if tweetXML == None:
		print("Couldn't find tweet id " + tweetID[1].decode("utf-8") + " in tweets database.")
	else:
		results.append([tweetXML[0], tweetXML[1]])

	while True:
		tweetID = dateCur.next_dup()
		if tweetID == None:
			# Next term not found, we're done
			break

		# Get tweets using tweetID
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
		print('\nIncorrect Input, Please try again.\n')
		continue

	# Check each query split by spaces
	userInputTerms = userInput.split(' ')
	termResults = []

	multipleQueries = len(userInputTerms)

	correctInput = True

	for term in userInputTerms:
		fullMatch = 0
		partMatch = 0
		rangeMatch = 0

		# Check each character in term
		for char in term:
			if char == ':':
				fullMatch += 1
			if char in ('<', '>'):
				rangeMatch += 1
			if char in ('%'):
				partMatch += 1

		# Term contains more than 1 ':' and/or '<' or '>' and/or '%'
		if (partMatch > 1 or fullMatch > 1 or rangeMatch > 1):
			print('\nIncorrect Input "' +  term + '", Please try again.\n')
			correctInput = False

		# Term is full match and range match 
		elif (fullMatch + rangeMatch) == 2:
			print('\nIncorrect Input "' +  term + '", Please try again.\n')
			correctInput = False

		# Full Match "CONDITION:TERM"
		elif (fullMatch and not partMatch):
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
				print('\nIncorrect Input "' +  userInputFormatted[0] + '", Please try again.\n')
				correctInput = False
				continue

		# Partial Match "(TEXT/NAME/LOCATION):TERM%"
		elif (fullMatch and partMatch):
			partialResults = []
			#print('\nPART MATCH\n')
			for char in term:
				if char == '%':
					userInputFormatted = term.split(':')
			if userInputFormatted[0] == 'text':
				partialQuery = str.encode(userInputFormatted[1].strip('%'))
				termType = str.encode('t-')
				termResults.append(partialSearch(partialQuery, termType))
			elif userInputFormatted[0] == 'name':
				partialQuery = str.encode(userInputFormatted[1].strip('%'))
				termType = str.encode('n-')
				termResults.append(partialSearch(partialQuery, termType))
			elif userInputFormatted[0] == 'location':
				partialQuery = str.encode(userInputFormatted[1].strip('%'))
				termType = str.encode('l-')
				termResults.append(partialSearch(partialQuery, termType))
			else:
				print('\nIncorrect Input "' +  userInputFormatted[0] + '", Please try again.\n')
				continue

		# Partial Match "TERM%"
		elif partMatch and not fullMatch:
			partialResults = []
			#print('\nPART MATCH\n')
			partialQuery = str.encode(term.strip('%'))
			termType = str.encode('-')
			termResults.append(partialSearch(partialQuery, termType))

		# Range Match "DATE(</>)__DATE__"
		elif (rangeMatch and (partMatch + fullMatch) == 0):
			lessThan = False
			greaterThan = False
			
			# Split query at < or >
			for char in term:
				if char == '<':
					userInputFormatted = term.split('<')
					lessThan = True
					break
				elif char == '>':
					userInputFormatted = term.split('>')
					greaterThan = True
					break

			# Can only do range search on date
			if userInputFormatted[0] == 'date':
				if lessThan:
					# IGNORE THIS, TRIED TO DO BINARY SEARCH
					# dateDBInfo = dateDatabase.stat()
					# uniqueKeys = dateDBInfo['nkeys']
					# middle = math.floor(uniqueKeys/2)

					# Convert user input yyyy/mm/dd to yyyymmdd
					userInput = userInputFormatted[1]

					# Check if input was correct
					if len(userInput) == 10:
						# Convert user input to int
						userInput = int(userInput.replace('/',''))

						# Start at beginning of tree
						current = dateCur.first()

						# End of tree
						end = False
						if current == None:
							end = True

						# Convert current date to int(yyyymmdd)
						date = int(current[0].decode("utf-8").replace('/',''))

						temp = []

						while date < userInput and not end:
							tweetXML = tweetsCur.set(current[1])
							if tweetXML == None:
								print("Couldn't find tweet id " + current[1].decode("utf-8") + " in tweets database.")
							else:
								temp.append([tweetXML[0], tweetXML[1]])

							while True:
								current = dateCur.next_dup()
								if current == None:
									break

								tweetXML = tweetsCur.set(current[1])
								if tweetXML == None:
									print("Couldn't find tweet id " + current[1].decode("utf-8") + " in tweets database.")
								else:
									temp.append([tweetXML[0], tweetXML[1]])

							# Get next date
							current = dateCur.next()
							if current == None:
								end = True
							else:
								date = int(current[0].decode("utf-8").replace('/',''))

						termResults.append(temp)

					else:
						print('Wrong date format, Please try again.')

				elif greaterThan:
					# Convert user input yyyy/mm/dd to yyyymmdd
					userInput = userInputFormatted[1]

					# Check if input was correct
					if len(userInput) == 10:
						# Convert user input to int
						userInput = int(userInput.replace('/',''))

						# Start at beginning of tree
						current = dateCur.first()

						# End of tree
						end = False
						if current == None:
							end = True

						# Convert current date to int(yyyymmdd)
						date = int(current[0].decode("utf-8").replace('/',''))

						temp = []

						while not end:
							if date > userInput:
								tweetXML = tweetsCur.set(current[1])
								if tweetXML == None:
									print("Couldn't find tweet id " + current[1].decode("utf-8") + " in tweets database.")
								else:
									temp.append([tweetXML[0], tweetXML[1]])

								while True:
									current = dateCur.next_dup()
									if current == None:
										break

									tweetXML = tweetsCur.set(current[1])
									if tweetXML == None:
										print("Couldn't find tweet id " + current[1].decode("utf-8") + " in tweets database.")
									else:
										temp.append([tweetXML[0], tweetXML[1]])

							# Get next date
							current = dateCur.next()
							if current == None:
								end = True
							else:
								date = int(current[0].decode("utf-8").replace('/',''))

						termResults.append(temp)

					else:
						print('Wrong date format, Please try again.')
			# Not date
			else:
				print('\nCannot do range search on "' +  userInputFormatted[0] + '". Please try again.\n')
				correctInput = False

		# All 3
		elif (fullMatch + partMatch + rangeMatch) == 0:
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

		# Wrong input
		else:
			print('\nIncorrect Input "' +  userInputFormatted[0] + '", Please try again.\n')
			correctInput = False

	if correctInput:
		intersectResults(termResults, multipleQueries) #To find final result
