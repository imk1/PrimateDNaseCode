def countNumOccurrences(merDict, readLength, sequence):
	# Count the number of times that each mer occurs in the sequence
	sequenceList = sequence.split("N")
	print len(sequenceList)
	for seq in sequenceList:
		# Iterate through the sequences that do not contain Ns
		remainingSequence = seq
		while len(remainingSequence) >= readLength:
			currentMer = remainingSequence[0:readLength].upper()
			if currentMer in merDict:
				# Increment the counts for the current mer
				merDict[currentMer] = merDict[currentMer] + 1
			else:
				merDict[currentMer] = 1
			remainingSequence = remainingSequence[1:len(remainingSequence)]
	return merDict

def computeNumMappableReads(genomeFileName, readLength):
	# Compute the number of times each k-mer occurs and the total number of uniquely mappable bases given the read length
	merDict = {}
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
			sequence = ""
			currentLine = genomeFile.readline()
			continue
		sequence = sequence + currentLine.strip()
		currentLine = genomeFile.readline()
	merDict = countNumOccurrences(merDict, readLength, sequence)
	genomeFile.close()
	return merDict

def writeMerDictToFile(merDict, readLength, outputFileName, uniqueMersFileName):
	# Write the mer dictionary to the output file and compute the number of uniquely mappable mers
	numUniqueMers = 0
	outputFile = open(outputFileName, 'w+')
	uniqueMersFile = open(uniqueMersFileName, 'w+')
	for mer in merDict.keys():
		# Record the mer and the number of times that it occurs to the output file
		outputFile.write(mer + "\t" + str(merDict[mer]) + "\n")
		if merDict[mer] == 1:
			# There is only 1 location in the genome with the current mer
			numUniqueMers = numUniqueMers + 1
			uniqueMersFile.write(mer + "\n")
	numBases = numUniqueMers * readLength
	print numUniqueMers
	print numBases
	outputFile.close()
	uniqueMersFile.close()

if __name__=="__main__":
   import sys
   genomeFileName = sys.argv[1] 
   readLength = int(sys.argv[2])
   outputFileName = sys.argv[3]
   uniqueMersFileName = sys.argv[4]
   merDict = computeNumMappableReads(genomeFileName, readLength)
   writeMerDictToFile(merDict, readLength, outputFileName, uniqueMersFileName)
