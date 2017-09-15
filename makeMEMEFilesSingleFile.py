def getNextMotifStart(PWMLines, currentLineIndex):
	# Get the start of the next motif
	while (currentLineIndex < len(PWMLines)) and (len(PWMLines[currentLineIndex].strip()) == 0):
		# Iterate through the blank lines between PWMs and increment currentLineIndex for each blank line
		currentLineIndex = currentLineIndex + 1
	return currentLineIndex

def makeMEMEFilesSingleFile (PWMFileName, outputFileNamePrefix, outputFileAllName):
	# Convert PWM file into MEME file
	PWMFile = open(PWMFileName)
	PWMLines = PWMFile.readlines()
	PWMFile.close()
	outputFileAll = open(outputFileAllName, 'w+')
	outputFileAll.write("MEME version 4.9.0\n\n")
	outputFileAll.write("ALPHABET= ACGT\n\n")
	outputFileAll.write("strands: +-\n\n")
	currentLineIndex = 0
	lastMotifName = ""
	while currentLineIndex < len(PWMLines):
		# Iterate through the PWMs and make a MEME file for each
		TFLine = PWMLines[currentLineIndex + 1]
		TFLineElements = TFLine.split("\t")
		TFName = TFLineElements[1].strip().upper()
		motifLine = PWMLines[currentLineIndex + 3]
		motifLineElements = motifLine.split("\t")
		motifName = motifLineElements[1].strip()
		if motifName == lastMotifName:
			# Skip the current motif because it has already been recorded
			currentLineIndex = getNextMotifStart(PWMLines, currentLineIndex + 7 + numPos)
			continue
		numPos = 0
		while len(PWMLines[currentLineIndex + 7 + numPos].strip()) > 0:
			# Iterate through lines with PWM positions and count the number of such lines
			# ASSUMES THAT THERE IS A BLANK LINE BETWEEN ALL PWMS AND A BLANK LINE AT THE END OF THE FILE
			numPos = numPos + 1
		if numPos == 0:
			# There is no motif information, so continue
			currentLineIndex = getNextMotifStart(PWMLines, currentLineIndex + 7 + numPos)
			continue
		outputFileName = outputFileNamePrefix + "_" + TFName + "_" + motifName
		outputFile = open(outputFileName, 'w+')
		outputFile.write("MEME version 4.9.0\n\n")
		outputFile.write("ALPHABET= ACGT\n\n")
		outputFile.write("strands: +-\n\n")
		outputFile.write("MOTIF " + TFName + "\n")
		outputFileAll.write("MOTIF " + TFName + "\n")
		outputFile.write("letter-probability matrix: alength= 4 w= " + str(numPos) + "\n")
		outputFileAll.write("letter-probability matrix: alength= 4 w= " + str(numPos) + "\n")
		for line in PWMLines[currentLineIndex + 7:currentLineIndex + 7 + numPos]:
			# Iterate through base probabilities at each position and write the probabilities to the output file
			lineElements = line.split("\t")
			for prob in lineElements[1:]:
				# Itereate through probabilities and write each to the outputFile
				outputFile.write(prob.strip())
				outputFileAll.write(prob.strip())
				outputFile.write("\t")
				outputFileAll.write("\t")
			outputFile.write("\n")
			outputFileAll.write("\n")
		outputFileAll.write("\n")
		outputFile.close()
		lastMotifName = motifName
		currentLineIndex = getNextMotifStart(PWMLines, currentLineIndex + 7 + numPos)
	outputFileAll.close()

if __name__=="__main__":
   import sys
   PWMFileName = sys.argv[1] 
   outputFileNamePrefix = sys.argv[2]
   outputFileAllName = sys.argv[3]
   makeMEMEFilesSingleFile (PWMFileName, outputFileNamePrefix, outputFileAllName)
	
