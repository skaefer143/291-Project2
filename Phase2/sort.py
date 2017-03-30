import subprocess

def dateSort():
	subprocess.call(["sort", "-u", dateFilename, "--output=sortedDates.txt"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs sort command to sortedTweets.txt
	return

def termSort():
	subprocess.call(["sort", "-u", termsFilename, "--output=sortedTerms.txt"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs sort command to sortedTweets.txt
	return

def tweetSort():
	# With help from https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
	subprocess.call(["sort", "-u", tweetFilename, "--output=sortedTweets.txt"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs sort command to sortedTweets.txt
	#subprocess.call(["sort", "-h", "-u", filename, "-o"])
	# Outputs sort command to filename
	return

print("Filenames must be tweets.txt, terms.txt, and dates.txt for program to work.")
print("This message will always display.")


tweetFilename = "tweets.txt"
termsFilename = "terms.txt"
dateFilename = "dates.txt"
tweetSort()
termSort()
dateSort()

exit()