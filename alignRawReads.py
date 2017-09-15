def alignRawReads(extractedRawReadsListFileName, pathInput, pathGenome, pathOutput, assemblySuffix, outputFileName, multiMapVal):
	# Creates a script that aligns the raw reads to their appropriateGenome
	extractedRawReadsListFile = open(extractedRawReadsListFileName)
	outputFile = open(outputFileName, 'w+')
	for line in extractedRawReadsListFile:
		# Iterate through the raw reads files and make a script that will align them to their appropriate genome
		outputFile.write("bwa aln -R " + str(multiMapVal) + " -f ")
		lineElements = line.split(".")
		outputFile.write(pathOutput + lineElements[0] + "Mapped ")
		# ASSUMES THAT THE SPECIES IS HUMAN, CHIMP, OR MACAQUE
		# ASSUMES THAT THE ASSEMBLIES ARE hg19, panTro2, and rheMac2
		species = "Human"
		assembly = "hg19"
		if "Chimp" in lineElements[0]:
			# The species is Chimp
			species = "Chimp"
			assembly = "panTro2"
		elif "Macaque" in lineElements[0]:
			species = "Macaque"
			assembly = "rheMac2"
		outputFile.write(pathGenome + species + "Genome/" + assembly + assemblySuffix + " " + pathInput + line)
	extractedRawReadsListFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   extractedRawReadsListFileName = sys.argv[1] 
   pathInput = sys.argv[2]
   pathGenome = sys.argv[3]
   pathOutput = sys.argv[4]
   assemblySuffix = sys.argv[5]
   outputFileName = sys.argv[6]
   multiMapVal = int(sys.argv[7])
   alignRawReads(extractedRawReadsListFileName, pathInput, pathGenome, pathOutput, assemblySuffix, outputFileName, multiMapVal)
