def getNumNeighboringSeqDiffs(regionsToDifferencesFileName, outputFileName):
	# Gets the number of sequences differences in the same region as each sequence difference
	regionsToDifferencesFile = open(regionsToDifferencesFileName)
	outputFile = open(outputFileName, 'w+')
	for line in regionsToDifferencesFile:
		# Iterate through regions and find the numbers for each of the corresponding sequence differences
		lineElements = line.split("\t")
		if len(lineElements) < 5:
			# There are no sequence differences for the current region, so do not consider it
			continue
		numSeqDiffs = len(lineElements) - 4
		for seqDiffIndexStr in lineElements[4:]:
			# Iterate through the seq. diffs. associated with the current reg. and record the num. of seq. diffs.
			outputFile.write(str(numSeqDiffs) + "\n")
	regionsToDifferencesFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   regionsToDifferencesFileName = sys.argv[1] # Name of file with the regions and their associated sequence differences
   outputFileName = sys.argv[2]
   getNumNeighboringSeqDiffs(regionsToDifferencesFileName, outputFileName)
