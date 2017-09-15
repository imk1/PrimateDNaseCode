def makeaxtToMafScript(axtFileNameListFileName, path, outputFileName):
	# Make a script that will convert axt files to maf files
	axtFileNameListFile = open(axtFileNameListFileName)
	outputFile = open(outputFileName, 'w+')
	for line in axtFileNameListFile:
		# Iterate through the names of the axt files and make a maf conversion file for each
		lineElements = line.split(".")
		chromSizesFileName = lineElements[1] + ".chrom.sizes"
		otherSpeciesChromSizesFileName = lineElements[2] + ".chrom.sizes"
		mafFileName = lineElements[0] + "." + lineElements[1] + "." + lineElements[2] + "." + lineElements[3] + ".maf"

		outputFile.write("axt_to_maf.py "  + lineElements[1] + ":" + path + chromSizesFileName + " " + lineElements[2] + ":" + path + otherSpeciesChromSizesFileName + " < " + path + line.strip() + " > " + path + mafFileName + "\n")
	axtFileNameListFile.close()
	outputFile.close()


if __name__=="__main__":
	import sys
	axtFileNameListFileName = sys.argv[1]
	path = sys.argv[2]
	outputFileName = sys.argv[3]
                        
	makeaxtToMafScript(axtFileNameListFileName, path, outputFileName)
