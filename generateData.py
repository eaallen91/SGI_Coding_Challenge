import random

dataFile = open('datafile.csv','w');

for i in range(0,1000000):
	randomLastName = "a"
	randomFirstName = "b"
	randomBirthYear = random.randrange(1900,2001)
	randomDeathYear = random.randrange(1900,2001)
	dataFile.write(randomLastName + "," + randomFirstName + "," + str(randomBirthYear) + "," + str(randomDeathYear) + "\n")

dataFile.close()
