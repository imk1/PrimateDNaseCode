def getFIMOLocations(FIMOFileName):
	# Get the regions in a FIMO file
	# Returns an array where each entry has a region and the entries are (chromosome, start, end)
	FIMOFile = open(FIMOFileName)
	FIMOLocations = []
	for line in FIMOFile:
		# Iterate through the lines of the FIMO file and record the locations
		if line[0] == "#":
			# The current line is a header, so skip it
			continue
		lineElements = line.split("\t")
		locationElements = lineElements[1].split("_")
		currentLocation = (locationElements[1], int(locationElements[2]) + int(lineElements[2]), int(locationElements[2]) + int(lineElements[3]))
		FIMOLocations.append(currentLocation)
	FIMOFile.close()
	return FIMOLocations

def intersectFIMOBed (FIMOFileName, bedFileName, outputFileName):
	# Finds the intersecting regions of a FIMO file and a bed file
	# Outputs a table that is number of bed regions x number of FIMO regions, where there is a 1 when regions intersect
	FIMOLocations = getFIMOLocations(FIMOFileName)
	bedFile = open(bedFileName)
	outputFile = open(outputFileName, 'w+')
	for line in bedFile:
		# For each line of the bed file, create a row with indicators of which FIMO lines the region intersects
		lineElements = line.split("\t")
		chrom = lineElements[0]
		start = int(lineElements[1])
		end = int(lineElements[2])
		for FIMOLoc in FIMOLocations:
			# Iterate through FIMO locations to determine which locations intersect the BED location
			if FIMOLoc[0] == chrom:
				# The FIMO location and the bed file region are on the same chromosome
				if (((start <= FIMOLoc[1]) and (end >= FIMOLoc[1])) or ((end >= FIMOLoc[2]) and (start <= FIMOLoc[2]))) or ((start >= FIMOLoc[1]) and (end <= FIMOLoc[2])):
					# The regions overlap, so record a 1
					outputFile.write("1")
				else:
					outputFile.write("0")
			else:
				outputFile.write("0")
			outputFile.write("\t")
		outputFile.write("\n")
	bedFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   FIMOFileName = sys.argv[1] 
   bedFileName = sys.argv[2]
   outputFileName = sys.argv[3]
   intersectFIMOBed (FIMOFileName, bedFileName, outputFileName)
