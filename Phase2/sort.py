import subprocess

def dateSort():
	subprocess.call(["sort", "-h", "-u", dateFilename, "--output=sortedDates.txt"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs sort command to sortedTweets.txt
	return

def termSort():
	subprocess.call(["sort", "-h", "-u", termsFilename, "--output=sortedTerms.txt"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs sort command to sortedTweets.txt
	return

def tweetSort():
	# With help from https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
	subprocess.call(["sort", "-h", "-u", tweetFilename, "--output=sortedTweets.txt"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs sort command to sortedTweets.txt
	#subprocess.call(["sort", "-h", "-u", filename, "-o"])
	# Outputs sort command to filename
	return

tweetFilename = input("Please enter filename that has unsorted Tweet input: ")
termsFilename = input("Please enter filename that has unsorted Terms input: ")
dateFilename = input("Please enter filename that has unsorted Date input: ")
tweetSort()
termSort()
dateSort()

exit()