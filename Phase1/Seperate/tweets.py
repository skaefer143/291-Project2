# CMPUT 291 - Mini Project 2
# Group 13 - Ken Li, Noah Kryzanowski, Storm Kaefer
# Phase 1 (Tweets)
# Last Change By: Storm
# Time Changed:
# ----
import xml.etree.ElementTree as ET

def parseTweets():
	tree = ET.parse(filename)
	root = tree.getroot()

	for status in root.findall('status'):
		id = status.find("id").text
		outputFile.write(id + ":" + ET.tostring(status, "unicode"))


filename = input("Please enter filename being used for input: ")
file = open(filename, "r")
outputFilename = "tweets.txt"
outputFile = open(outputFilename, "w")
parseTweets()