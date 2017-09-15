def filterPeakWindows(windowsFileName, minLength, maxLength, outputFileName):
	# Filter peak windows that are shorter than the minimum length or longer than the maximum length
	windowsFile = open(windowsFileName)
	outputFile = open(outputFileName, 'w+')

	for line in windowsFile:
		# Iterate through the windows and test whether each window is in the appropriate length range
		lineElements = line.split("\t")
		if (int(lineElements[2]) - int(lineElements[1]) >= minLength) and (int(lineElements[2]) - int(lineElements[1]) <= maxLength):
			# The window size is in the appropriate range, so keep the window
			outputFile.write(line)

	windowsFile.close()
	outputFile.close()


if __name__=="__main__":
   import sys
   windowsFileName = sys.argv[1] # Name of file with the peaks
   minLength = int(sys.argv[2]) # Number of bases of peak overlap required to be considered part of the same window
   maxLength = int(sys.argv[3]) # Distance within which 2 peaks that do not overlap sufficiently are discarded
   outputFileName = sys.argv[4]

   filterPeakWindows(windowsFileName, minLength, maxLength, outputFileName)
