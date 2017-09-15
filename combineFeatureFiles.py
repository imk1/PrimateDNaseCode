def combineFeatureFiles(sequenceDifferenceFileName, featureFileNameListFileName, outputFileName):
	# Combines files with features from the same sequence differences
	# THE NUMBER OF ROWS IN EVERY FILE SHOULD BE THE SAME AS THE NUMBER OF SEQUENCE DIFFERNCES
	sequenceDifferenceFile = open(sequenceDifferenceFileName)
	featureFileNameListFile = open(featureFileNameListFileName)
	outputFile = open(outputFileName, 'w+')
	featureFileList = []
	for featureFileName in featureFileNameListFile:
		# Iterate through feature files and add each to the list
		featureFile = open(featureFileName.strip())
		featureFileList.append(featureFile)
	featureFileNameListFile.close()

	for line in sequenceDifferenceFile:
		# Iterate through the sequence differences and add their feature information to the output file
		lineElements = line.split("\t")
		outputFile.write(lineElements[0] + "\t" + lineElements[1] + "\t" + lineElements[2].strip())
		for featureFile in featureFileList:
			# Iterate through the feature files and write the appropriate information to the output file
			featureLine = featureFile.readline()
			featureLineElements = featureLine.split("\t")
			for feat in featureLineElements:
				# Write each feature to the output file
				outputFile.write("\t" + feat.strip())
		outputFile.write("\n")

	sequenceDifferenceFile.close()
	for featureFile in featureFileList:
		# Close all of the feature files
		featureFile.close()
	outputFile.close()


if __name__=="__main__":
   import sys
   sequenceDifferenceFileName = sys.argv[1] # Name of file with the sequence difference locations
   featureFileNameListFileName = sys.argv[2] # Name of file with list of the file names with features
   outputFileName = sys.argv[3]

   combineFeatureFiles(sequenceDifferenceFileName, featureFileNameListFileName, outputFileName)
