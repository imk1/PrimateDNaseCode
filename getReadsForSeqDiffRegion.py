def getNextWindowInfo(windowsFile, windowsReadsMediansFile):
	# Gets the information for the next window
	windowLine = windowsFile.readline()
	windowLineElements = windowLine.split("\t")
	windowLocation = (windowLineElements[0], int(windowLineElements[1]), int(windowLineElements[2].strip()))
	windowMedian = float(windowsReadsMediansFile.readline().strip())
	return [windowLocation, windowMedian]

def getReadsForSeqDiffRegion(sequenceDifferenceFileName, regionsToDifferencesFileName, windowsFileName, windowsReadsMediansFileName, regionDistance, outputFileName):
	# Get the following information for each sequence difference:
	# Column 1: How many reads are in its region?
	# Column 2: How long is its region?
	sequenceDifferenceFile = open(sequenceDifferenceFileName)
	sequenceDifferenceLines = sequenceDifferenceFile.readlines()
	sequenceDifferenceFile.close()
	regionsToDifferencesFile = open(regionsToDifferencesFileName)
	windowsFile = open(windowsFileName)
	windowsReadsMediansFile = open(windowsReadsMediansFileName)
	outputFile = open(outputFileName, 'w+')
	[windowLocation, windowMedian] = getNextWindowInfo(windowsFile, windowsReadsMediansFile)

	for line in regionsToDifferencesFile:
		# Iterate through regions and find the features for each of the corresponding sequence differences
		lineElements = line.split("\t")
		if len(lineElements) < 5:
			# There are no sequence differences for the current region, so do not consider it
			continue
		regionLocation = (lineElements[1], int(lineElements[2]), int(lineElements[3]))
		DNaseLocation = (regionLocation[0], regionLocation[1] + regionDistance, regionLocation[2] - regionDistance)

		while windowLocation[0] < DNaseLocation[0]:
			# Iterate through windows until a window on the right chromosome has been reached
			[windowLocation, windowMedian] = getNextWindowInfo(windowsFile, windowsReadsMediansFile)
		while windowLocation[1] < DNaseLocation[1]:
			# Iterate through windows until the DNase site has been reached
			[windowLocation, windowMedian] = getNextWindowInfo(windowsFile, windowsReadsMediansFile)
		if windowLocation != DNaseLocation:
			print "Problem!"
		windowDistance = DNaseLocation[2] - DNaseLocation[1]

		for seqDiffIndexStr in lineElements[4:]:
			# Iterate through the sequence differences associated with the current region and get the median number of reads in their region and length of their region for each
			outputFile.write(str(windowMedian) + "\t" + str(windowDistance) + "\n")

	regionsToDifferencesFile.close()
	windowsFile.close()
	windowsReadsMediansFile.close()
	outputFile.close()


if __name__=="__main__":
   import sys
   sequenceDifferenceFileName = sys.argv[1] # Name of file with the sequence differences
   regionsToDifferencesFileName = sys.argv[2] # Name of file with the regions mapped to their corresponding sequence differences sequence differences
   windowsFileName = sys.argv[3]
   windowsReadsMediansFileName = sys.argv[4]
   regionDistance = int(sys.argv[5])
   outputFileName = sys.argv[6]

   getReadsForSeqDiffRegion(sequenceDifferenceFileName, regionsToDifferencesFileName, windowsFileName, windowsReadsMediansFileName, regionDistance, outputFileName)
