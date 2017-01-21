########################################################################################################################
# A script used to generate a dictionary using birth and death years as keys, and total net for a year as value. The 
# script will read in the datafile provided, read each line, if a birth year and a death year are present, increment and
# decrement respectively. Else, start a new key/value pair.
#
# Once done reading the file, the dictionray is sorted, and the entire dictionary of years is run through adding net 
# number of people per year.
#
# Who              | What                                                                                | When
# ----------------------------------------------------------------------------------------------------------------------
# Eric Allen       | Created the bare bones file                                                         | Jan 20, 2017
########################################################################################################################
import csv
import operator

# list of data read in from the data file
dataList = []

# Initialize the number alive to 0
numberAlive = 0
# Initialize the max number alive to 0
maxNumberAlive = 0
# Initialize the highest alive year to start of 1900
yearWithMostAlive = 1900
# Initialize the dictionary 
yearsDict = {}

# Open and read in each line of the data file and append to the data list
with open('datafile.csv', 'rb') as f:
	reader = csv.reader(f)
	dataList = list(reader)

# For each entry in the data list obtain the year born and died and increment/decrement the dictionary values
for entry in dataList:

	# Obtain the year born
	yearBorn = int(entry[2])
	# Obtain the year died
	yearDied = int(entry[3])
	
	
	# Check if the year born is in the dict, if so, increment value, if not, create new dict entry
	if yearBorn in yearsDict:
		yearsDict[yearBorn] += 1
	else:
		yearsDict[yearBorn] = 1

	# Check if the year died is in the dict, if so, decrement value, if not, create new dict entry
	if yearDied in yearsDict:
		yearsDict[yearDied] -= 1
	else:
		yearsDict[yearDied] = -1

# Sort the dictionary based on keys (years)
sortedDict = sorted(yearsDict.items(), key=operator.itemgetter(0))
#print sortedDict

# For eatch entry in the dictionary get the net number of people alive, compare with current, update accordingly
for element in sortedDict:
	
	# Get the net number of people alive in a year and add to the current number alive
	numberAlive += element[1]
	# If the number alive is greater than the max, set current number alive to max, and the year to current key 
	if (numberAlive > maxNumberAlive):
		maxNumberAlive = numberAlive
		yearWithMostAlive = element[0]

# Print the year the most people were alive in 
print "There were the most people alive in the year " + str(yearWithMostAlive) + " at " + str(maxNumberAlive)
