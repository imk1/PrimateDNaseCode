def getNextPeak(currentPeakLine):
	# Gets the information for the next peak
	currentPeakLineElements = currentPeakLine.split("\t")
	currentPeakLoc = (currentPeakLineElements[0], int(currentPeakLineElements[1]), int(currentPeakLineElements[2]))
	currentPeakHeight = float(currentPeakLineElements[6])
	currentPeakpVal = float(currentPeakLineElements[7])
	return [currentPeakLoc, currentPeakHeight, currentPeakpVal]

def associateSeqDiffsToPeaks(seqDiffsFileName, peaksFileName, outputFileName):
	# Get the following information for associating sequence differences to peaks:
	# Column 1: Is the sequence difference in the peak? (Binary)
	# Column 2: What is the height of the peak that the sequence difference is in? (0 if not in a peak)
	# Column 3: What is the -log10(p-value) of the peak that the sequence difference is in? (0 if not in a peak)
	# ASSUMES THAT EACH SEQUENCE DIFFERENCE IS IN AT MOST 1 PEAK
	# ASSUMES THAT PEAKS AND SEQ. DIFFS. ARE SORTED BY CHROM, THEN START, THEN END
	# Allows for only part of sequence difference to be in the peak
	seqDiffsFile = open(seqDiffsFileName)
	peaksFile = open(peaksFileName)
	outputFile = open(outputFileName, 'w+')
	[currentPeakLoc, currentPeakHeight, currentPeakpVal] = getNextPeak(peaksFile.readline())
	for line in seqDiffsFile:
		# Get the peak features for each sequence difference
		inPeak = 0
		peakHeight = 0
		peakpVal = 0
		lineElements = line.split("\t")
		seqDiffLoc = (lineElements[0], int(lineElements[1]), int(lineElements[2]))
		while seqDiffLoc[0] > currentPeakLoc[0]:
			# Iterate through the peaks until a peak in the same chromosome as the sequence difference is reached
			[currentPeakLoc, currentPeakHeight, currentPeakpVal] = getNextPeak(peaksFile.readline())
		while (seqDiffLoc[0] == currentPeakLoc[0]) and (currentPeakLoc[2] < seqDiffLoc[1]):
			# Iterate through peaks until a peak that does not occur earlier than the seq. diff. is reached
			[currentPeakLoc, currentPeakHeight, currentPeakpVal] = getNextPeak(peaksFile.readline())
		if (seqDiffLoc[0] == currentPeakLoc[0]) and ((currentPeakLoc[2] > seqDiffLoc[1]) and (currentPeakLoc[1] < seqDiffLoc[2])):
			# The peak and the sequence difference overlap
			inPeak = 1
			peakHeight = currentPeakHeight
			peakpVal = currentPeakpVal
		outputFile.write(str(inPeak) + "\t" + str(peakHeight) + "\t" + str(peakpVal) + "\n")
	seqDiffsFile.close()
	peaksFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   seqDiffsFileName = sys.argv[1] 
   peaksFileName = sys.argv[2]
   outputFileName = sys.argv[3]
   associateSeqDiffsToPeaks(seqDiffsFileName, peaksFileName, outputFileName)
			
