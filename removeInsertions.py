def getFastaHeader(currentFastaLine):
	# Gets the header for a fasta entry
	currentFastaLineElements = currentFastaLine.split("_")
	currentFastaChrom = currentFastaLineElements[1]
	currentFastaStart = int(currentFastaLineElements[2])
	currentFastaEnd = int(currentFastaLineElements[3])
	return [currentFastaChrom, currentFastaStart, currentFastaEnd]

def writeNewFastaNoInsertion(outputFile, fastaEntry, chrom, start, end):
	# Re-write a fasta file without the insertion
	outputFile.write(">hg19_" + fastaEntry[0] + "_" + str(fastaEntry[1]) + "_" + str(fastaEntry[2]) + "_" + chrom + "_" + str(start) + "_" + str(end) + "\n")
	count = fastaEntry[1]
	inInsertion = False
	for base in fastaEntry[3]:
		# Iterate through bases and write them or their substitution to the output file
		if count == start:
			# The substitution has been reached, so write it to the output file
			inInsertion = True
		if inInsertion == True:
			# Continue unless at end of insertion
			if count >= end:
				# The insertion is over
				inInsertion = False
		if inInsertion == False:
			# Write the current base to the output file
			outputFile.write(base)
		count = count + 1
	outputFile.write("\n")

def removeInsertions(insertionFileName, fastaFileName, outputFileName):
	# For every insertion, create a new fasta where the insertion has been removed
	# ASSUMES THAT INSERTIONS AND FASTAS ARE SORTED BY CHROM, THEN START, THEN END
	insertionFile = open(insertionFileName)
	fastaFile = open(fastaFileName)
	outputFile = open(outputFileName, 'w+')
	currentFastaLine = fastaFile.readline()
	[currentFastaChrom, currentFastaStart, currentFastaEnd] = getFastaHeader(currentFastaLine)
	currentFastaList = []
	allFastasSeen = False
	for line in insertionFile:
		# Iterate through the lines of the insertions and find the intersecting fastas
		lineElements = line.split("\t")
		chrom = lineElements[0]
		start = int(lineElements[1])
		end = int(lineElements[2])
		lastFastaList = currentFastaList
		currentFastaList = []
		for fastaEntry in lastFastaList:
			# Iterate through the last substitutions fasta entries and identify those that overlap with this one
			if (chrom == fastaEntry[0]) and ((((start <= fastaEntry[1]) and (end >= fastaEntry[1])) or ((end >= fastaEntry[2]) and (start <= fastaEntry[2]))) or ((start >= fastaEntry[1]) and (end <= fastaEntry[2]))):
				# The fastas overlap, so write the replacement fasta to a file
				writeNewFastaNoInsertion(outputFile, fastaEntry, chrom, start, end)
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
		if currentFastaStart < end:
			# Iterate through the fastas that intersect the current substitution and replace the sequences
			# if instead of while ALLOWS 1 FASTA PER INSERTION SINCE INSERTIONS IN MULTIPLE FASTAS ARE REPEATED
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
			writeNewFastaNoInsertion(outputFile, fastaEntry, chrom, start, end)
			if currentFastaLine == "":
				# At end of the fastaFile, so stop
				allFastasSeen = True
				break
			currentFastaList.append(fastaEntry)
			[currentFastaChrom, currentFastaStart, currentFastaEnd] = getFastaHeader(currentFastaLine)
			if currentFastaChrom != chrom:
				# All of the fastas on the chromosome of the substitution have been seen, so stop
				break
	insertionFile.close()
	fastaFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   insertionFileName = sys.argv[1] 
   fastaFileName = sys.argv[2]
   outputFileName = sys.argv[3]
   removeInsertions(insertionFileName, fastaFileName, outputFileName)
