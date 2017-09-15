def getSeqDiffLengths(seqDiffFileName, outputFileName):
	# Get the lengths of sequence differences
	seqDiffFile = open(seqDiffFileName)
	outputFile = open(outputFileName, 'w+')
	for line in seqDiffFile:
		# Iterate through the file with the sequence differences and get the length of each
		lineElements = line.split("\t")
		seqDiffLength = int(lineElements[2]) - int(lineElements[1])
		outputFile.write(str(seqDiffLength) + "\n")
	outputFile.close()

if __name__=="__main__":
   import sys
   seqDiffFileName = sys.argv[1] # Name of file with the sequence differences
   outputFileName = sys.argv[2]
   getSeqDiffLengths(seqDiffFileName, outputFileName)
