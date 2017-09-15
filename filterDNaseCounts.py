def makeIntList(intListFileName):
	# Make a list of integers from a file that contains a list of integers
	# ASSUMES THAT EACH ROW HAS COLUMNS FOR A DIFFERENT SPECIES
	intList = []
	intListFile = open(intListFileName)
	lineCount = 0
	for line in intListFile:
		# Iterate through the list of integers in the file and add each integer to the list
		intList.append([])
		lineElements = line.split("\t")
		for colNum in lineElements:
			# Iterate through column numbers and add them to the array
			intList[lineCount].append(int(colNum.strip()))
		lineCount = lineCount + 1
	intListFile.close()
	return intList

def filterDNaseCounts (DNaseCountsFileName, colListFileName, outputFileName):
	# Filter DNase counts to include only regions that have at least 1 read from each column
	DNaseCountsFile = open(DNaseCountsFileName)
	colMat = makeIntList(colListFileName)
	outputFile = open(outputFileName, 'w+')
	DNaseCountsFile.readline()
	for line in DNaseCountsFile:
		# Iterate through the lines in the DNase file and record those with reads in each column in the list
		lineElements = line.split("\t")
		recordLine = True
		for colList in colMat:
			# Iterate through column lists and check that each species has at least 1 read
			allZeros = True
			for col in colList:
				# Iterate through columns and check that at least 1 read is present
				if int(lineElements[col]) > 0:
					# There are reads in the current column
					allZeros = False
					break
			if allZeros == True:
				# There are no reads for the current species, so do not record the line
				recordLine = False
		if recordLine == True:
			# Record the line in the output file
			outputFile.write(line)
	DNaseCountsFile.close()
	outputFile.close()

if __name__=="__main__":
    import sys
    DNaseCountsFileName = sys.argv[1]
    colListFileName = sys.argv[2]
    outputFileName = sys.argv[3]
    filterDNaseCounts (DNaseCountsFileName, colListFileName, outputFileName)
