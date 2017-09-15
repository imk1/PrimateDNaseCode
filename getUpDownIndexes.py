def getNextSeqDiff(seqDiffsFile):
	# Get the next seq. diff. from a file of seq. diffs.
	seqDiffsLine = seqDiffsFile.readline()
	if seqDiffsLine == "":
		# The sequence difference file has ended
		return ["-1", -1, -1]
	seqDiffsLineElements = seqDiffsLine.split("\t")
	seqDiffChrom = seqDiffsLineElements[0]
	seqDiffStart = int(seqDiffsLineElements[1])
	seqDiffEnd = int(seqDiffsLineElements[2])
	return [seqDiffChrom, seqDiffStart, seqDiffEnd]
	

def getUpDownIndexes(seqDiffsFileName, dirRegionsFileName, outputFileName):
	# Get the indexes of the sequence differences that are located in up/down-regulated regions
	seqDiffsFile = open(seqDiffsFileName)
	dirRegionsFile = open(dirRegionsFileName)
	outputFile = open(outputFileName, 'w+')
	[seqDiffChrom, seqDiffStart, seqDiffEnd] = getNextSeqDiff(seqDiffsFile)
	seqIndex = 1
	# OUTPUT WILL BE 1-INDEXED
	allSeqDiffsSeen = False
	for line in dirRegionsFile:
		# Iterate through the up/down-regulated regions and find the overlapping sequence differences
		lineElements = line.split("\t")
		chrom = lineElements[0]
		start = int(lineElements[1])
		end = int(lineElements[2])
		while seqDiffChrom < chrom:
			# Get the next seq. diff. until a seq. diff. in the current region's chromosome has bene reached
			[seqDiffChrom, seqDiffStart, seqDiffEnd] = getNextSeqDiff(seqDiffsFile)
			seqIndex = seqIndex + 1
			if seqDiffChrom == "-1":
				# All seq. diffs. have been seen, so stop
				allSeqDiffsSeen = True
				break
		if allSeqDiffsSeen == True:
			# All seq. diffs. have been seen, so stop
			break
		while (seqDiffChrom == chrom) and (seqDiffEnd <= start):
			# The current seq. diff. is on the same chromosome as the current region, so check if it overlaps
			# If not, continue searching through seq. diffs on that chromosome for overlapping seq. diffs.
			[seqDiffChrom, seqDiffStart, seqDiffEnd] = getNextSeqDiff(seqDiffsFile)
			seqIndex = seqIndex + 1
			if seqDiffChrom == "-1":
				# All seq. diffs. have been seen, so stop
				allSeqDiffsSeen = True
				break
		if allSeqDiffsSeen == True:
			# All seq. diffs. have been seen, so stop
			break
		while (seqDiffChrom == chrom) and ((seqDiffStart >= start) and (seqDiffEnd <= end)):
			# Iterate through seq. diffs. that are FULLY CONTAINED within the region and record their indexes
			outputFile.write(str(seqIndex) + "\n")
			[seqDiffChrom, seqDiffStart, seqDiffEnd] = getNextSeqDiff(seqDiffsFile)
			seqIndex = seqIndex + 1
			if seqDiffChrom == "-1":
				# All seq. diffs. have been seen, so stop
				allSeqDiffsSeen = True
				break
		if allSeqDiffsSeen == True:
			# All seq. diffs. have been seen, so stop
			break
	seqDiffsFile.close()
	dirRegionsFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   seqDiffsFileName = sys.argv[1] 
   dirRegionsFileName = sys.argv[2]
   outputFileName = sys.argv[3]
   getUpDownIndexes(seqDiffsFileName, dirRegionsFileName, outputFileName)
