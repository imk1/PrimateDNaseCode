def makeRegionList(regionFileName):
	# Make a list of all of the regions
	regionFile = open(regionFileName)
	regionList = []
	for line in regionFile:
		# Iterate through the regions and make an entry in the list for each
		lineElements = line.split("\t")
		regionInfo = (lineElements[0], int(lineElements[1]), int(lineElements[2]))
		regionList.append(regionInfo)
	regionFile.close()
	return regionList

def makeTFList(TFListFileName):
	# Make a list of TFs from the TF file
	TFListFile = open(TFListFileName)
	TFList = []
	for line in TFListFile:
		# Iterate through the TFs and add each to the list
		TFList.append(string.upper(line.strip()))
	TFListFile.close()
	return TFList

def makeTFRegionClustMat(FIMOFileNameListFileName, TFListFileName, regionList):
	# Makes a matrix that is (# regions) x (# TFs) in which entry (i,j) is a 1 if the TF j has a motif in the region i
	# Having a motif in at least 1 FIMO file is sufficient
	TFRegionClustMat = []
	TFList = makeTFList(TFListFileName)
	for i in range(len(regionList)):
		# Make a row in the matrix for each region
		TFRegionClustMat.append([])
		for TF in TFList:
			# Make an entry in the matrix for each TF in the region and initialize the entry to 0
			TFRegionClustMat[i].append(False)
	FIMOFileNameListFile = open(FIMOFileNameListFileName)
	for line in FIMOFileNameListFile:
		# Iterate through the FIMO files and change 0s to 1s for region, TF entries in them
		FIMOFile = open(line.strip())
		FIMOFile.readline() # Remove the header
		for line in FIMOFile:
			# Iterate through the lines of the FIMO file and modify the matrix appropriately
			# ASSUMES THAT THE "sequence name" COLUMN IS OF THE FORM "[string]_[chrom]_[start]_[end]"
			# ASSUMES THAT REGIONS ARE 1-INDEXED
			lineElements = line.split("\t")
			regionInfo = lineElements[1].split("_")
			regionTuple = (regionInfo[1], int(regionInfo[2]), int(regionInfo[3]))
			regionNum = regionList.index(regionTuple) # regionNum IS 0-INDEXED
			TFNum = TFList.index(string.upper(lineElements[0]))
			TFRegionClustMat[regionNum][TFNum] = True
		FIMOFile.close()
	return TFRegionClustMat

def writeMat(TFRegionClustMat, outputFileName):
	# Write the matrix to the output file
	outputFile = open(outputFileName, 'w+')
	for regionRow in TFRegionClustMat:
		# Write the TF information for each region to the output file
		for entry in regionRow:
			# Iterate through the entries for the TF and write each to the output file
			if entry == True:
				# The TF has a motif in the region in at least 1 FIMO file
				outputFile.write("1\t")
			else:
				outputFile.write("0\t")
		outputFile.write("\n")
	outputFile.close()

if __name__=="__main__":
   import sys
   import string
   FIMOFileNameListFileName = sys.argv[1] 
   TFListFileName = sys.argv[2]
   regionFileName = sys.argv[3]
   outputFileName = sys.argv[4]
   regionList = makeRegionList(regionFileName)
   TFRegionClustMat = makeTFRegionClustMat(FIMOFileNameListFileName, TFListFileName, regionList)
   writeMat(TFRegionClustMat, outputFileName)
