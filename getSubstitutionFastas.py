def getSubstitutionFastas(fastaFileName, binaryFileName, substitutionFileName, outputFileName):
	# Find the sequence difference that corresponds to each substitution
	fastaFile = open(fastaFileName)
	binaryFile = open(binaryFileName)
	substitutionFile = open(substitutionFileName)
	outputFile = open(outputFileName, 'w+')
	for line in substitutionFile:
		# For each substitution, find the corresponding line in the fasta file, and record the location and bases
		binaryLine = binaryFile.readline()
		fastaHeader = fastaFile.readline()
		fastaSequence = fastaFile.readline()
		while int(binaryLine.strip()) == 0:
			# The current line in the binary file corresponds to a non-common substitution, so continue
			binaryLine = binaryFile.readline()
			fastaHeader = fastaFile.readline()
			fastaSequence = fastaFile.readline()
		lineElements = line.split("\t")
		for locInfo in lineElements:
			# Write each part of the location information to the output file
			outputFile.write(locInfo.strip() + "\t")
		outputFile.write(fastaSequence)
	fastaFile.close()
	binaryFile.close()
	substitutionFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   fastaFileName = sys.argv[1] 
   binaryFileName = sys.argv[2]
   substitutionFileName = sys.argv[3]
   outputFileName = sys.argv[4]
   getSubstitutionFastas(fastaFileName, binaryFileName, substitutionFileName, outputFileName)
