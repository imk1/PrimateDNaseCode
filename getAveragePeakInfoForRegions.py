def getNextPeak(currentPeakLine):
	# Gets the information for the next peak
	currentPeakLineElements = currentPeakLine.split("\t")
	currentPeakLoc = (currentPeakLineElements[0], int(currentPeakLineElements[1]), int(currentPeakLineElements[2]))
	currentPeakHeight = float(currentPeakLineElements[6])
	currentPeakpVal = float(currentPeakLineElements[7])
	return [currentPeakLoc, currentPeakHeight, currentPeakpVal]

def getAveragePeakInfoForRegions(regionsFileName, peaksFileName, outputFileName):
	# Get the average across bases in each region of the following quantities:
	# Column 1: Is the base in a peak? (Binary)
	# Column 2: What is the height of the peak that the base is in? (0 if not in a peak)
	# Column 3: What is the -log10(p-value) of the peak that the base is in? (0 if not in a peak)
	# ASSUMES THAT EACH BASE IS IN AT MOST 1 PEAK
	# ASSUMES THAT PEAKS AND REGIONS ARE SORTED BY CHROM, THEN START, THEN END
	regionsFile = open(regionsFileName)
	peaksFile = open(peaksFileName)
	outputFile = open(outputFileName, 'w+')
	[currentPeakLoc, currentPeakHeight, currentPeakpVal] = getNextPeak(peaksFile.readline())
	lastRegionPeakLocs = [] # Allows regions to overlap
	for line in regionsFile:
		# Get the peak data averages for each peak
		lineElements = line.split("\t")
		regionLoc = (lineElements[0], int(lineElements[1]), int(lineElements[2]))
		inPeakList = []
		peakHeightList = []
		peakpValList = []
		currentRegionPeakLocs = []
		for i in range(regionLoc[1], regionLoc[2]):
			# Iterate through bases and get the peak information for each base
			inPeak = 0
			peakHeight = 0
			peakpVal = 0
			overlapFound = False
			lastRegionPeakLocsIndex = 0
			for peakLoc in lastRegionPeakLocs[lastRegionPeakLocsIndex:]:
				# Iterate through the peaks from the last region to check if the current base overlaps
				if (regionLoc[0] == peakLoc[0]) and ((peakLoc[2] > i) and (peakLoc[1] <= i)):
					# The peak and the base overlap
					if peakLoc not in currentRegionPeakLocs:
						# The current peak is not in the list of peak locations
						currentRegionPeakLocs.append(peakLoc)
					inPeak = 1
					peakHeight = currentPeakHeight
					peakpVal = currentPeakpVal
					overlapFound = True
				else:
					lastRegionPeakLocsIndex = lastRegionPeakLocsIndex + 1
			if overlapFound == False:
				# The current base is not in any of the peaks from the previous region
				while regionLoc[0] > currentPeakLoc[0]:
					# Iterate through the peaks until a peak in the same chromosome as the base is reached
					[currentPeakLoc, currentPeakHeight, currentPeakpVal] = getNextPeak(peaksFile.readline())
				while (regionLoc[0] == currentPeakLoc[0]) and (currentPeakLoc[2] <= i):
					# Iterate through peaks until a peak that does not occur earlier than the base is reached
					[currentPeakLoc, currentPeakHeight, currentPeakpVal] = getNextPeak(peaksFile.readline())
				if (regionLoc[0] == currentPeakLoc[0]) and ((currentPeakLoc[2] > i) and (currentPeakLoc[1] <= i)):
					# The peak and the base overlap
					if currentPeakLoc not in currentRegionPeakLocs:
						# The current peak is not in the list of peak locations
						currentRegionPeakLocs.append(currentPeakLoc)
					inPeak = 1
					peakHeight = currentPeakHeight
					peakpVal = currentPeakpVal
			inPeakList.append(inPeak)
			peakHeightList.append(peakHeight)
			peakpValList.append(peakpVal)
		inPeakMean = numpy.mean(numpy.array(inPeakList))
		peakHeightMean = numpy.mean(numpy.array(peakHeightList))
		peakpValMean = numpy.mean(numpy.array(peakpValList))
		outputFile.write(str(inPeakMean) + "\t" + str(peakHeightMean) + "\t" + str(peakpValMean) + "\n")
		lastRegionPeakLocs = currentRegionPeakLocs
	regionsFile.close()
	peaksFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   import numpy
   regionsFileName = sys.argv[1] 
   peaksFileName = sys.argv[2]
   outputFileName = sys.argv[3]
   getAveragePeakInfoForRegions(regionsFileName, peaksFileName, outputFileName)
