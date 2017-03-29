import sys
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