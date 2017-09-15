def getCommonFastaIndexes(fastaFileOneName, fastaFileTwoName, outputFileName):
	# Gets the locations in the fasta files where the sequences agree and prints a list of corresponding 1s and 0s
	fastaFileOne = open(fastaFileOneName)
	fastaFileTwo = open(fastaFileTwoName)
	outputFile = open(outputFileName, 'w+')

	currentLineOne = fastaFileOne.readline()
	currentLineTwo = fastaFileTwo.readline()
	while currentLineOne != "":
		# Iterate through the lines of the fasta file to and determine whether the sequences are the same
		# Sequences are on every other line
		currentLineOne = fastaFileOne.readline()
		currentLineTwo = fastaFileTwo.readline()
		if currentLineOne.strip().upper() == currentLineTwo.strip().upper():
			# The sequences agree, so write a 1 to the output file
			outputFile.write("1\n")
		else:
			outputFile.write("0\n")
		currentLineOne = fastaFileOne.readline()
		currentLineTwo = fastaFileTwo.readline()

	fastaFileOne.close()
	fastaFileTwo.close()
	outputFile.close()


if __name__=="__main__":
   import sys
   fastaFileOneName = sys.argv[1] 
   fastaFileTwoName = sys.argv[2]
   outputFileName = sys.argv[3]

   getCommonFastaIndexes(fastaFileOneName, fastaFileTwoName, outputFileName)
