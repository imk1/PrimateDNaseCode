def getUniqueMers(mersFileNameListFileName, outputFileName):
	# Gets a list of unique mers from files in which each file has a list of unique mers
	merList = []
	mersFileNameListFile = open(mersFileNameListFileName)
	for mersFileName in mersFileNameListFile:
		# Iterate through the files with the mers and find those that appear only once across files
		mersFile = open(mersFileName.strip())
		for line in mersFile:
			# Iterate through the mers and find those that are not yet in the list while removing those that are already in the list
			if line.strip() in merList:
				# Remove the current mer from the list because it appears more than once
				merList.remove(line.strip())
			else:
				merList.append(line.strip())
		mersFile.close()
	mersFileNameListFile.close()
	print len(merList)
	outputFile = open(outputFileName, 'w+')
	outputFile.write(str(len(merList)) + "\n")
	for mer in merList:
		# Iterate through the mers and write each mer to the output file
		outputFile.write(mer + "\n")
	outputFile.close()

if __name__=="__main__":
   import sys
   mersFileNameListFileName = sys.argv[1] 
   outputFileName = sys.argv[2]
   getUniqueMers(mersFileNameListFileName, outputFileName)
