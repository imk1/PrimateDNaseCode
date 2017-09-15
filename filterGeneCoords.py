def makeGeneList(geneFileName):
	# Make a list of genes in which all of the letters are capitalized
	geneFile = open(geneFileName)
	geneList = []
	for line in geneFile:
		# Iterate through gene file and make a list of all of the genes in upper case
		# ASSUMES THAT THE GENE NAME IS THE FIRST ELEMENT IN THE LINE
		lineElements = line.split("\t")
		geneCap = string.upper(lineElements[0].strip())
		geneList.append(geneCap)
	geneFile.close()
	return geneList


def makeGeneDict(geneNamesFileName):
	# Make a gene name dictionary
	geneNamesFile = open(geneNamesFileName)
	geneDict = {}
	for line in geneNamesFile:
		# Add each gene to the dictionary
		lineElements = line.split("\t")
		geneDict[lineElements[0]] = lineElements[1].strip()
	geneNamesFile.close()
	return geneDict


def filterGeneCoords(coordsFileName, geneNamesFileName, coordsOutputFileName, geneNamesCol, geneNamesIsDict):
	# Filter gene coordinates to remove genes whose names are not in the list and genes with unknown locations
	coordsFile = open(coordsFileName)
	geneList = makeGeneList(geneNamesFileName)
	coordsOutputFile = open(coordsOutputFileName, 'w+')
	coordsFile.readline() # Remove the header
	includedGeneList = []
	geneDict = {}
	if geneNamesIsDict == True:
		# Make a gene name dictionary to be used for generating names later
		geneDict = makeGeneDict(geneNamesFileName)

	for line in coordsFile:
		# Iterate through the lines with the gene coordinates and write those that are included after filtering
		lineElements = line.split("\t")
		chromElements = lineElements[1].split("_")
		if len(chromElements) > 1:
			# The location is not known, so do not include these coordinates
			continue
		if string.upper(lineElements[geneNamesCol].strip()) not in geneList:
			# The location is for a gene that is not in the list, so do not include it
			continue
		includedGeneList.append(string.upper(lineElements[geneNamesCol].strip()))
		coordsOutputFile.write(lineElements[1] + "\t" + lineElements[3] + "\t" + lineElements[4] + "\t")
		if geneNamesIsDict == True:
			# Use the gene dictionary to get the gene name
			coordsOutputFile.write(geneDict[lineElements[geneNamesCol]] + "\n")
		else:
			coordsOutputFile.write(lineElements[geneNamesCol].strip() + "\n")
	coordsFile.close()
	coordsOutputFile.close()
	return [geneList, includedGeneList]


def makeMissingList(geneList, includedGeneList, missingOutputFileName):
	# Make a list of genes from the list with that are not included in the other input file
	missingOutputFile = open(missingOutputFileName, 'w+')
	for geneName in geneList:
		# Iterate through genes and record each that was not included in the other input file
		if geneName not in includedGeneList:
			# The gene was not included, so record the name of the gene
			missingOutputFile.write(geneName + "\n")
	missingOutputFile.close()


if __name__=="__main__":
    import sys
    import string
    coordsFileName = sys.argv[1]
    geneNamesFileName = sys.argv[2]
    coordsOutputFileName = sys.argv[3]
    missingOutputFileName = sys.argv[4]
    geneNamesCol = int(sys.argv[5])
    geneNamesIsDictInt = int(sys.argv[6])
    geneNamesIsDict = bool(geneNamesIsDictInt)

                        
    [geneList, includedGeneList] = filterGeneCoords(coordsFileName, geneNamesFileName, coordsOutputFileName, geneNamesCol, geneNamesIsDict)
    makeMissingList(geneList, includedGeneList, missingOutputFileName)
