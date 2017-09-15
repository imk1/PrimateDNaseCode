def extractRawReads(rawReadsListFileName, path, outputFileName):
	# Creates a script that extracts the raw reads to files with meaningful names
	rawReadsListFile = open(rawReadsListFileName)
	outputFile = open(outputFileName, 'w+')
	count = 0
	for line in rawReadsListFile:
		# Iterate through the raw reads files and make a script that will extract them and then re-name the file in a meaningful way
		outputFile.write("unzip " + path + line)
		species = "Human"
		if line[0] == "C":
			# The data is from chimp
			species = "Chimp"
		elif line[0] == "Q":
			# The data is from macaque
			species = "Macaque"
		cellType = "Fibroblast"
		if line[1] == "L":
			# The data is from LCLs
			cellType = "LCL"
		rep = "Rep1"
		if line[4] == "2":
			# The data is from the second sample
			rep = "Rep2"
		elif line[4] == "3":
			# The data is from the third sample
			rep = "Rep3"
		unzippedFileName = line[-21:-5]
		renamedFileName = path+species+cellType+rep+"Sequence"+str(count)+".txt"
		outputFile.write("mv " + unzippedFileName + " " + renamedFileName + "\n")
		count = count + 1
	rawReadsListFile.close()
	outputFile.close()

if __name__=="__main__":
   import sys
   rawReadsListFileName = sys.argv[1] 
   path = sys.argv[2]
   outputFileName = sys.argv[3]
   extractRawReads(rawReadsListFileName, path, outputFileName)
