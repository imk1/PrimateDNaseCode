def makeMACSScriptDNAse(fileNameListFileName, path, outpath, genomeFileName, shift, outputFileName):
	# Creates a script that sorts files from a list
	fileNameListFile = open(fileNameListFileName)
	genomeFile = open(genomeFileName)
	outputFile = open(outputFileName, 'w+')
	for line in fileNameListFile:
		# Iterate through lines of the file and make a script that runs MACS on them
		if "input" in line:
			# The current line is an input file, so do not call peaks
			genomeFile.readline()
			continue
		fileName = path + line.strip()
		genome = int(genomeFile.readline().strip())
		fileNameElements = line.strip().split("_")
		experimentName = fileNameElements[0] + "_" + fileNameElements[1] + "_" + fileNameElements[2] + "_" + fileNameElements[3][len(fileNameElements[3])-1]
		# Do NOT use the broad setting for DNAse
		outputFile.write("macs2 callpeak -t " + fileName + " -n " + outpath + experimentName + " -f BED -g " + str(genome) + " -q 1e-5 -shiftsize " + str(shift) + " --keep-dup=all" + "\n")
	fileNameListFile.close()
	outputFile.close()

if __name__=="__main__":
    import sys
    fileNameListFileName = sys.argv[1]
    path = sys.argv[2]
    outpath = sys.argv[3]
    genomeFileName = sys.argv[4]
    shift = int(sys.argv[5])
    outputFileName = sys.argv[6]
    makeMACSScriptDNAse(fileNameListFileName, path, outpath, genomeFileName, shift, outputFileName)
