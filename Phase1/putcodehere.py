import xml.etree.ElementTree as ET

def parseDates():
	tree = ET.parse(inputFileName)
	root = tree.getroot()

	for status in root.findall('status'):
		date = status.find('created_at').text
		id = status.find('id').text
		outputFile.write(date + ':' + id + '\n')
	

inputFileName = input('Please input a filename with the extension: ')
inputFile = open(inputFileName, 'r')
outputFileName = 'dates.txt'
outputFile = open(outputFileName, 'w')

parseDates()
