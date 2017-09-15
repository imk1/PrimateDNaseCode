def addNamesToBed(inputFileName, outputFileName):
	# Add a name column to a bed file
	inputFile = open(inputFileName)
	outputFile = open(outputFileName, 'w+')
	regNum = 0
	for line in inputFile:
		# Iterate through the lines of the bed file and add a name to each
		regNum = regNum + 1 # REGIONS ARE 1-INDEXED
		lineElements = line.split("\t")
		regName = "Region" + str(regNum) + "_" + lineElements[0] + "_" + lineElements[1] + "_" + lineElements[2].strip()
		outputFile.write(lineElements[0] + "\t" + lineElements[1] + "\t" + lineElements[2].strip() + "\t" + regName + "\n")
	inputFile.close()
	outputFile.close()

if __name__=="__main__":
	import sys
	inputFileName = sys.argv[1]
	outputFileName = sys.argv[2]
        addNamesToBed(inputFileName, outputFileName)
