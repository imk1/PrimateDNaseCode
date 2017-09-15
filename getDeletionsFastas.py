def makeFastaList(fastaFileName):
	# Create a list that maps the location in the fasta file to the fasta sequence at that location
	fastaList = []
	fastaSequence = ""
	fastaFile = open(fastaFileName)
	for line in fastaFile:
		# Iterates through the lines of the fasta file and concatenates the current sequence or adds the last sequence to the dictionary
		# ASSUMES THAT THE FIRST LINE OF THE FASTA FILE STARTS WITH ">"
		if line[0] == ">":
			# Starting a new fasta
			if fastaSequence != "":
				# Add the last fasta to the dictionary
				# ASSUMES THAT THERE IS AT LEAST 1 BASE FOR EVERY FASTA ENTRY
				fastaList.append(fastaSequence)
				fastaSequence = ""
		else:
			fastaSequence = fastaSequence + line.strip()
	fastaList.append(fastaSequence)
	fastaFile.close()
	return fastaList

def makeRegionList(regionFileName):
	# Makes a list of regions, where each entry is a tuple with the region's chromosome, start, end
	regionFile = open(regionFileName)
	regionList = []
	for line in regionFile:
		# Iterate through the lines of the region file and add the information from each line to the list of regions
		lineElements = line.split("\t")
		lineTuple = (lineElements[0], int(lineElements[1]), int(lineElements[2].strip()))
		regionList.append(lineTuple)
	regionFile.close()
	return regionList		

def getDeletionsFastas(fastaFileName, deletionFileName, deletionSortedFileName, outputFileName):
	# Find the location that corresponds to each deletion and write the deleted sequence and the location to the output file
	fastaList = makeFastaList(fastaFileName)
	deletionList = makeRegionList(deletionFileName)
	deletionSortedFile = open(deletionSortedFileName)
	outputFile = open(outputFileName, 'w+')
	for line in deletionSortedFile:
		# Iterate through the sorted elements of the deletion file and find the fasta sequence for each
		lineElements = line.split("\t")
		lineTuple = (lineElements[0], int(lineElements[1]), int(lineElements[2].strip()))
		lineIndex = deletionList.index(lineTuple)
		fastaSequence = fastaList[lineIndex]
		for locInfo in lineElements:
			# Write each part of the location information to the output file
			outputFile.write(locInfo.strip() + "\t")
		outputFile.write(fastaSequence)
		outputFile.write("\n")
	deletionSortedFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   fastaFileName = sys.argv[1] 
   deletionFileName = sys.argv[2] # Use coordinates for original species, not species with the sequences that will be added
   deletionSortedFileName = sys.argv[3] # Use coordinates for original species, not species with the sequences that will be added
   outputFileName = sys.argv[4]
   getDeletionsFastas(fastaFileName, deletionFileName, deletionSortedFileName, outputFileName)
