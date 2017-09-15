def makeFIMOScript(fastaFileName, GCContentFileNamePrefix, outputFileName, FIMOOutputFileNamePrefix, PWMFileName, regionFileName):
	# Separate fastas into their own file and make a script that will run FIMO on each fasta file separately
	# Fastas are from substitution files, so make sure that each fasta is matched with the proper GC content file
	# ASSUMES THAT ALL FILES ARE SORTED BY REGION CHROM, THEN REGION START, AND THEN REGION END
	# ASSUMES THAT THERE ARE NO SEQUENCE DIFFERENCES THAT AFFECT MULTIPLE REGIONS
	fastaFile = open(fastaFileName)
	fastaFileNameParts = fastaFileName.split("/")
	fastaFileNameEnd = fastaFileNameParts[len(fastaFileNameParts) - 1]
	outputFile = open(outputFileName, 'w+')
	regionFile = open(regionFileName)
	regionLine = regionFile.readline()
	regionLineElements = regionLine.split("\t")
	regionChrom = regionLineElements[0]
	regionStart = int(regionLineElements[1])
	regionEnd = int(regionLineElements[2].strip())
	regionLineCount = 1
	fastaOutFileName = ""
	fastaOutFile = ""
	fastaLineCount = 0
	for line in fastaFile:
		# Iterate through the lines of the fasta file, write them to the appropriate output file, and add to the script
		# ASSUMES THAT THE FIRST LINE STARTS WITH >
		if line[0] == ">":
			if fastaOutFileName != "":
				# Close the last fasta file
				fastaOutFile.close()
			lineElements = line.split("_")
			while (lineElements[1] != regionChrom) or ((int(lineElements[2]) != regionStart) or (int(lineElements[3]) != regionEnd)):
				# Iterate through regions until the region corresponding to the current fasta has been found
				# ASSUMES THAT THERE IS A REGION FOR EVERY FASTA
				fastaLineCount = 0
				regionLine = regionFile.readline()
				regionLineElements = regionLine.split("\t")
				regionChrom = regionLineElements[0]
				regionStart = int(regionLineElements[1])
				regionEnd = int(regionLineElements[2].strip())
				regionLineCount = regionLineCount + 1
			fastaLineCount = fastaLineCount + 1
			fastaOutFileName = fastaFileName + str(regionLineCount) + "-" + str(fastaLineCount)
			GCContentFileName = GCContentFileNamePrefix + str(regionLineCount)
			FIMOOutputFileName = FIMOOutputFileNamePrefix + str(regionLineCount) + "-" + str(fastaLineCount)
			fastaOutFile = open(fastaOutFileName, 'w+')
			fastaOutFileNameScript = fastaOutPath + fastaFileNameEnd + str(regionLineCount) + "-" + str(fastaLineCount)
			outputFile.write("fimo --bgfile " + GCContentFileName + " --max-stored-scores 10000000 --o " + FIMOOutputFileName + " --qv-thresh --thresh 0.05 " + PWMFileName + " " + fastaOutFileNameScript + "\n")
		fastaOutFile.write(line)
	fastaOutFile.close()
	regionFile.close()
	outputFile.close()
	fastaFile.close()

if __name__=="__main__":
   import sys
   fastaFileName = sys.argv[1]
   fastaOutPath = sys.argv[2]
   GCContentFileNamePrefix = sys.argv[3]
   outputFileName = sys.argv[4]
   FIMOOutputFileNamePrefix = sys.argv[5]
   PWMFileName = sys.argv[6]
   regionFileName = sys.argv[7]
   makeFIMOScript(fastaFileName, GCContentFileNamePrefix, outputFileName, FIMOOutputFileNamePrefix, PWMFileName, regionFileName)
