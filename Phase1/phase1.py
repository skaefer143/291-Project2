# CMPUT 291 - Mini Project 2
# Group 13 - Ken Li, Noah Kryzanowski, Storm Kaefer
# Phase 1
# Version: #1
# Last Change By: Ken
# Time Changed: March 28, 5:00~PM

def main():
	# Loop till file opened correctly
	correctFile = False
	while not correctFile:
		userInput = input("Enter a input file (with file extension) or 'exit' to exit: ")
		if userInput.upper() == 'EXIT':
			print("\nProgram exiting.\n")	
			exit(0)
		try:
			inputFile = open(userInput)
			correctFile = True
		except:
			print("\nCannot open file, please try again.\n")
	

	lineCounter = 0	
	for line in inputFile:
		# First two lines, Skip
		if lineCounter < 2:
			lineCounter += 1
			continue
		# Last line, End
		elif line.rstrip() == '</statuses>': break
		# Do calculations
		else:
			print(line)
			
main()