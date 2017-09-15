def makeListCol(fileName, col):
	# Makes a list from the file, where column col of each line in the file is an element in the list
	# ASSUMES THAT EACH LINE IN THE FILE HAS EXACTLY 1 WORD/NUMBER/etc.
	listFile = open(fileName)
	listFromFile = []
	for line in listFile:
		# Iterate through the lines of the file and add each line to the list
		lineElements = line.split("\t")
		listFromFile.append(string.upper(lineElements[col].strip()))
	listFile.close()
	return listFromFile


def getDNaseInfo(currentLine):
	# Gets the DNase chromosome, start, end, and nearest gene from data in the current line
	currentLineElements = currentLine.split("\t")
	chrom = currentLineElements[0]
	start = int(currentLineElements[1])
	end = int(currentLineElements[2])
	geneName = string.upper(currentLineElements[6].strip())
	return [chrom, start, end, geneName]


def getFracDNaseNearDiffExpr (nearestGenesFileName, diffExprFileName, diffDNaseExprFileName):
	# Get the fraction of differential DNase sites that are near differentiall expressed genes
	# RECORDS AN ASSOCIATION IF AT LEAST 1 NEAR-BY GENE IS DIFFERENTIALLY EXPRESSED
	nearestGenesFile = open(nearestGenesFileName)
	diffExprList = makeListCol(diffExprFileName, 3)
	diffDNaseExprFile = open(diffDNaseExprFileName, 'w+')
	lastChrom = ""
	lastStart = -1
	lastEnd = -1
	currentLine = nearestGenesFile.readline()
	[chrom, start, end, geneName] = getDNaseInfo(currentLine)
	DNaseCount = 0
	recordedCount = 0

	while currentLine != "":
		# Iterate through the lines associating differential DNase to genes and record DNase for diff. expr. genes
		DNaseCount = DNaseCount + 1
		if geneName in diffExprList:
			# The DNase is associated ot a differentially expressed gene
			recordedCount = recordedCount + 1
			diffDNaseExprFile.write(chrom + "\t" + str(start) + "\t" + str(end) + "\n")
			lastChrom = chrom
			lastStart = start
			lastEnd = end
			while ((lastChrom == chrom) and (lastStart == start)) and (lastEnd == end):
				# Read lines until a new region has been reached
				currentLine = nearestGenesFile.readline()
				if currentLine == "":
					# At the end of the file, so stop
					break
				[chrom, start, end, geneName] = getDNaseInfo(currentLine)

		else:
			lastChrom = chrom
			lastStart = start
			lastEnd = end
			currentLine = nearestGenesFile.readline()
			if currentLine == "":
				# At the end of the file, so stop
				break
			[chrom, start, end, geneName] = getDNaseInfo(currentLine)
	nearestGenesFile.close()
	diffDNaseExprFile.close()
	print float(recordedCount)
	print float(recordedCount)/float(DNaseCount)


if __name__=="__main__":
   import sys
   import string
   nearestGenesFileName = sys.argv[1] # Name of file with each DNase site and the coordinates and name of the nearest gene
   diffExprFileName = sys.argv[2] # Name of file with differential DNase sites
   diffDNaseExprFileName = sys.argv[3] # Name of output file for diff. DNase sites near diff. expressed genes

   getFracDNaseNearDiffExpr (nearestGenesFileName, diffExprFileName, diffDNaseExprFileName)
