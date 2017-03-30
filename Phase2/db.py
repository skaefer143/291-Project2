import subprocess

def dateDB():
	subprocess.call(["db_load", "-f", dateFilename, "-T", "-t", "btree", "da.idx"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs db_load command to da.idx
	return

def termsDB():
	subprocess.call(["db_load", "-f", termsFilename, "-T", "-t", "btree", "te.idx"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs db_load command to te.idx
	return

def tweetDB():
	# With help from https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
	subprocess.call(["db_load", "-f", tweetsFilename, "-T", "-t", "hash", "tw.idx"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs db_load command to tw.idx
	return

tweetsFilename = input("Please enter filename that has sorted Tweets input: ")
termsFilename = input("Please enter filename that has sorted Terms input: ")
dateFilename = input("Please enter filename that has sorted Date input: ")
tweetDB()
termsDB()
dateDB()

exit()