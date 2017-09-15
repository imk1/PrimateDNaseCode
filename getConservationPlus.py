def getPhastconsRegionInfo(PhastconsFile, PhastconsChrom, newChromReached):
	# Gets information about a region from a Phastcons file
	PhastconsChromLine = PhastconsFile.readline()
	PhastconsChromInfo = PhastconsChromLine.split(" ")
	if PhastconsChrom != PhastconsChromInfo[2].strip():
		# A new chromosome has been reached
		newChromReached = True
		PhastconsChrom = PhastconsChromInfo[2].strip()
	for i in range(6):
		# Remove additional header lines
		PhastconsFile.readline()
	PhastconsLine = PhastconsFile.readline()
	# ASSUMES THAT THERE IS CONSERVATION INFORMATION FOR AT LEAST ONE BASE IN REGION
	PhastconsLineElements = PhastconsLine.split("\t")
	return [PhastconsChrom, newChromReached, PhastconsLineElements]

def getConservationPlus(DNaseFileName, PhastconsFileName, conservationFileName):
	# Gets the average conservation score of each DNase region
	DNaseFile = open(DNaseFileName)
	PhastconsFile = open(PhastconsFileName)
	PhastconsFile.readline() # Remove header
	conservationFile = open(conservationFileName, 'w+')
	PhastconsIndex = 0
	PhastconsChrom = "chr0"
	PhastconsScores = []
	PhastconsLine = ""
	lastChrom = "chr0"
	for line in DNaseFile:
		# Iterate through DNase regions and find the average conservation score for each
		lineElements = line.split("\t")
		chrom = lineElements[0]
		if chrom != lastChrom:
			print chrom
			lastChrom = chrom
		start = int(lineElements[1])
		end = int(lineElements[2])
		# ASSUMES THAT NO REGIONS HAVE MULTIPLE PHASTCONS ENTRIES
		PhastconsChrom = "chr0"
		PhastconsIndex = 0
		stopReached = False
		while chrom > PhastconsChrom:
			# At a new chromosome, so read through Phastcons file until the next chromosome is reached
			newChromReached = False
			while newChromReached == False:
				# Have not reached a new chromosome, so keep reading the Phastcons file
				PhastconsLine = PhastconsFile.readline()
				if len(PhastconsLine) == 0:
					# There is no more conservation information, so do not record any conservation information for the region
					conservationFile.write(str(-1))
					conservationFile.write("\n")
					stopReached = True
					break
				PhastconsLineElements = PhastconsLine.split("\t")
				if PhastconsLineElements[0] == "#":
					# A new region has been reached
					[PhastconsChrom, newChromReached, PhastconsLineElements] = getPhastconsRegionInfo(PhastconsFile, PhastconsChrom, newChromReached)
				PhastconsIndex = int(PhastconsLineElements[0])
			if stopReached == True:
				# The conservation information for this region cannot be obtained, so continue
				break
		if stopReached == True:
			# The conservation information for this region cannot be obtained, so continue
			continue
		if PhastconsChrom > chrom:
			# DNase conservation information is not in Phastcons file because a new chromosome has been reached in the Phastcons file
			conservationFile.write(str(-1))
			conservationFile.write("\n")
			continue
		while PhastconsIndex < start:
			# Go through bases until the start is reached
			PhastconsLine = PhastconsFile.readline()
			PhastconsLineElements = PhastconsLine.split("\t")
			if len(PhastconsLine) == 0:
				# There is no more conservation information, so do not record any conservation information for the region
				conservationFile.write(str(-1))
				conservationFile.write("\n")
				stopReached = True
				break
			if PhastconsLineElements[0] == "#":
				# At a new starting index for conservation scores
				[PhastconsChrom, newChromReached, PhastconsLineElements] = getPhastconsRegionInfo(PhastconsFile, PhastconsChrom, newChromReached)
			PhastconsIndex = int(PhastconsLineElements[0]) # Modify PhastconsIndex appropriately
		if stopReached == True:
			# The conservation information for this region cannot be obtained, so continue
			continue
		if PhastconsIndex > start + 1: # PHASTCONS DOES NOT GET CONSERVATION FOR THE FIRST BASE
			# The DNase region is before the next conservation score
			if len(PhastconsScores) < PhastconsIndex - start:
				# The conservation read is after the DNase region and there is no sufficiently early conservation read
				conservationFile.write(str(-1))
				conservationFile.write("\n")
				continue
		# ASSUMES THAT NO REGIONS HAVE MULTIPLE PHASTCONS ENTRIES
		PhastconsScores = []
		PhastconsScores.append(float(PhastconsLineElements[1]))
		while PhastconsIndex < end:
			# ASSUMES THAT THERE ARE NO DNASE REGIONS THAT ARE COMPLETELY OVERLAPPING OTHER DNASE REGIONS
			# Gets conservation scores of every base in the DNase region
			PhastconsLine = PhastconsFile.readline()
			PhastconsLineElements = PhastconsLine.split("\t")
			if len(PhastconsLine) == 0:
				# There is no more conservation information, so do not record any conservation information for the region
				conservationFile.write(str(-1))
				conservationFile.write("\n")
				stopReached = True
				break
			if PhastconsLineElements[0] == "#":
				# At a new starting index for conservation scores
				PhastconsChromLine = PhastconsFile.readline()
				PhastconsChromInfo = PhastconsChromLine.split(" ")
				PhastconsChrom = PhastconsChromInfo[2].strip()
				PhastconsStartLine = PhastconsFile.readline()
				PhastconsStartLineElements = PhastconsStartLine.split(" ")
				PhastconsStartInfo = PhastconsStartLineElements[2].split("-")
				if (PhastconsChrom != chrom) or (int(PhastconsStartInfo[0]) != PhastconsIndex):
					# There is no more conservation information for the rest of the region, so do not compute its conservation
					print "Not enough conservation info.!"
					print end
					print PhastconsIndex
					conservationFile.write(str(-1))
					conservationFile.write("\n")
					for i in range(5):
						# Remove additional header lines
						PhastconsFile.readline()
					PhastconsLine = PhastconsFile.readline()
					# ASSUMES THAT THERE IS CONSERVATION INFORMATION FOR AT LEAST ONE BASE IN REGION
					PhastconsLineElements = PhastconsLine.split("\t")
					PhastconsIndex = int(PhastconsLineElements[0])
					stopReached = True
					break
			else:
				PhastconsScores.append(float(PhastconsLineElements[1]))
				PhastconsIndex = int(PhastconsLineElements[0])
		if stopReached == True:
			# The conservation information for this region cannot be obtained, so continue
			continue
		DNaseLength = end - start
		if len(PhastconsScores) == end - start:
			# There are conservation scores for every base in the DNase region
			averageScore = float(sum(PhastconsScores))/float(len(PhastconsScores))
			conservationFile.write(str(averageScore))
			conservationFile.write("\n")
		else:
			conservationFile.write(str(-1))
			conservationFile.write("\n")
	DNaseFile.close()
	PhastconsFile.close()
	conservationFile.close()

if __name__=="__main__":
    import sys
    DNaseFileName = sys.argv[1]
    PhastconsFileName = sys.argv[2]
    conservationFileName = sys.argv[3]
    getConservationPlus(DNaseFileName, PhastconsFileName, conservationFileName)
