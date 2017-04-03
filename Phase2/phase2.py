# CMPUT 291 - Mini Project 2
# Group 13 - Ken Li, Noah Kryzanowski, Storm Kaefer
# Phase 2 - Calls all required steps
# Last Change By: Ken
# Time Changed: 1:25AM
# ----
# With help from https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
# ----
# Filenames must be tweets.txt, terms.txt, and dates.txt for program to work
# ----

import subprocess
import os
import stat

def dateSort(dateFilename):
	subprocess.call(["sort", "-u", dateFilename, "--output=sortedDates.txt"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs sort command to sortedTweets.txt
	return

def termSort(termsFilename):
	subprocess.call(["sort", "-u", termsFilename, "--output=sortedTerms.txt"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs sort command to sortedTweets.txt
	return

def tweetSort(tweetFilename):
	subprocess.call(["sort", "-u", tweetFilename, "--output=sortedTweets.txt"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs sort command to sortedTweets.txt
	#subprocess.call(["sort", "-h", "-u", filename, "-o"])
	# Outputs sort command to filename
	return

def dateDB(dateFilename):
	subprocess.call(["db_load", "-c", "dupsort=1", "-f", dateFilename, "-T", "-t", "btree", "da.idx"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs db_load command to da.idx
	# The -c dupsort=1 argument makes sure that duplicates are in the database and sorted
	return

def termsDB(termsFilename):
	subprocess.call(["db_load", "-c", "dupsort=1", "-f", termsFilename, "-T", "-t", "btree", "te.idx"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs db_load command to te.idx
	# The -c dupsort=1 argument makes sure that duplicates are in the database and sorted
	return

def tweetDB(tweetsFilename):
	subprocess.call(["db_load", "-f", tweetsFilename, "-T", "-t", "hash", "tw.idx"])
	# Outputs db_load command to tw.idx
	return

def main():
	tweetSort("tweets.txt")
	termSort("terms.txt")
	dateSort("dates.txt")

	print("--- Sort done. (This message will always display)")

	st = os.stat('break.pl')
	os.chmod('break.pl', st.st_mode | stat.S_IEXEC)

	subprocess.call(['sh', '-c', 'perl break.pl < sortedTweets.txt >| indexedTweets.txt'])
	subprocess.call(['sh', '-c', 'perl break.pl < sortedDates.txt >| indexedDates.txt'])
	subprocess.call(['sh', '-c', 'perl break.pl < sortedTerms.txt >| indexedTerms.txt'])

	tweetDB("indexedTweets.txt")
	termsDB("indexedTerms.txt")
	dateDB("indexedDates.txt")

	print("--- Database Created. (This message will always display)")
main()