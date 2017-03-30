import subprocess

def dateDB():
	subprocess.call(["db_load", "-c", "duplicates=1", "-f", dateFilename, "-T", "-t", "btree", "da.idx"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs db_load command to da.idx
	# The -c dupsort=1 argument makes sure that duplicates are in the database and sorted
	return

def termsDB():
	subprocess.call(["db_load", "-c", "duplicates=1", "-f", termsFilename, "-T", "-t", "btree", "te.idx"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs db_load command to te.idx
	# The -c dupsort=1 argument makes sure that duplicates are in the database and sorted
	return

def tweetDB():
	# With help from https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
	subprocess.call(["db_load", "-f", tweetsFilename, "-T", "-t", "hash", "tw.idx"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs db_load command to tw.idx
	return

print("Filenames must be indexedTweets.txt, indexedTerms.txt, and indexedDates.txt for program to work.")
print("This message will always display.")

tweetsFilename = "indexedTweets.txt"
termsFilename = "indexedTerms.txt"
dateFilename = "indexedDates.txt"
tweetDB()
termsDB()
dateDB()

exit()