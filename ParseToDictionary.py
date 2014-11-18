def parsePersons(filename):
	import csv
	reader = csv.reader(open(filename, 'r'))
	PersonsDict = {}
	for row in reader:
	   Name,Age,Height,Weight = row
	   PersonsDict[Name] = int(Age),int(Height),int(Weight)
	return PersonsDict
