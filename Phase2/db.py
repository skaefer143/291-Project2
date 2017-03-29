import subprocess

def tweetDB():
	# With help from https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
	subprocess.call(["db_load", "-f", filename, "-T", "-t", "hash", "tw.idx"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs db_load command to tw.idx
	return

filename = input("Please enter filename being used for input: ")
tweetDB()
