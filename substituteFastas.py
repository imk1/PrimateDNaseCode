def getFastaHeader(currentFastaLine):
	# Gets the header for a fasta entry
	currentFastaLineElements = currentFastaLine.split("_")
	currentFastaChrom = currentFastaLineElements[1]
	currentFastaStart = int(currentFastaLineElements[2])
	currentFastaEnd = int(currentFastaLineElements[3])
	return [currentFastaChrom, currentFastaStart, currentFastaEnd]

def writeNewFasta(outputFile, fastaEntry, chrom, start, end, substitution):
	# Re-write a fasta file with the substitutions
	outputFile.write(">hg19_" + fastaEntry[0] + "_" + str(fastaEntry[1]) + "_" + str(fastaEntry[2]) + "_" + chrom + "_" + str(start) + "_" + str(end) + "\n")
	count = fastaEntry[1]
	inSub = False
	for base in fastaEntry[3]:
		# Iterate through bases and write them or their substitution to the output file
		if count == start:
			# The substitution has been reached, so write it to the output file
			outputFile.write(substitution)
			inSub = True
		if inSub == True:
			# Continue unless at end of substitution
			if count >= end:
				# The substitution is over
				inSub = False
		if inSub == False:
			# Write the current base to the output file
			outputFile.write(base)
		count = count + 1
	outputFile.write("\n")

def substituteFastas(substitutionFileName, fastaFileName, outputFileName):
	# For every substitution, create a new fasta where the substitution has replaced its original sequence
	# ASSUMES THAT SUBSTITUTIONS AND FASTAS ARE SORTED BY CHROM, THEN START, THEN END
	substitutionFile = open(substitutionFileName)
	fastaFile = open(fastaFileName)
	outputFile = open(outputFileName, 'w+')
	currentFastaLine = fastaFile.readline()
	[currentFastaChrom, currentFastaStart, currentFastaEnd] = getFastaHeader(currentFastaLine)
	currentFastaList = []
	allFastasSeen = False
	for line in substitutionFile:
		# Iterate through the lines of the sequence substitutions and find the intersecting fastasq
		lineElements = line.split("\t")
		chrom = lineElements[0]
		start = int(lineElements[1])
		end = int(lineElements[2])
		substitution = lineElements[3].strip()
		lastFastaList = currentFastaList
		currentFastaList = []
		for fastaEntry in lastFastaList:
			# Iterate through the last substitutions fasta entries and identify those that overlap with this one
			if (chrom == fastaEntry[0]) and ((((start <= fastaEntry[1]) and (end >= fastaEntry[1])) or ((end >= fastaEntry[2]) and (start <= fastaEntry[2]))) or ((start >= fastaEntry[1]) and (end <= fastaEntry[2]))):
				# The fastas overlap, so write the replacement fasta to a file
				writeNewFasta(outputFile, fastaEntry, chrom, start, end, substitution)
				currentFastaList.append(fastaEntry)
		if allFastasSeen == True:
			# All fastas have beeen seen, so do not look for other fastas that might contain the substitution
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
			writeNewFasta(outputFile, fastaEntry, chrom, start, end, substitution)
			currentFastaList.append(fastaEntry)
			if currentFastaLine == "":
				# At end of the fastaFile, so stop
				allFastasSeen = True
				break
			[currentFastaChrom, currentFastaStart, currentFastaEnd] = getFastaHeader(currentFastaLine)
			if currentFastaChrom != chrom:
				# All of the fastas on the chromosome of the substitution have been seen, so stop
				break
	substitutionFile.close()
	fastaFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   substitutionFileName = sys.argv[1] 
   fastaFileName = sys.argv[2]
   outputFileName = sys.argv[3]
   substituteFastas(substitutionFileName, fastaFileName, outputFileName)
