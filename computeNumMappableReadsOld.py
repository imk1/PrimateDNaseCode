def createMerList(readLength):
	# Create a list of all possible mers of length readLength
	bases = ["A", "C", "G", "T"]
	if readLength == 1:
		# Return the bases
		return bases
	merListShort = createMerList(readLength - 1)
	merList = []
	for mer in merListShort:
		# Append all of the bases to each mer
		for b in bases:
			# Iterate through all of the bases and add to the mer list for each
			merLong = mer + b
			merList.append(merLong)
	return merList

def createMerDict(readLength):
	# Create a dictionary for all k-mers, where k is read length
	merDict = {}
	merList = createMerList(readLength)
	print len(merList)
	for mer in merList:
		# Add each mer to the dictionary
		merDict[mer] = 0
	return merDict

def countNumOccurrences(merDict, readLength, sequence):
	# Count the number of times that each mer occurs in the sequence
	remainingSequence = sequence
	while len(remainingSequence) >= readLength:
		currentMer = remainingSequence[0:readLength].upper()
		if "N" not in currentMer:
			# Checked that every base in the current mer is known
			merDict[currentMer] = merDict[currentMer] + 1
			remainingSequence = remainingSequence[1:len(remainingSequence)]
	return merDict

def computeNumMappableReads(genomeFileName, readLength):
	# Compute the number of times each k-mer occurs and the total number of uniquely mappable bases given the read length
	merDict = createMerDict(readLength)
	genomeFile = open(genomeFileName)
	currentLine = genomeFile.readline()
	sequence = ""
	while currentLine != "":
		# Iterate through the genome lines and count the number of occurrences of each mer
		if currentLine[0] == ">":
			# Skip this line because there is no sequence
			if len(sequence) > 0:
				# Count the number of times each mer occurs in each sequence
				merDict = countNumOccurrences(merDict, readLength, sequence)
			currentLine = genomeFile.readline()
			continue
		sequence = sequence + currentLine.strip()
		currentLine = genomeFile.readline()
	merDict = countNumOccurrences(merDict, readLength, sequence)
	genomeFile.close()
	return merDict

def writeMerDictToFile(merDict, readLength, outputFileName):
	# Write the mer dictionary to the output file and compute the number of uniquely mappable mers
	numUniqueMers = 0
	outputFile = open(outputFileName, 'w+')
	for mer in merDict.keys():
		# Record the mer and the number of times that it occurs to the output file
		outputFile.write(mer + "\t" + str(merDict[mer]) + "\n")
		if merDict[mer] == 1:
			# There is only 1 location in the genome with the current mer
			numUniqueMers = numUniqueMers + 1
	numBases = numUnqiueMers * readLength
	print numUniqueMers
	print numBases
	outputFile.write("Number of uniquely mappable bases" + "\t" + str(numBases) + "\n")
	outputFile.close()

if __name__=="__main__":
   import sys
   genomeFileName = sys.argv[1] 
   readLength = int(sys.argv[2])
   outputFileName = sys.argv[3]
   merDict = computeNumMappableReads(genomeFileName, readLength)
   writeMerDictToFile(merDict, readLength, outputFileName)
