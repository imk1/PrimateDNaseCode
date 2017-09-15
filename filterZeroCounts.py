def filterZeroCounts(allReadsFileName, numSpecies, numColsPerSpecies, outputFileName, keptLinesFileName):
	# Run the 0 counts filter, which removes any window for which there are 0 counts across individuals from a species
	# ASSUMES THAT EVERY SPECIES HAS THE SAME NUMBER OF INDIVIDUALS
	allReadsFile = open(allReadsFileName)
	outputFile = open(outputFileName, 'w+')
	keptLinesFile = open(keptLinesFileName, 'w+')
	lineIndex = 0 # LINES THAT ARE KEPT ARE 0-INDEXED
	for line in allReadsFile:
		# Iterate through the reads lines, checking that there is a read from an individual from each species
		lineElements = line.split("\t")
		excludeLine = False
		for i in range(numSpecies):
			# Iterate through the species, checking that there is a read for at least 1 individual
			noReads = True
			for j in range(numColsPerSpecies):
				# Itereate through the individuals in the current species, checking if there is a read
				if int(lineElements[(i*numColsPerSpecies) + j].strip()) > 0:
					# There is a read for the current species
					noReads = False
					break

			if noReads == True:
				# There are no reads for a species
				excludeLine = True
				break
		if excludeLine == False:
			# Do not exclude the current window
			outputFile.write(line)
			keptLinesFile.write(str(lineIndex) + "\n")
		lineIndex = lineIndex + 1
	allReadsFile.close()
	outputFile.close()
	keptLinesFile.close()


if __name__=="__main__":
   import sys
   allReadsFileName = sys.argv[1] # Name of file with the numbers of reads for each individual in each window
   numSpecies = int(sys.argv[2]) # Number of species
   numColsPerSpecies = int(sys.argv[3]) # Number of individuals per species
   outputFileName = sys.argv[4]
   keptLinesFileName = sys.argv[5]

   filterZeroCounts(allReadsFileName, numSpecies, numColsPerSpecies, outputFileName, keptLinesFileName)
