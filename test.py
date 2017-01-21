import csv
import operator

dataList = []
numberAlive = 0
maxNumberAlive = 0
yearWithMostAlive = 1900
yearsList = {}
yearDiedList = {}

with open('datafile.csv', 'rb') as f:
	reader = csv.reader(f)
	dataList = list(reader)

for i in dataList:
	yearBorn = int(i[2])
	yearDied = i[3]
	if yearDied != '':
		yearDied = int(yearDied)
	if yearBorn in yearsList:
		yearsList[yearBorn] += 1
	else:
		yearsList[yearBorn] = 1

	if yearDied == '':
		yearsList[yearDied] = 0
	elif yearDied in yearsList:
		yearsList[yearDied] -= 1
	else:
		yearsList[yearDied] = -1

sortedList = sorted(yearsList.items(), key=operator.itemgetter(0))
print sortedList
for i in sortedList:
	numberAlive += i[1]
	if numberAlive > maxNumberAlive:
		maxNumberAlive = numberAlive
		yearWithMostAlive = i[0]
print yearWithMostAlive
print maxNumberAlive
