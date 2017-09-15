def getCurrentLineNum(currentLineNumLine, lineNumsCl, lineNumsSplit, lineNumsEl):
	# Get the current line number that will be kept
	if currentLineNumLine == "":
		# At the end of the file, so stop
		return -1
	currentLineNumLineCols = currentLineNumLine.split("\t")
	currentLineNum = currentLineNumLineCols[lineNumsCl]
	if lineNumsSplit != "":
		# The column with the line numbers needs to be split
		currentLineNumElements = currentLineNumLineCols[lineNumsCl].strip().split(lineNumsSplit)
		currentLineNum = currentLineNumElements[lineNumsEl]
	return int(currentLineNum.strip())


def filterPeakWindowsLineNums(peakWindowsFileName, lineNumsFileName, zeroIndex, lineNumsCl, lineNumsSplit, lineNumsEl, outputFileName):
	# Write the peak windows with the designated numbers to the output file
	peakWindowsFile = open(peakWindowsFileName)
	lineNumsFile = open(lineNumsFileName)
	lineIndex = 0
	lineNums = []
	for lineNumsLine in lineNumsFile:
		# Iterate through the line numbers and put them in a list
		currentLineNum = getCurrentLineNum(lineNumsLine, lineNumsCl, lineNumsSplit, lineNumsEl)
		if zeroIndex == 1:
			# Line numbers are 0-indexed, so do not subtract 1
			lineNums.append(currentLineNum)
		else:
			lineNums.append(currentLineNum - 1)
	outputFile = open(outputFileName, 'w+')
	for line in peakWindowsFile:
		# Iterate through windows and record those that should be kept
		if lineIndex in lineNums:
			# Keep the current line
			outputFile.write(line)
			currentLineNum = getCurrentLineNum(lineNumsFile.readline(), lineNumsCl, lineNumsSplit, lineNumsEl)
		lineIndex = lineIndex + 1
	peakWindowsFile.close()
	lineNumsFile.close()
	outputFile.close()


if __name__=="__main__":
   import sys
   peakWindowsFileName = sys.argv[1] # Name of file with the peaks' windows
   lineNumsFileName = sys.argv[2] # Name of file with the line numbers to include
   outputFileName = sys.argv[3] # Name of file where the filtered windows will be written
   zeroIndex = int(sys.argv[4])

   lineNumsCl = 0
   lineNumsSplit = ""
   lineNumsEl = 0
   if len(sys.argv) > 5:
	# A column number has been provided by the user
	lineNumsCl = int(sys.argv[5]) # 0-INDEXED
	if len(sys.argv) > 6:
		# The column with the line numbers will need to be split
		lineNumsSplit = sys.argv[6]
		if len(sys.argv) > 7:
			# The element with the line number has been provided by the user
			lineNumsEl = int(sys.argv[7]) # 0-INDEXED

   filterPeakWindowsLineNums(peakWindowsFileName, lineNumsFileName, zeroIndex, lineNumsCl, lineNumsSplit, lineNumsEl, outputFileName)
