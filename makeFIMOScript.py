def makeFIMOScript(fastaFileName, fastaOutPath, GCContentFileNamePrefix, outputFileName, FIMOOutputFileNamePrefix, PWMFileName):
	# Separate fastas into their own file and make a script that will run FIMO on each fasta file separately
	fastaFile = open(fastaFileName)
	fastaFileNameParts = fastaFileName.split("/")
	fastaFileNameEnd = fastaFileNameParts[len(fastaFileNameParts) - 1]
	outputFile = open(outputFileName, 'w+')
	fastaLineCount = 0
	fastaOutFileName = ""
	fastaOutFile = ""
	for line in fastaFile:
		# Iterate through the lines of the fasta file, write them to the appropriate output file, and add to the script
		# ASSUMES THAT THE FIRST LINE STARTS WITH >
		if line[0] == ">":
			if fastaLineCount > 0:
				# Close the last fasta file
				fastaOutFile.close()
			fastaLineCount = fastaLineCount + 1
			fastaOutFileName = fastaFileName + str(fastaLineCount)
			GCContentFileName = GCContentFileNamePrefix + str(fastaLineCount)
			FIMOOutputFileName = FIMOOutputFileNamePrefix + str(fastaLineCount)
			fastaOutFile = open(fastaOutFileName, 'w+')
			fastaOutFileNameScript = fastaOutPath + fastaFileNameEnd + str(fastaLineCount)
			outputFile.write("fimo --bgfile " + GCContentFileName + " --max-stored-scores 10000000 --o " + FIMOOutputFileName + " --qv-thresh --thresh 0.05 " + PWMFileName + " " + fastaOutFileNameScript + "\n") # Modified for fraser-server
		fastaOutFile.write(line)
	fastaOutFile.close()

if __name__=="__main__":
   import sys
   fastaFileName = sys.argv[1]
   fastaOutPath = sys.argv[2]
   GCContentFileNamePrefix = sys.argv[3]
   outputFileName = sys.argv[4]
   FIMOOutputFileNamePrefix = sys.argv[5]
   PWMFileName = sys.argv[6]
   makeFIMOScript(fastaFileName, fastaOutPath, GCContentFileNamePrefix, outputFileName, FIMOOutputFileNamePrefix, PWMFileName)
