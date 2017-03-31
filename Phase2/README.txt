Phase2 Instructions:
(Assuming Phase1 is complete)

1. Run "sort.py" (Sort tweets.txt, dates.txt, terms.txt)

2. Enable perl script if not already:
	"chmod +x break.pl"

3. Run 3 perl scripts in terminal (Prepare sorted files for indexing):
	"perl break.pl < sortedTweets.txt >| indexedTweets.txt"
	"perl break.pl < sortedDates.txt >| indexedDates.txt"
	"perl break.pl < sortedTerms.txt >| indexedTerms.txt"

4. Run "create.py" (Create index files from indexed<FILE>.txt)
