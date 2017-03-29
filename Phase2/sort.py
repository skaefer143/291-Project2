import subprocess

def tweetSort():
	# With help from https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
	subprocess.call(["sort", "-h", "-u", filename, "--output=sortedTweets.txt"]) # -h for sorting by the id key at start, -u for unique entries
	# Outputs sort command to sortedTweets.txt
	#subprocess.call(["sort", "-h", "-u", filename, "-o"])
	# Outputs sort command to filename
	return

filename = input("Please enter filename being used for input: ")
tweetSort()
