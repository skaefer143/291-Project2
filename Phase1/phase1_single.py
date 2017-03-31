# CMPUT 291 - Mini Project 2
# Group 13 - Ken Li, Noah Kryzanowski, Storm Kaefer
# Phase 1
# Last Change By: Ken
# Time Changed: March 31, 12:20 AM
# ----
def main():
	# Loop till file opened correctly
	correctFile = False
	while not correctFile:
		# userInput = input("Enter a input file (with file extension) or 'exit' to exit: ")
		userInput = '10000.txt' # HARDCODE ------------------------------------------------------
		if userInput.upper() == 'EXIT':
			print("\nProgram exiting.\n")	
			exit()
		try:
			inputFile = open(userInput)
			correctFile = True
		except:
			print("\nCannot open file, please try again.\n")
	
	termsOutput = open('terms.txt', 'w')
	tweetsOutput = open("tweets.txt", "w")
	datesOutput = open("dates.txt", "w")

	# ---- TERMS ----

	loopCounter = 0
	line = inputFile.readline()
	# Loop for each line
	while line:
		idFound = False
		dateFound = False
		termsStarted = False
		nameStarted = False
		locationStarted = False

		words = []
		names = []
		locations = []

		# Skip the first 2 lines
		if loopCounter > 1:
			temp = ''
			for char in line:
				# Get each chunk of text split by a space
				if char != ' ': temp += char

				# Parse the chunk of text
				else:
					# Check if tag is <id>
					if not idFound and temp[0:4] == '<id>':
						# Get ID till </id>
						id = ''
						for i in range(4, len(temp)):
							char = temp[i]
							# Reached </id>
							if temp[i:i+5] == '</id>':
								idFound = True
								break
							else:
								id += char

					elif not dateFound and temp[0:12] == '<created_at>':
						# Get Date till </created_at>
						date = ''
						for i in range(12, len(temp)):
							char = temp[i]
							# Reached </created_at>
							if temp[i:i+13] == '</created_at>':
								dateFound = True
								break
							else:
								date += char

					# Check if tag is <text> or between <text> and </text>
					elif (termsStarted or temp[0:6] == '<text>'):
						termsStarted = True
						temp += ' '
						# Get terms
						word = ''
						prev = ''

						for i in range(len(temp)):
							# Skip <text>
							if (temp[0:6] == '<text>' and i < 6):
								continue
							# Get each character in chunk
							char = temp[i].lower()

							# Reached </text>
							if temp[i:i+7] == '</text>':
								# Save last word
								if len(word) > 2:
									words.append(word)
								word = ''
								termsStarted = False
								break

							# If character is [0-9a-zA-Z_] or '&', '#'
							elif char.isalnum() or char in ('&','#','_'):
								# Save 'aaa' for 'aaa&(#)bbb;ccc' case
								if char == '&':
									if len(word) > 0:
										prev = word
										word = ''
									word += char

								# 2 Cases with '#', "hashtag" and between strings
								elif char == '#':
									# Remove '#' from case '#aaa'
									if word == '':
										continue
									# Append char if current word is '&'
									elif word == '&':
										word += char
									# Save 'aaa' from '(#)aaa#bbb' case and start bbb
									elif len(word) > 2:
										words.append(word)
										word = ''
								# Alphanumeric or _
								else:
									word += char

							# 2 Cases with ';' - '&#number;' and '&number;'
							elif char == ';':
								if len(word) > 2 and word[0:2] == '&#':
									# Restore 'aaa' for 'aaa&#bbb;ccc'
									if len(prev) > 0:
										word = prev
										prev = ''
									# No previous string, ignore '&#aaa;'
									else:
										word = ''

								elif len(word) > 0 and word[0] == '&':
									# Save 'aaa' for 'aaa&bbb;ccc'
									if len(prev) > 2:
										words.append(prev)
									prev = ''

									# Save 'aaa' from '&aaa;'
									if len(word) > 2:
										words.append(word[1:])
									word = ''

								else:
									if len(word) > 2:
										words.append(word)
									word = ''

							# Not alphanumeric or '&' or '#'
							else:
								if len(word) > 2:
									words.append(word)
								word = ''

					# Check if tag is <name> or between <name> and </name>
					elif (nameStarted or temp[0:6] == '<name>'):
						nameStarted = True
						temp += ' '
						# Get terms
						word = ''
						prev = ''

						for i in range(len(temp)):
							# Skip <name>
							if (temp[0:6] == '<name>' and i < 6):
								continue
							# Get each character in chunk
							char = temp[i].lower()

							# Reached </name>
							if temp[i:i+7] == '</name>':
								# Save last word
								if len(word) > 2:
									names.append(word)
								word = ''
								nameStarted = False
								break

							# If character is [0-9a-zA-Z_] or '&', '#'
							elif char.isalnum() or char in ('&','#','_'):
								# Save 'aaa' for 'aaa&(#)bbb;ccc' case
								if char == '&':
									if len(word) > 0:
										prev = word
										word = ''
									word += char

								# 2 Cases with '#', "hashtag" and between strings
								elif char == '#':
									# Remove '#' from case '#aaa'
									if word == '':
										continue
									# Append char if current word is '&'
									elif word == '&':
										word += char
									# Save 'aaa' from '(#)aaa#bbb' case and start bbb
									elif len(word) > 2:
										names.append(word)
										word = ''
								# Alphanumeric or _
								else:
									word += char

							# 2 Cases with ';' - '&#number;' and '&number;'
							elif char == ';':
								if len(word) > 2 and word[0:2] == '&#':
									# Restore 'aaa' for 'aaa&#bbb;ccc'
									if len(prev) > 0:
										word = prev
										prev = ''
									# No previous string, ignore '&#aaa;'
									else:
										word = ''

								elif len(word) > 0 and word[0] == '&':
									# Save 'aaa' for 'aaa&bbb;ccc'
									if len(prev) > 2:
										names.append(prev)
									prev = ''

									# Save 'aaa' from '&aaa;'
									if len(word) > 2:
										names.append(word[1:])
									word = ''

								else:
									if len(word) > 2:
										names.append(word)
									word = ''

							# Not alphanumeric or '&' or '#'
							else:
								if len(word) > 2:
									names.append(word)
								word = ''

					# Check if tag is <location> or between <location> and </location>
					elif (locationStarted or temp[0:10] == '<location>'):
						locationStarted = True
						temp += ' '
						# Get terms
						word = ''
						prev = ''

						for i in range(len(temp)):
							# Skip <name>
							if (temp[0:10] == '<location>' and i < 10):
								continue
							# Get each character in chunk
							char = temp[i].lower()

							# Reached </name>
							if temp[i:i+11] == '</location>':
								# Save last word
								if len(word) > 2:
									locations.append(word)
								word = ''
								locationStarted = False
								break

							# If character is [0-9a-zA-Z_] or '&', '#'
							elif char.isalnum() or char in ('&','#','_'):
								# Save 'aaa' for 'aaa&(#)bbb;ccc' case
								if char == '&':
									if len(word) > 0:
										prev = word
										word = ''
									word += char

								# 2 Cases with '#', "hashtag" and between strings
								elif char == '#':
									# Remove '#' from case '#aaa'
									if word == '':
										continue
									# Append char if current word is '&'
									elif word == '&':
										word += char
									# Save 'aaa' from '(#)aaa#bbb' case and start bbb
									elif len(word) > 2:
										locations.append(word)
										word = ''
								# Alphanumeric or _
								else:
									word += char

							# 2 Cases with ';' - '&#number;' and '&number;'
							elif char == ';':
								if len(word) > 2 and word[0:2] == '&#':
									# Restore 'aaa' for 'aaa&#bbb;ccc'
									if len(prev) > 0:
										word = prev
										prev = ''
									# No previous string, ignore '&#aaa;'
									else:
										word = ''

								elif len(word) > 0 and word[0] == '&':
									# Save 'aaa' for 'aaa&bbb;ccc'
									if len(prev) > 2:
										locations.append(prev)
									prev = ''

									# Save 'aaa' from '&aaa;'
									if len(word) > 2:
										locations.append(word[1:])
									word = ''

								else:
									if len(word) > 2:
										locations.append(word)
									word = ''

							# Not alphanumeric or '&' or '#'
							else:
								if len(word) > 2:
									locations.append(word)
								word = ''

					temp = ''

			# Write everything to terms.txt
			for word in words:
				termsOutput.write('t-' + word + ":" + str(id) + '\n')
			for name in names:
				termsOutput.write('n-' + name + ":" + str(id) + '\n')
			for location in locations:
				termsOutput.write('l-' + location + ":" + str(id) + '\n')
			
			if line != '</statuses>\n':
				# Writes date to dates.txt
				datesOutput.write(date + ':' + id + '\n')
				# Writes line to tweets.txt
				tweetsOutput.write(id + ":" + line)

		line = inputFile.readline()
		loopCounter += 1

	inputFile.close()
	termsOutput.close()
	tweetsOutput.close()
	datesOutput.close()

main()


	

