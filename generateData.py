########################################################################################################################
# A script used to generate a user specified number of rows containing random names, birth years and death years. 
# Death years must be greater than birth years. Names are randomly select and contain both male and female (names might
# not make that much sense).
#
# Who         | What                                                                                     | When 
# ----------------------------------------------------------------------------------------------------------------------
# Eric Allen  | Created the file and updated allowing for randomly selected names and birth/death years  | Jan 20, 2017
########################################################################################################################
import random

# Get the user specified number of rows
numRows = input("Please input how many rows of data you would like: ")

# Initialize an empty list for names
namesList = []

# Open the names file and put each name into the list
with open('names.txt', 'rb') as nameFile:
	for line in nameFile:
		namesList.append(line.strip())

# Open the data file we will be writing to
dataFile = open('datafile.csv','w')

# Generate a specified number of rows of data
for i in range(0,numRows):
	randomLastName = random.choice(namesList)
	randomFirstName = random.choice(namesList)
	randomBirthYear = random.randrange(1900,2000)
	randomDeathYear = random.randrange(randomBirthYear,2000)
	dataFile.write(randomLastName + "," + randomFirstName + "," + str(randomBirthYear) + "," + str(randomDeathYear) + "\n")

print "Data file has been created successfully! datafile.csv"
dataFile.close()
