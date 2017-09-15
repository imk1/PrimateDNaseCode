def getNextPeak(peaksFile):
	# Get the next peak from a peak file
	currentPeakLine = peaksFile.readline()
	currentPeakLineElements = currentPeakLine.split("\t")
	currentPeakCoord = (currentPeakLineElements[0], int(currentPeakLineElements[1]), int(currentPeakLineElements[2]))
	return currentPeakCoord

def getNumOverlappingPeaks(peaksFileNameListFileName, regionFileName, outputFileName):
	# Makes a table with 1 column for each sample and 1 row for each region
	# Each entry is the number of peaks from the sample that overlap with the region
	# ASSUMES THAT REGIONS AND PEAKS ARE SORTED BY CHROM, START, END
	regionFile = open(regionFileName)
	peaksFileNameListFile = open(peaksFileNameListFileName)
	peaksFileList = []
	currentPeakList = []
	for peaksFileName in peaksFileNameListFile:
		# Iterate through the peak files, put them in a list, and put their first peaks in a list
		peaksFile = open(peaksFileName.strip())
		peaksFileList.append(peaksFile)
		currentPeakList.append(getNextPeak(peaksFile))
	peaksFileNameListFile.close()
	outputFile = open(outputFileName, 'w+')
	for line in regionFile:
		# Iterate through the regions and find the number of peaks that overlap with each
		lineElements = line.split("\t")
		regionCoord = (lineElements[0], int(lineElements[1]), int(lineElements[2]))
		for i in range(len(currentPeakList)):
			# Iterate through the peaks and find how many overlap with the current region
			peakCount = 0
			while currentPeakList[i][0] < regionCoord[0]:
				# Get the next peak until a peak in the current region's chromosome has bene reached
				currentPeakList[i] = getNextPeak(peaksFileList[i])
			while (currentPeakList[i][0] == regionCoord[0]) and (currentPeakList[i][2] <= regionCoord[1]):
				# The current peak is on the same chromosome as the current region, so check if it overlaps
				# If not, continue searching through peaks on that chromosome for overlapping peaks
				currentPeakList[i] = getNextPeak(peaksFileList[i])
			while (currentPeakList[i][0] == regionCoord[0]) and ((currentPeakList[i][2] > regionCoord[1]) and (currentPeakList[i][1] < regionCoord[2])):
				# Iterate through the overlappling peaks and add to the peak count for each
				peakCount = peakCount + 1
				currentPeakList[i] = getNextPeak(peaksFileList[i])
			outputFile.write(str(peakCount) + "\t")
		outputFile.write("\n")
	regionFile.close()
	for peaksFile in peaksFileList:
		# Iterate through the peak files and close each one
		peaksFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   peaksFileNameListFileName = sys.argv[1] 
   regionFileName = sys.argv[2]
   outputFileName = sys.argv[3]
   getNumOverlappingPeaks(peaksFileNameListFileName, regionFileName, outputFileName)
