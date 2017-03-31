# CMPUT 291 - Mini Project 2
# Group 13 - Ken Li, Noah Kryzanowski, Storm Kaefer
# Phase 3 - Print all information in database
# Last Change By: Ken
# Time Changed: 4:13 PM
# ----

from bsddb3 import db 
#Get an instance of BerkeleyDB 
tweetsDatabase = db.DB() 
tweetsDatabase.open("tw.idx")
termsDatabase = db.DB() 
termsDatabase.open("te.idx")
dateDatabase = db.DB() 
dateDatabase.open("da.idx")

print("Tweets Database:")
cur = tweetsDatabase.cursor() 
iter = cur.first()
while iter:
	print(iter[0].decode("utf-8") + "\t\t" + iter[1].decode("utf-8"))
	iter = cur.next()

cur.close()
tweetsDatabase.close()

print("Terms Database:")
cur = termsDatabase.cursor() 
iter = cur.first()
while iter:
	print(iter[0].decode("utf-8") + "\t\t" + iter[1].decode("utf-8"))
	iter = cur.next()

cur.close()
termsDatabase.close()

print("Date Database:")
cur = dateDatabase.cursor() 
iter = cur.first()
while iter:
	print(iter[0].decode("utf-8") + "\t\t" + iter[1].decode("utf-8"))
	iter = cur.next()

cur.close()
dateDatabase.close()