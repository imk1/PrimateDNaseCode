def makePeakWindows(peakFileName, overlapDistMin, discardDist, outputFileName):
	# Makes windows based on a unified list of peaks
	# ASSUMES THAT PEAKS ARE SORTED BY CHROM, START, END
	peakFile = open(peakFileName)
	outputFile = open(outputFileName, 'w+')
	lastPeakLine = peakFile.readline()
	lastPeakLineElements = lastPeakLine.split("\t")
	lastPeak = [lastPeakLineElements[0], int(lastPeakLineElements[1]), int(lastPeakLineElements[2])]
	currentWindow = lastPeak
	windowDiscarded = False

	for line in peakFile:
		# Iterate through peaks and define windows for each peak
		# Each peak is part of the same window as the last peak if at least overlapDistMin of 1 peak overlaps
		# Peaks/windows are discarded if consecutive peaks do not overlap at least overlapDistMin but are within discardDist of each other
		lineElements = line.split("\t")
		currentPeak = [lineElements[0], int(lineElements[1]), int(lineElements[2])]
		if windowDiscarded == True:
			# The last window has been discard, so either discard the current peak or start a new window
			if (currentPeak[0] != currentWindow[0]) and ((currentPeak[0] != "chrX") and (currentPeak[0] != "chrY")):
				# Start a new window
				windowDiscarded = False
				currentWindow = currentPeak
				lastPeak = currentPeak
				continue
			elif (currentPeak[1] - currentWindow[2] > discardDist) and ((currentPeak[0] != "chrX") and (currentPeak[0] != "chrY")):
				# Start a new window
				windowDiscarded = False
				currentWindow = currentPeak
				lastPeak = currentPeak
				continue
			else:
				currentWindow[2] = currentPeak[2]
				lastPeak = currentPeak
				continue

		if currentPeak[0] != currentWindow[0]:
			# The peak is on a new chromosome, so record the current window and start a new window
			outputFile.write(currentWindow[0] + "\t" + str(currentWindow[1]) + "\t" + str(currentWindow[2]) + "\n")
			currentWindow = currentPeak
			lastPeak = currentPeak
			continue

		overlapDist = currentPeak[1] - lastPeak[2]
		if (currentPeak[0] == "chrX") or (currentPeak[0] == "chrY"):
			# Remove sex chromosomes because population is mix of males and females
			windowDiscarded == True
		elif overlapDist < 0:
			# There is some overlap, so include the current peak in the window
			currentWindow[2] = max([currentPeak[2], currentWindow[2]])
			if abs(overlapDist) < overlapDistMin:
				# There is not enough overlap
				windowDiscarded = True
		elif overlapDist <= discardDist:
			# The peaks are too close to each other
			windowDiscarded = True
		else:
			outputFile.write(currentWindow[0] + "\t" + str(currentWindow[1]) + "\t" + str(currentWindow[2]) + "\n")
			currentWindow = currentPeak
		lastPeak = currentPeak

	if windowDiscarded == False:
		# Record the final window
		outputFile.write(currentWindow[0] + "\t" + str(currentWindow[1]) + "\t" + str(currentWindow[2]) + "\n")
	peakFile.close()
	outputFile.close()


if __name__=="__main__":
   import sys
   peakFileName = sys.argv[1] # Name of file with the peaks
   overlapDistMin = int(sys.argv[2]) # Number of bases of peak overlap required to be considered part of the same window
   discardDist = int(sys.argv[3]) # Distance within which 2 peaks that do not overlap sufficiently are discarded
   outputFileName = sys.argv[4]

   makePeakWindows(peakFileName, overlapDistMin, discardDist, outputFileName)
