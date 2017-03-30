# CMPUT 291 - Mini Project 2
# Group 13 - Ken Li, Noah Kryzanowski, Storm Kaefer
# Phase 1 (Terms)
# Last Change By: Ken
# Time Changed: March 30, 1:40AM
# ----
# Bugs
# - Special characters in the middle of a string
# - Hashtag in the middle of a string
# ---

import re

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

	loopCounter = 0
	line = inputFile.readline()
	# Loop for each line
	while line:
		idFound = False
		termsStarted = False
		nameStarted = False
		locationStarted = False

		words = []
		names = []
		locations = []

		# Skip the first 2 lines
		if loopCounter > 1:
			# Get each chunk of text split by a space
			temp = ''
			for char in line:
				if char != ' ':
					temp += char

				# Split line at spaces
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

					# Check if tag is <text>
					elif (termsStarted or temp[0:6] == '<text>'):
						termsStarted = True
						# Get terms
						word = ''
						for i in range(len(temp)):
							# Skip <text>
							if (temp[0:6] == '<text>' and i < 6): continue

							char = temp[i].lower()

							# Reached </text>
							if temp[i:i+8] == '</text>':
								# Save last word
								if len(word) > 2:
									words.append(word)
								word = ''
								termsStarted = False
								break

							# If character is [0-9a-zA-Z_] and '&' or '#'
							elif char.isalnum() or char in ('&','#','_'):
								# Have a word before, but special character has started
								if char == '&' and len(word) > 0:
									if len(word) > 2:
										words.append(word)
									word = ''

								# special character has started but not '&#numbers;'
								elif word == '&' and char != '#': word = ''

								# Hashtag word has started
								elif word == '#': word = ''

								word += char

								# If current word is size of seperate word
								if len(word) == len(temp):
									if len(word) > 2:
										words.append(word)
									word = ''
							
							# Check if special character '&#number;'
							elif (char == ';' and word[0:2] == '&#'): word = ''

							# Anything else, word ends
							else:
								if len(word) > 2:
									words.append(word)
								word = ''

						if len(word) > 2 and re.match(r'\w+$', word): words.append(word)

					# Check if tag is <name>
					elif (nameStarted or temp[0:6] == '<name>'):
						nameStarted = True
						# Get names
						name = ''
						for i in range(len(temp)):
							# Skip <name>
							if (temp[0:6] == '<name>' and i < 6): continue

							char = temp[i].lower()

							# Reached </name>
							if temp[i:i+8] == '</name>':
								# Save last name
								if len(name) > 2:
									names.append(name)
								name = ''
								nameStarted = False
								break

							# If character is [0-9a-zA-Z_] and '&' or '#'
							elif char.isalnum() or char in ('&','#','_'):
								# Have a name before, but special character has started
								if char == '&' and len(name) > 0:
									if len(name) > 2:
										names.append(name)
									name = ''

								# Hashtag name has started
								elif name == '#': name = ''

								name += char

								# If current name is size of seperate name
								if len(name) == len(temp):
									if len(name) > 2:
										names.append(name)
									name = ''
							
							# Check if special character '&#number;'
							elif (char == ';' and name[0:2] == '&#'): name = ''

							# Anything else, name ends
							else:
								if len(name) > 2:
									names.append(name)
								name = ''

						if len(name) > 2 and re.match(r'\w+$', name): names.append(name)

					# Check if tag is <location>
					elif (locationStarted or temp[0:10] == '<location>'):
						locationStarted = True
						# Get locations
						location = ''
						for i in range(len(temp)):
							# Skip <location>
							if (temp[0:10] == '<location>' and i < 10): continue

							char = temp[i].lower()

							# Reached </location>
							if temp[i:i+12] == '</location>':
								# Save last location
								if len(location) > 2:
									locations.append(location)
								location = ''
								locationStarted = False
								break

							# If character is [0-9a-zA-Z_] and '&' or '#'
							elif char.isalnum() or char in ('&','#','_'):
								# Have a location before, but special character has started
								if char == '&' and len(location) > 0:
									if len(location) > 2:
										locations.append(location)
									location = ''

								# Hashtag location has started
								elif location == '#': location = ''

								location += char

								# If current location is size of seperate location
								if len(location) == len(temp):
									if len(location) > 2:
										locations.append(location)
									location = ''
							
							# Check if special character '&#number;'
							elif (char == ';' and location[0:2] == '&#'): location = ''

							# Anything else, location ends
							else:
								if len(location) > 2:
									locations.append(location)
								location = ''

						if len(location) > 2 and re.match(r'\w+$', location): locations.append(location)

					temp = ''

			# Write everything to terms.txt
			for word in words:
				termsOutput.write('t-' + word + ":" + str(id) + '\n')
			for name in names:
				termsOutput.write('n-' + name + ":" + str(id) + '\n')
			for location in locations:
				termsOutput.write('l-' + location + ":" + str(id) + '\n')

		line = inputFile.readline()
		loopCounter += 1

	inputFile.close()
	termsOutput.close()

main()