def getNextPeak(currentPeakLine):
	# Gets the information for the next peak
	currentPeakLineElements = currentPeakLine.split("\t")
	currentPeakLoc = (currentPeakLineElements[0], int(currentPeakLineElements[1]), int(currentPeakLineElements[2]))
	currentPeakHeight = float(currentPeakLineElements[6])
	currentPeakpVal = float(currentPeakLineElements[7])
	return [currentPeakLoc, currentPeakHeight, currentPeakpVal]

def associateSeqDiffsToPeaksNorm(seqDiffsFileName, peaksFileName, regionsToDifferencesFileName, regionsPeakAveragesFileName, outputFileName, averageStartCol, averageEndCol):
	# Get the following normalized information for associating sequence differences to peaks:
	# Column 1: (Is the sequence difference in the peak?)/(Fraction of region in a peak)
	# Column 2: (What is the height of the peak that the sequence difference is in?)/(Weighted average of peak heights in region) (0 if not in a peak)
	# Column 3: (What is the -log10(p-value) of the peak that the sequence difference is in?)/(Weighted average of -log10(p-value)'s in region) (0 if not in a peak)
	# ASSUMES THAT EACH SEQUENCE DIFFERENCE IS IN AT MOST 1 PEAK
	# ASSUMES THAT PEAKS AND SEQ. DIFFS. ARE SORTED BY CHROM, THEN START, THEN END
	# Regions include DNase regions and surrounding regions
	# Allows for only part of sequence difference to be in the peak
	# Value is 0 for features if no peaks overlap the region with the sequence difference
	seqDiffsFile = open(seqDiffsFileName)
	sequenceDifferenceLines = seqDiffsFile.readlines()
	seqDiffsFile.close()
	peaksFile = open(peaksFileName)
	regionsToDifferencesFile = open(regionsToDifferencesFileName)
	regionsPeakAveragesFile = open(regionsPeakAveragesFileName)
	outputFile = open(outputFileName, 'w+')
	[currentPeakLoc, currentPeakHeight, currentPeakpVal] = getNextPeak(peaksFile.readline())
	for line in regionsToDifferencesFile:
		# Iterate through regions and find the features for each of the corresponding sequence differences
		currentRegionPeakAverages = regionsPeakAveragesFile.readline() # NEED TO READ REGION DATA FOR EVERY REGION
		lineElements = line.split("\t")
		if len(lineElements) < 5:
			# There are no sequence differences for the current region, so do not consider it
			continue
		currentRegionPeakAveragesElements = currentRegionPeakAverages.split("\t")
		currentRegionPeakAveragesTuple = []
		for i in range(averageStartCol, averageEndCol + 1):
			# Iterate through the columns with the normalization data and add the data to a array
			currentRegionPeakAveragesTuple.append(float(currentRegionPeakAveragesElements[i]))
		for seqDiffIndexStr in lineElements[4:]:
			# Iterate through the sequence differences associated with the current region and get the normalized ChIP-seq peak features for each
			seqDiffIndex = int(seqDiffIndexStr.strip())
			seqDiffInfo = sequenceDifferenceLines[seqDiffIndex].split("\t")
			seqDiffLoc = (seqDiffInfo[0], int(seqDiffInfo[1]), int(seqDiffInfo[2]))
			inPeak = 0
			peakHeight = 0
			peakpVal = 0
			while seqDiffLoc[0] > currentPeakLoc[0]:
				# Iterate through the peaks until a peak in the same chromosome as the sequence difference is reached
				[currentPeakLoc, currentPeakHeight, currentPeakpVal] = getNextPeak(peaksFile.readline())
			while (seqDiffLoc[0] == currentPeakLoc[0]) and (currentPeakLoc[2] < seqDiffLoc[1]):
				# Iterate through peaks until a peak that does not occur earlier than the seq. diff. is reached
				[currentPeakLoc, currentPeakHeight, currentPeakpVal] = getNextPeak(peaksFile.readline())
			if ((seqDiffLoc[0] == currentPeakLoc[0]) and ((currentPeakLoc[2] > seqDiffLoc[1]) and (currentPeakLoc[1] < seqDiffLoc[2]))) and (currentRegionPeakAveragesTuple[0] != 0):
				# The peak and the sequence difference overlap
				# Divide all features by the number of reads in the region
				inPeak = float(1) / currentRegionPeakAveragesTuple[0]
				peakHeight = currentPeakHeight / currentRegionPeakAveragesTuple[0]
				peakpVal = currentPeakpVal / currentRegionPeakAveragesTuple[0]
			#else:
			#	inPeak = -currentRegionPeakAveragesTuple[0]
			#	peakHeight = -currentRegionPeakAveragesTuple[1]
			#	peakpVal = -currentRegionPeakAveragesTuple[2]
			outputFile.write(str(inPeak) + "\t" + str(peakHeight) + "\t" + str(peakpVal) + "\n")
	peaksFile.close()
	regionsToDifferencesFile.close()
	regionsPeakAveragesFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   seqDiffsFileName = sys.argv[1] 
   peaksFileName = sys.argv[2]
   regionsToDifferencesFileName = sys.argv[3] # Name of file with the regions mapped to their corresponding sequence differences sequence differences
   regionsPeakAveragesFileName = sys.argv[4]
   outputFileName = sys.argv[5]
   averageStartCol = int(sys.argv[6]) # Column with the first region average/normalization number, 0-INDEXED
   averageEndCol = int(sys.argv[7]) # Column with the last region average/normalization number, 0-INDEXED
   associateSeqDiffsToPeaksNorm(seqDiffsFileName, peaksFileName, regionsToDifferencesFileName, regionsPeakAveragesFileName, outputFileName, averageStartCol, averageEndCol)
			
