def writeGenesequencessToFileUCSC(outputFile, geneName, chrom, start, end, sequencesForGeneIndexes):
    # Write a gene, its location, and the indexes of the sequences hypersensitivity sites near its TSS to the output file
    outputFile.write(geneName)
    outputFile.write("\t")
    outputFile.write(chrom)
    outputFile.write("\t")
    outputFile.write(str(start))
    outputFile.write("\t")
    outputFile.write(str(end))
    for di in sequencesForGeneIndexes:
	# Write each sequences index to the file
	outputFile.write("\t")
	outputFile.write(str(di))
    outputFile.write("\n")

def getSequenceInfoSpecific(sequenceInfo, sequenceIndex):
    # Gets the information about a specific sequence
    sequenceElements = sequenceInfo[sequenceIndex].split("\t")
    sequenceChrom = sequenceElements[0]
    sequenceStart = int(sequenceElements[1])
    sequenceEnd = int(sequenceElements[2])
    sequenceMiddle = sequenceStart + (float(sequenceEnd - sequenceStart) / float(2))
    return [sequenceChrom, sequenceMiddle, sequenceStart, sequenceEnd]

def associateRegionsToSequencesUCSCSingle(regionsFileName, sequencesFileName, outputFileName, nameCol, chromCol, startCol, endCol, singleFileName):
    # Find all of the sequences sites that overlap with each region
    # ASSUMES THAT TRANSCRIPTS FROM DIFFERENT MULTI-TRANSCRIPT GENES DO NOT OVERLAP, THAT ALL TRANSCRIPTS IN A GENE ARE CONSECUTIVE, AND THAT THERE ARE NO GENES WITH THE SAME NAME ON DIFFERENT CHROMOSOMES
    # ASSUMES THAT ALL GENES/REGIONS and DNASE SITES/SEQUENCES ARE SORTED BY CHROMOSOME, THEN START, THEN END
    # sequences hypersensitivity sites/sequences are 0-INDEXED
    regionsFile = open(regionsFileName)
    regionsInfo = regionsFile.readlines()
    regionsFile.close()
    sequencesFile = open(sequencesFileName)
    sequencesInfo = sequencesFile.readlines()
    sequencesFile.close()
    outputFile = open(outputFileName, 'w+')
    singleFile = open(singleFileName, 'w+')
    lastGenesIndex = -1
    chrom = ""
    startList = []
    start = 0
    end = 0
    lastGenesName = ""
    geneName = ""
    regionsIndex = 0
    sequencesIndex = 0
    hasAssociationCount = 0
    hasOneAssociationCount = 0
    [sequencesChrom, sequencesMiddle, sequencesStart, sequencesEnd] = getSequenceInfoSpecific(sequencesInfo, sequencesIndex)
    sequencesForGeneIndexes = []
    while regionsIndex < len(regionsInfo):
        # Find the sequences peaks/sequences associated with each gene/region
	if regionsIndex > lastGenesIndex:
		# Get the information for the new gene/region
        	geneElements = regionsInfo[regionsIndex].split("\t")
		geneName = str(regionsIndex)
		if nameCol >= 0:
			# The gene/region has a name in the file
			geneName = geneElements[nameCol].strip()
		if geneName != lastGenesName:
			# Change the starts and end if at a new gene/region
			if lastGenesName != "":
				# Write the information from the last gene/region to the file
				if len(sequencesForGeneIndexes) > 0:
					# There is at least 1 sequence difference near the gene/region
					hasAssociationCount = hasAssociationCount + 1
					if len(sequencesForGeneIndexes) == 1:
						# There is exactly 1 sequence difference near the gene/region
						hasOneAssociationCount = hasOneAssociationCount + 1
						[sequencesChromPlus, sequencesMiddlePlus, sequencesStartPlus, sequencesEndPlus] = getSequenceInfoSpecific(sequencesInfo, sequencesForGeneIndexes[0])
						singleFile.write(sequencesChromPlus + "\t" + str(sequencesStartPlus) + "\t" + str(sequencesEndPlus) + "\n")
				writeGenesequencessToFileUCSC(outputFile, lastGenesName, chrom, startList[0], end, sequencesForGeneIndexes)
			start = int(geneElements[startCol].strip())
			startList = []
			startList.append(start)
			end = int(geneElements[endCol].strip())
			if len(sequencesForGeneIndexes) > 0:
				# Go back to the 1st sequences/sequence for the previous gene/region
				sequencesIndex = sequencesForGeneIndexes[0]
				[sequencesChrom, sequencesMiddle, sequencesStart, sequencesEnd] = getSequenceInfoSpecific(sequencesInfo, sequencesIndex)
    				sequencesForGeneIndexes = []
		else:
			start = int(geneElements[startCol].strip())
			startList.append(start)
			end = max(end, int(geneElements[endCol].strip()))
		chrom = geneElements[chromCol].strip()
		lastGenesIndex = regionsIndex
		lastGenesName = geneName
	allsequencessUsed = False
	while sequencesChrom < chrom:
		# Iterate through sequences sites/sequences until a site on the correct chromosome has been found
		sequencesIndex = sequencesIndex + 1
		if sequencesIndex >= len(sequencesInfo):
			# All sequencess/sequences have been used, so stop
			allsequencessUsed = True
			break
		[sequencesChrom, sequencesMiddle, sequencesStart, sequencesEnd] = getSequenceInfoSpecific(sequencesInfo, sequencesIndex)
	if allsequencessUsed == True:
		# No more sequencess/sequences remain, so write the current gene/region to the file
		regionsIndex = regionsIndex + 1
		continue			
	while (sequencesEnd < start) and (sequencesChrom == chrom):
		# Iterate through sequences sites/sequences until a site near the gene's TSS/region's start has been found
		sequencesIndex = sequencesIndex + 1
		if sequencesIndex >= len(sequencesInfo):
			# All sequencess/sequences have been used, so stop
			allsequencessUsed = True
			break
		[sequencesChrom, sequencesMiddle, sequencesStart, sequencesEnd] = getSequenceInfoSpecific(sequencesInfo, sequencesIndex)
	if allsequencessUsed == True:
		# No more sequencess/sequences remain, so write the current gene/region to the file
		regionsIndex = regionsIndex + 1
		continue	
	if sequencesChrom > chrom:
		# There are no more sequences hypersensitivity sites/sequences on the chromosome with the gene/region
		regionsIndex = regionsIndex + 1
		continue
	if sequencesStart > end:
		# There are no more sequences hypersensitivity sites/sequences near the gene's TSS/region's start
		regionsIndex = regionsIndex + 1
		continue
	if sequencesIndex not in sequencesForGeneIndexes:
		# The sequences hypersensitivity site/sequence has not been stored for the gene/region, so add it to the list
		sequencesForGeneIndexes.append(sequencesIndex)
	sequencesIndex = sequencesIndex + 1
	if sequencesIndex >= len(sequencesInfo):
		# All sequencess/sequences have been used, so stop
		regionsIndex = regionsIndex + 1
		continue
	[sequencesChrom, sequencesMiddle, sequencesStart, sequencesEnd] = getSequenceInfoSpecific(sequencesInfo, sequencesIndex)
    if len(sequencesForGeneIndexes) > 0:
	# There is at least 1 sequence difference near a sequences site and the gene
	hasAssociationCount = hasAssociationCount + 1
	if len(sequencesForGeneIndexes) == 1:
		# There is exactly 1 sequence difference near the gene/region
		hasOneAssociationCount = hasOneAssociationCount + 1
		[sequencesChromPlus, sequencesMiddlePlus, sequencesStartPlus, sequencesEndPlus] = getSequenceInfoSpecific(sequencesInfo, sequencesForGeneIndexes[0])
		singleFile.write(sequencesChromPlus + "\t" + str(sequencesStartPlus) + "\t" + str(sequencesEndPlus) + "\n")
    writeGenesequencessToFileUCSC(outputFile, lastGenesName, chrom, startList[0], end, sequencesForGeneIndexes)
    print hasAssociationCount
    print float(hasAssociationCount)/float(len(regionsInfo))
    print hasOneAssociationCount
    outputFile.close()
    singleFile.close()

if __name__=="__main__":
    import sys
    regionsFileName = sys.argv[1]
    sequencesFileName = sys.argv[2]
    outputFileName = sys.argv[3]
    nameCol = int(sys.argv[4]) # Use -1 if there is no name
    chromCol = int(sys.argv[5])
    startCol = int(sys.argv[6])
    endCol = int(sys.argv[7])
    singleFileName = sys.argv[8]
                        
    associateRegionsToSequencesUCSCSingle(regionsFileName, sequencesFileName, outputFileName, nameCol, chromCol, startCol, endCol, singleFileName)
