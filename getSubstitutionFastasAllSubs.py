def getRegionInfo(line):
	# Get the chromosome, start, and end from a line in the bed file
	lineElements = line.split("\t")
	chrom = lineElements[0]
	start = int(lineElements[1])
	end = int(lineElements[2].strip())
	return [chrom, start, end]

def getSubstitutionFastas(allSubstitutionsFileName, substitutionFileName, outputFileName):
	# Find the sequence difference that corresponds to each substitution using a file with all substitutions
	# ASSUMES THAT BOTH SUBSTITUTIONS FILES ARE SORTED BY CHROM, THEN START, THEN END
	# ASSUMES THAT ALL SUBSTITUTIONS ARE PART OF SUBSTITUTIONS IN THE COMPLETE SUBSTITUTION LIST
	allSubstitutionsFile = open(allSubstitutionsFileName)
	substitutionFile = open(substitutionFileName)
	currentSubLine = allSubstitutionsFile.readline()
	[currentSubChrom, currentSubStart, currentSubEnd] = getRegionInfo(currentSubLine)
	outputFile = open(outputFileName, 'w+')
	for line in substitutionFile:
		# For each substitution, find the corresponding line in the fasta file, and record the location and bases
		[chrom, start, end] = getRegionInfo(line)
		while chrom > currentSubChrom:
			# Go to the next substitution in the file of all substitutions until the correct chrom. is reached
			currentSubLine = allSubstitutionsFile.readline()
			[currentSubChrom, currentSubStart, currentSubEnd] = getRegionInfo(currentSubLine)
		while start > currentSubEnd:
			# Go to the next substitution in the file of all substitutions until the correct region is reached
			currentSubLine = allSubstitutionsFile.readline()
			[currentSubChrom, currentSubStart, currentSubEnd] = getRegionInfo(currentSubLine)
		if (chrom != currentSubChrom) or ((start < currentSubStart) or (end > currentSubEnd)):
			print "Problem!"
		subSeq = currentSubLine.split("\t")[3].strip()
		outputFile.write(chrom + "\t" + str(start) + "\t" + str(end) + "\t" + subSeq + "\n")
	allSubstitutionsFile.close()
	substitutionFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   allSubstitutionsFileName = sys.argv[1] 
   substitutionFileName = sys.argv[2]
   outputFileName = sys.argv[3]
   getSubstitutionFastas(allSubstitutionsFileName, substitutionFileName, outputFileName)
