def countNumOccurrences(uniqueMerList, multiMerList, readLength, sequence):
	# Count the number of times that each mer occurs in the sequence
	sequenceList = sequence.split("N")
	print len(sequenceList)
	for seq in sequenceList:
		# Iterate through the sequences that do not contain Ns
		remainingSequence = seq
		while len(remainingSequence) >= readLength:
			currentMer = remainingSequence[0:readLength].upper()
			if currentMer in uniqueMerList:
				# The mer occurs multiple times, so remove it from the list of unique mers and add it to the list of multi-mers
				uniqueMerList.remove(currentMer)
				multiMerList.append(currentMer)
			elif currentMer not in multiMerList:
				# This is the first time the mer has occurred
				uniqueMerList.append(currentMer)
			remainingSequence = remainingSequence[1:len(remainingSequence)]
	return [uniqueMerList, multiMerList]

def computeNumMappableReads(genomeFileName, readLength):
	# Compute the number of times each k-mer occurs and the total number of uniquely mappable bases given the read length
	uniqueMerList = []
	multiMerList = []
	genomeFile = open(genomeFileName)
	currentLine = genomeFile.readline()
	sequence = ""
	while currentLine != "":
		# Iterate through the genome lines and count the number of occurrences of each mer
		if currentLine[0] == ">":
			# Skip this line because there is no sequence
			if len(sequence) > 0:
				# Count the number of times each mer occurs in each sequence
				[uniqueMerList, multiMerList] = countNumOccurrences(uniqueMerList, multiMerList, readLength, sequence)
			sequence = ""
			currentLine = genomeFile.readline()
			continue
		sequence = sequence + currentLine.strip()
		currentLine = genomeFile.readline()
	[uniqueMerList, multiMerList] = countNumOccurrences(uniqueMerList, multiMerList, readLength, sequence)
	genomeFile.close()
	return uniqueMerList

def writeMerDictToFilePlus(uniqueMerList, readLength, uniqueMersFileName):
	# Write the mer dictionary to the output file and compute the number of uniquely mappable mers
	numUniqueMers = 0
	uniqueMersFile = open(uniqueMersFileName, 'w+')
	for mer in uniqueMerList:
		# Record the mer and the number of times that it occurs to the output file
		# There is only 1 location in the genome with the current mer
		numUniqueMers = numUniqueMers + 1
		uniqueMersFile.write(mer + "\n")
	numBases = numUniqueMers * readLength
	print numUniqueMers
	print numBases
	uniqueMersFile.close()

if __name__=="__main__":
   import sys
   genomeFileName = sys.argv[1] 
   readLength = int(sys.argv[2])
   uniqueMersFileName = sys.argv[3]
   uniqueMerList = computeNumMappableReads(genomeFileName, readLength)
   writeMerDictToFilePlus(uniqueMerList, readLength, uniqueMersFileName)
