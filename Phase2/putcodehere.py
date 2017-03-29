import subprocess
from bsddb3 import db 
#Get an instance of BerkeleyDB 
database = db.DB() 

def tweetSort():
	# With help from https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
	subprocess.call(["sort", "-h", "-u", filename, "--output=sortedTweets.txt"])
	# Outputs sort command to sortedTweets.txt
	#subprocess.call(["sort", "-h", "-u", filename, "-o"])
	# Outputs sort command to filename
	return

def indexTweets():
	
	return


filename = input("Please enter filename being used for input: ")
tweetSort()
indexTweets()
