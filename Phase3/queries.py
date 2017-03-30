from bsddb3 import db 
#Get an instance of BerkeleyDB 
database = db.DB() 
database.open("tw.idx")

cur = database.cursor() 
iter = cur.first()

userInput = input("Please type your query: ")

cur.close()
database.close()