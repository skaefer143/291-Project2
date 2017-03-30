from bsddb3 import db 
#Get an instance of BerkeleyDB 
database = db.DB() 
database.open("tw.idx")

cur = database.cursor() 
iter = cur.first()
while iter:
	print(iter[0].decode("utf-8") + "\t" + iter[1].decode("utf-8"))
	iter = cur.next()

cur.close()
database.close()