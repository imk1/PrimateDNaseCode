def filterListBinaries (listFileName, binariesFileName, outputFileName):
	# Filter a list based on binaries, where all lines at indexes of lines with 1s in the binaries file are kept
	listFile = open(listFileName)
	binariesFile = open(binariesFileName)
	outputFile = open(outputFileName, 'w+')

	for line in binariesFile:
		# Iterate through the binaries and keep the corresponding line in the list if the binary is 1
		listLine = listFile.readline()
		if int(line.strip()) == 1:
			# The current line in the list should be kept
			outputFile.write(listLine)

	listFile.close()
	binariesFile.close()
	outputFile.close()


if __name__=="__main__":
   import sys
   listFileName = sys.argv[1] 
   binariesFileName = sys.argv[2]
   outputFileName = sys.argv[3]

   filterListBinaries (listFileName, binariesFileName, outputFileName)
