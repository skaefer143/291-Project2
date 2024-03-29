# CMPUT 291 - Mini Project 2
# Group 13 - Ken Li, Noah Kryzanowski, Storm Kaefer
# Phase 2 - Create index files
# Last Change By: Storm
# Time Changed:
# ----
# With help from https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
# ----
# Filenames must be indexedTweets.txt, indexedTerms.txt, and indexedDates.txt for program to work
# ----

import subprocess

def dateDB():
	subprocess.call(["db_load", "-c", "dupsort=1", "-f", dateFilename, "-T", "-t", "btree", "da.idx"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs db_load command to da.idx
	# The -c dupsort=1 argument makes sure that duplicates are in the database and sorted
	return

def termsDB():
	subprocess.call(["db_load", "-c", "dupsort=1", "-f", termsFilename, "-T", "-t", "btree", "te.idx"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs db_load command to te.idx
	# The -c dupsort=1 argument makes sure that duplicates are in the database and sorted
	return

def tweetDB():
	subprocess.call(["db_load", "-f", tweetsFilename, "-T", "-t", "hash", "tw.idx"])
	# Outputs db_load command to tw.idx
	return

tweetsFilename = "indexedTweets.txt"
termsFilename = "indexedTerms.txt"
dateFilename = "indexedDates.txt"
tweetDB()
termsDB()
dateDB()

print("--- Database Created. (This message will always display)")

exit()