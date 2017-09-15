def getPostLiftoverReadCounts(initialRegionListFileName, unmappedRegionListFileName, infoFileName, outputFileName):
	# Filter the information to eliminate lines that were from regions that were not lifted over
	initialRegionListFile = open(initialRegionListFileName)
	unmappedRegionListFile = open(unmappedRegionListFileName)
	infoFile = open(infoFileName)
	outputFile = open(outputFileName, 'w+')
	allUnmappedFiltered = False
	currentUnmappedLine = unmappedRegionListFile.readline() # Remove current header
	if currentUnmappedLine == "":
		# All of the unmapped regions have been read (there were no unmapped regions)
		allUnmappedFiltered = True
	else:
		currentUnmappedLine = unmappedRegionListFile.readline()
		currentUnmappedLineElements = currentUnmappedLine.split("\t")
		currentUnmappedChrom = currentUnmappedLineElements[0]
		currentUnmappedStart = int(currentUnmappedLineElements[1])
		currentUnmappedEnd = int(currentUnmappedLineElements[2])
	for line in initialRegionListFile:
		# Iterate through the regions in the original file and identify those that were not mapped
		info = infoFile.readline()
		if allUnmappedFiltered == True:
			# All unmapped regions have been found, so write the current read count to the file
			outputFile.write(info)
			continue
		lineElements = line.split("\t")
		chrom = lineElements[0]
		start = int(lineElements[1])
		end = int(lineElements[2])
		if (chrom == currentUnmappedChrom) and ((start == currentUnmappedStart) and (end == currentUnmappedEnd)):
			# The current region was not mapped, so do not write the read count to the output file
			currentUnmappedLine = unmappedRegionListFile.readline() # Remove current header
			if currentUnmappedLine == "":
				# All of the unmapped regions have been read
				allUnmappedFiltered = True
			else:
				currentUnmappedLine = unmappedRegionListFile.readline()
				currentUnmappedLineElements = currentUnmappedLine.split("\t")
				currentUnmappedChrom = currentUnmappedLineElements[0]
				currentUnmappedStart = int(currentUnmappedLineElements[1])
				currentUnmappedEnd = int(currentUnmappedLineElements[2])
		else:
			outputFile.write(info)
	initialRegionListFile.close()
	unmappedRegionListFile.close()
	infoFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   initialRegionListFileName = sys.argv[1] 
   unmappedRegionListFileName = sys.argv[2]
   infoFileName = sys.argv[3]
   outputFileName = sys.argv[4]
   getPostLiftoverReadCounts(initialRegionListFileName, unmappedRegionListFileName, infoFileName, outputFileName)
