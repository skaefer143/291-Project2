# CMPUT 291 - Mini Project 2
# Group 13 - Ken Li, Noah Kryzanowski, Storm Kaefer
# Phase 1 (Dates)
# Last Change By: Noah
# Time Changed:
# ----

import xml.etree.ElementTree as ET

def parseDates():
	tree = ET.parse(inputFileName)
	root = tree.getroot()

	for status in root.findall('status'):
		id = status.find('id').text
		date = status.find('created_at').text
		outputFile.write(date + ':' + id + '\n')
	

inputFileName = input('Please input a filename with the extension: ')
inputFile = open(inputFileName, 'r')
outputFileName = 'dates.txt'
outputFile = open(outputFileName, 'w')

parseDates()
