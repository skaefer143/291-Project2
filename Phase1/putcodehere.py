# CMPUT 291 - Mini Project 2
# Group 13 - Ken Li, Noah Kryzanowski, Storm Kaefer
# Phase 1
# Last Change By: Ken
# Time Changed: March 29, 9:10PM

import re
import xml.etree.ElementTree as ET
def is_alnum(char):
	try:
		return (char.encode('ascii').isalnum() or char in ('&', '_'))
	except:
		return False

def main():
	# Loop till file opened correctly
	correctFile = False
	while not correctFile:
		# userInput = input("Enter a input file (with file extension) or 'exit' to exit: ")
		userInput = '10000.txt'
		if userInput.upper() == 'EXIT':
			print("\nProgram exiting.\n")	
			exit()
		try:
			inputFile = open(userInput)
			correctFile = True
		except:
			print("\nCannot open file, please try again.\n")
	
	# Output files
	termsOutput = open('terms.txt', 'w', encoding='utf-8')

	tree = ET.parse(inputFile)
	root = tree.getroot()

	# Go through each status
	for status in root.findall('status'):
		# Get id field of status
		id = status.find("id").text

		# Get name and location of status poster
		userInfo = status.find("user")

		# Name
		tempName = userInfo.find("name").text
		if tempName is not None:
			tempName = tempName.split()

			name = []
			for word in tempName:
				# Remove special characters from name
				temp = ''
				for char in word:
					if is_alnum(char):
						temp += char.lower()

				name.append(temp)
		else:
			name = []

		# Location
		tempLocation = userInfo.find("location").text
		if tempLocation is not None:
			tempLocation = tempLocation.split()

			location = []
			for word in tempLocation:
				# Remove special characters from location
				temp = ''
				for char in word:
					if is_alnum(char):
						temp += char.lower()

				location.append(temp)
		else:
			location = []

		# Get text field of status
		text = status.find("text").text
		text = text.replace('"',' quot ')
		text += ' '

		temp = ''
		words = []
		for char in text:
			if is_alnum(char):
				temp += char.lower()
			else:
				if len(temp) > 2:
					words.append(temp)
				temp = ''

		# Write all terms to terms.txt
		if words:
			for word in words:
				if word:
					termsOutput.write('t-' + word + ":" + str(id) + '\n')

		# Write all names to terms.txt
		if name:
			for word in name:
				if word and len(word) > 2:
					termsOutput.write('n-' + word + ":" + str(id) + '\n')

		# Write all locations to terms.txt
		if location:
			for word in location:
				if word and len(word) > 2:
					termsOutput.write('l-' + word + ":" + str(id) + '\n')

	inputFile.close()
	termsOutput.close()

main()