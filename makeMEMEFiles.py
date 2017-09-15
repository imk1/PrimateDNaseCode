def makeTFInfoDict(TFInfoFileName):
	# Make a dictionary that maps CIS-BP names to TF names
	TFInfoFile = open(TFInfoFileName)
	TFInfoDict = {}
	for line in TFInfoFile:
		# Iterate through the TF information and make a dictionary entry for each CIS-BP name
		lineElements = line.strip().split("\t")
		TFInfoDict[lineElements[3]] = lineElements[6]
	TFInfoFile.close()
	return TFInfoDict

def makeMEMEFiles (PWMFileName, outputFileNamePrefix, outputFileAll, motifStartLine, TFInfoDict, lastTFName, outputFile):
	# Convert PWM file into MEME file
	PWMFile = open(PWMFileName)
	PWMLines = PWMFile.readlines()
	PWMFile.close()
	TFName = ""
	if TFInfoDict is not None:
		# Use the dictionary to get the name of the TF
		PWMFileNameElements = PWMFileName.split("/")
		CISBPName = PWMFileNameElements[-1][0:-4] # REMOVE THE .txt
		TFName = TFInfoDict[CISBPName]
	else:
		# The name of the TF should be in the file
		TFLine = PWMLines[1]
		TFLineElements = TFLine.split("\t")
		TFName = TFLineElements[1].strip().upper()
	numPos = len(PWMLines) - motifStartLine
	if outputFileNamePrefix != "None":
		# Record the intermediate output file
		if TFName != lastTFName:
			# At a new TF, so make a new MEME file
			if lastTFName != "":
				# Close the previous ouput file
				outputFile.close()
			outputFileName = outputFileNamePrefix + "_" + TFName
			outputFile = open(outputFileName, 'w+')
			outputFile.write("MEME version 4.9.0\n\n")
			outputFile.write("ALPHABET= ACGT\n\n")
			outputFile.write("strands: +-\n\n")
		outputFile.write("MOTIF " + TFName + "\n")
		outputFile.write("letter-probability matrix: alength= 4 w= " + str(numPos) + "\n")
	outputFileAll.write("MOTIF " + TFName + "\n")
	outputFileAll.write("letter-probability matrix: alength= 4 w= " + str(numPos) + "\n")
	for line in PWMLines[motifStartLine:]:
		# Iterate through base probabilities at each position and write the probabilities to the output file
		lineElements = line.split("\t")
		for prob in lineElements[1:]:
			# Itereate through probabilities and write each to the outputFile
			if outputFileNamePrefix != "None":
				# Record the intermediate output file
				outputFile.write(prob.strip())
				outputFile.write("\t")
			outputFileAll.write(prob.strip())
			outputFileAll.write("\t")
		if outputFileNamePrefix != "None":
			# Record the intermediate output file
			outputFile.write("\n")
		outputFileAll.write("\n")
	outputFileAll.write("\n")
	if outputFileNamePrefix != "None":
		# Record the intermediate output file
		outputFile.write("\n")
	return [TFName, outputFile]

def makeMEMEFilesLoop (PWMFileNameListFileName, outputFileNamePrefix, outputFileAllName, motifStartLine, TFInfoFileName):
	# Convert all of the PWM files in a list into separate MEME files
	TFInfoDict = None
	if TFInfoFileName is not None:
		TFInfoDict = makeTFInfoDict(TFInfoFileName)
	PWMFileNameListFile = open(PWMFileNameListFileName)
	outputFileAll = open(outputFileAllName, 'w+')
	outputFileAll.write("MEME version 4.9.0\n\n")
	outputFileAll.write("ALPHABET= ACGT\n\n")
	outputFileAll.write("strands: +-\n\n")
	lastTFName = ""
	outputFile = None
	for line in PWMFileNameListFile:
		# Iterate through the PWM files and create a MEME file for each
		[lastTFName, outputFile] =\
			makeMEMEFiles(line.strip(), outputFileNamePrefix, outputFileAll, motifStartLine, TFInfoDict, lastTFName, outputFile)
	if outputFile is not None:
		# Close the final output file
		outputFile.close()
	PWMFileNameListFile.close()
	outputFileAll.close()

if __name__=="__main__":
   import sys
   PWMFileNameListFileName = sys.argv[1] 
   outputFileNamePrefix = sys.argv[2]
   outputFileAllName = sys.argv[3]
   motifStartLine = int(sys.argv[4]) # 7 for old version of CIS-BP, 1 for new version
   TFInfoFileName = None
   if len(sys.argv) > 5:
	   # There is a TF information file
	   TFInfoFileName = sys.argv[5]
   makeMEMEFilesLoop (PWMFileNameListFileName, outputFileNamePrefix, outputFileAllName, motifStartLine, TFInfoFileName)
	
