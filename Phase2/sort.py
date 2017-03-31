# CMPUT 291 - Mini Project 2
# Group 13 - Ken Li, Noah Kryzanowski, Storm Kaefer
# Phase 2 - Sort Phase1 Output
# Last Change By:
# Time Changed:
# ----
# With help from https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
# ----
# Filenames must be tweets.txt, terms.txt, and dates.txt for program to work
# ----

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
	subprocess.call(["sort", "-u", tweetFilename, "--output=sortedTweets.txt"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs sort command to sortedTweets.txt
	#subprocess.call(["sort", "-h", "-u", filename, "-o"])
	# Outputs sort command to filename
	return

tweetFilename = "tweets.txt"
termsFilename = "terms.txt"
dateFilename = "dates.txt"
tweetSort()
termSort()
dateSort()

print("--- Sort done. (This message will always display)")

exit()