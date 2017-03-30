Assuming Phase1 is complete:


Run sort.py (should sort Tweets file, Dates file, and Terms file)

Then, make index files using perl script in terminal:

./break.pl < sortedTweets.txt >| indexedTweets.txt
./break.pl < sortedDates.txt >| indexedDates.txt
./break.pl < sortedTerms.txt >| indexedTerms.txt


Then, run db.py (should put into a database index the Tweets file, Dates 
file, and Terms file)
