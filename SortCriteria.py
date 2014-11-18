#Function whcih reads the file persons.dat and converts it into list
def parsePersons():
	fl = open('persons.dat', 'r')
	fl_str = fl.readlines()
	PersonsList = []
	for row in fl_str:
	   dl_str = row.strip().split(',')
	   PersonsList.append([dl_str[0],int(dl_str[1]),int(dl_str[2]),int(dl_str[3])])
	return PersonsList

#Printing the messages as per sample output
print "Select the criteria to sort the file by:"
print "1. Name"
print "2. Age"
print "3. Weight"
print "4. Height"

#In a temporary List, put the parsed List
ParsePersonList = parsePersons()

#User input to choose the criteria
a = int(raw_input("Sort by what criteria: "))

#Open the persons.dat for rewriting as per the sorting
f = open('persons.dat', 'w')

# Sort based on user specified criteria
SortedList = sorted(ParsePersonList, key=lambda student: student[a-1])

# Rewrite in the file opened above
for i in SortedList:
	f.write(i[0]+","+str(i[1])+","+str(i[2])+","+str(i[3])+"\n")

#Printing the sort criteria
if a is 1:
	print "Sorted by Name!"
elif a is 2:
	print "Sorted by Age!"
elif a is 3:
	print "Sorted by Weight!"
elif a is 4:
	print "Sorted by Height!"
