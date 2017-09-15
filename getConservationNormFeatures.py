def getConservationNormFeatures(conservFileName, conservBackgroundFileName, regionsToDifferencesFileName, outputFileName):
	# Get the normalized conservation feature for each sequence difference, which is conservation/(region conservation)
	# ASSUMES THAT THERE ARE NO SEQUENCE DIFFERENCES IN MULTIPLE REGIONS
	# ASSUMES THAT THE INFORMATION IN ALL FILES IS SORTED BY CHROM, START, END

	regionsToDifferencesFile = open(regionsToDifferencesFileName)
	conservFile = open(conservFileName)
	conservLines = conservFile.readlines()
	conservFile.close()
	conservBackgroundFile = open(conservBackgroundFileName)
	outputFile = open(outputFileName, 'w+')

	for line in regionsToDifferencesFile:
		# Iterate through regions and find the features for each of the corresponding sequence differences
		lineElements = line.split("\t")
		backgroundConserv = float(conservBackgroundFile.readline().strip())
		if len(lineElements) < 5:
			# There are no sequence differences for the current region, so do not consider it
			continue

		for seqDiffIndexStr in lineElements[4:]:
			# Iterate through the sequence differences associated with the current region and get the conservation features for each
			seqDiffIndex = int(seqDiffIndexStr.strip())
			seqDiffConserv = float(conservLines[seqDiffIndex].strip())
			conserv = seqDiffConserv/backgroundConserv
			outputFile.write(str(conserv) + "\n")

	regionsToDifferencesFile.close()
	conservBackgroundFile.close()
	outputFile.close()


if __name__=="__main__":
   import sys
   import math
   conservFileName = sys.argv[1] # Name of file with the conservation for the regions surrounding the sequence differences
   conservBackgroundFileName = sys.argv[2] # Name of file with the conservation for the DNase hypersensitivity regions
   regionsToDifferencesFileName = sys.argv[3] # Name of file with the regions mapped to their corresponding sequence differences sequence differences
   outputFileName = sys.argv[4]

   getConservationNormFeatures(conservFileName, conservBackgroundFileName, regionsToDifferencesFileName, outputFileName)
