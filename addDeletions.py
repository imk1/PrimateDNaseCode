def getFastaHeader(fastaLine):
	# Gets the location of a fasta entry
	lineElements = fastaLine.split("_")
	fastaChrom = lineElements[1]
	fastaStart = int(lineElements[2])
	fastaEnd = int(lineElements[3].strip())
	return [fastaChrom, fastaStart, fastaEnd]

def writeNewFastaDeletion(outputFile, fastaEntry, chrom, start, end, sequence):
	# Re-write a fasta file with the deletion
	outputFile.write(">hg19_" + fastaEntry[0] + "_" + str(fastaEntry[1]) + "_" + str(fastaEntry[2]) + "_" + chrom + "_" + str(start) + "_" + str(end) + "\n")
	count = fastaEntry[1]
	inDeletion = False
	for base in fastaEntry[3]:
		# Iterate through bases and write them and the deletion to the output file
		outputFile.write(base) # ASSUMES THAT DELETION OCCURS RIGHT AFTER ITS FIRST COORDINATE
		if count == start:
			# The deletion has been reached, so write it to the output file
			outputFile.write(sequence)			
		count = count + 1
	outputFile.write("\n")

def addDeletions(fastaFileName, deletionFileName, outputFileName):
	# Add the sequences of deletions into their proper locations in a fasta file
	# ASSUMES THAT DELETIONS AND FASTAS ARE SORTED BY CHROM, THEN START, THEN END
	deletionFile = open(deletionFileName)
	fastaFile = open(fastaFileName)
	outputFile = open(outputFileName, 'w+')
	currentFastaLine = fastaFile.readline()
	[currentFastaChrom, currentFastaStart, currentFastaEnd] = getFastaHeader(currentFastaLine)
	currentFastaList = []
	allFastasSeen = False
	for line in deletionFile:
		# Iterate through the lines of the deletions and find the intersecting fastas
		lineElements = line.split("\t")
		chrom = lineElements[0]
		start = int(lineElements[1])
		end = int(lineElements[2])
		sequence = lineElements[3].strip()
		lastFastaList = currentFastaList
		currentFastaList = []
		for fastaEntry in lastFastaList:
			# Iterate through the last insertions' fasta entries and identify those that overlap with this one
			if (chrom == fastaEntry[0]) and ((((start <= fastaEntry[1]) and (end >= fastaEntry[1])) or ((end >= fastaEntry[2]) and (start <= fastaEntry[2]))) or ((start >= fastaEntry[1]) and (end <= fastaEntry[2]))):
				# The fastas overlap, so write the replacement fasta to a file
				writeNewFastaDeletion(outputFile, fastaEntry, chrom, start, end, sequence)
				currentFastaList.append(fastaEntry)
		if allFastasSeen == True:
			# All fastas have been seen, so do not look for other fastas that might contain the insertion
			continue
		while currentFastaChrom < chrom:
			# Get new fastas until a fasta on the current chromosome has been reached
			currentFastaLine = fastaFile.readline()
			# ASSUMES THAT ALL ENTRIES IN THE FASTA FILE HAVE AT LEAST 1 BASE
			while (currentFastaLine != "") and (currentFastaLine[0] != ">"):
				# Not at a new entry yet
				currentFastaLine = fastaFile.readline()
			if currentFastaLine == "":
				# At the end of the fasta file, so stop
				allFastasSeen = True
				break
			[currentFastaChrom, currentFastaStart, currentFastaEnd] = getFastaHeader(currentFastaLine)
		if allFastasSeen == True:
			# At the end of the fasta file, so stop
			break
		allChromSeen = False
		while currentFastaEnd <= start:
			# Get new fastas until a fasta that does not come before the current location has been reached
			if currentFastaChrom != chrom:
				# All of the current chromosome has been seen, so stop
				allChromSeen = True
				break
			currentFastaLine = fastaFile.readline()
			# ASSUMES THAT ALL ENTRIES IN THE FASTA FILE HAVE AT LEAST 1 BASE
			while currentFastaLine[0] != ">":
				# Not at a new entry yet
				currentFastaLine = fastaFile.readline()
			if currentFastaLine == "":
				# At the end of the fasta file, so stop
				allFastasSeen = True
				break
			[currentFastaChrom, currentFastaStart, currentFastaEnd] = getFastaHeader(currentFastaLine)
		if allFastasSeen == True:
			# At the end of the fasta file, so stop
			break
		if allChromSeen == True:
			# All of the chromosome has been seen, so continue to the next substitution
			continue
		while currentFastaStart < end:
			# Iterate through the fastas that intersect the current substitution and replace the sequences
			currentFastaSequence = ""
			currentFastaLine = fastaFile.readline()
			while (currentFastaLine != "") and (currentFastaLine[0] != ">"):
				# Get the fasta sequence
				currentFastaSequence = currentFastaSequence + currentFastaLine.strip()
				currentFastaLine = fastaFile.readline()
			fastaEntry = []
			fastaEntry.append(currentFastaChrom)
			fastaEntry.append(currentFastaStart)
			fastaEntry.append(currentFastaEnd)
			fastaEntry.append(currentFastaSequence)
			writeNewFastaDeletion(outputFile, fastaEntry, chrom, start, end, sequence)
			if currentFastaLine == "":
				# At end of the fastaFile, so stop
				allFastasSeen = True
				break
			currentFastaList.append(fastaEntry)
			[currentFastaChrom, currentFastaStart, currentFastaEnd] = getFastaHeader(currentFastaLine)
			if currentFastaChrom != chrom:
				# All of the fastas on the chromosome of the substitution have been seen, so stop
				break
	deletionFile.close()
	fastaFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   fastaFileName = sys.argv[1] 
   deletionFileName = sys.argv[2]
   outputFileName = sys.argv[3]
   addDeletions(fastaFileName, deletionFileName, outputFileName)
