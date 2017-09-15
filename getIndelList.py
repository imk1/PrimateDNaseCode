def getIndelList(inputFileName, speciesName, outputInsertionFileName, outputDeletionFileName, speciesTwoName, outputDeletionTwoFileName):
	# Gets the list of INDELs for a species from a 3-way alignment INDEL file
	inputFile = open(inputFileName)
	inputFile.readline()
	outputInsertionFile = open(outputInsertionFileName, 'w+')
	outputDeletionFile = open(outputDeletionFileName, 'w+')
	outputDeletionTwoFile = open(outputDeletionTwoFileName, 'w+')
	for line in inputFile:
		# Iterate through the lines of the input file and find the coordinates of INDELs for species speciesName
		lineElements = line.split("\t")
		speciesElements = lineElements[1].split(".")
		if speciesElements[0] == speciesName:
			# The INDEL is from the species of interest, so record its location
			chromElements = speciesElements[1].split("_")
			chrom = chromElements[0]
			inOrDel = chromElements[1]
			start = 0
			end = 0
			if lineElements[3] == speciesName + "." + chrom:
				# The first entry is for species speciesName
				start = int(lineElements[4])
				end = int(lineElements[5])
			elif lineElements[8] == speciesName + "." + chrom:
				# The second entry is for species speciesName
				start = int(lineElements[9])
				end = int(lineElements[10])
			else:
				# The third entry is for species speciesName
				start = int(lineElements[14])
				end = int(lineElements[15])
			if inOrDel == "insert":
				# The entry is an insertion, so record it in the insertion file
				outputInsertionFile.write(chrom + "\t" + str(start) + "\t" + str(end + 1) + "\n")
			elif inOrDel == "delete":
				# The entry is an deletion, so record it in the deletion file
				outputDeletionFile.write(chrom + "\t" + str(start) + "\t" + str(end) + "\n")
				if lineElements[3].split(".")[0] == speciesTwoName:
					# The first entry is for species speciesTwoName
					# Write regions for species 2 to its file (note that chromosomes might be different)
					outputDeletionTwoFile.write(lineElements[3].split(".")[1] + "\t" + lineElements[4] + "\t" + str(int(lineElements[5]) + 1) + "\n")
				elif lineElements[8].split(".")[0] == speciesTwoName:
					# The second entry is for species speciesTwoName
					# Write regions for species 2 to its file (note that chromosomes might be different)
					outputDeletionTwoFile.write(lineElements[8].split(".")[1] + "\t" + lineElements[9] + "\t" + str(int(lineElements[10]) + 1) + "\n")
				else:
					# The second entry is for species speciesTwoName
					# Write regions for species 2 to its file (note that chromosomes might be different)
					outputDeletionTwoFile.write(lineElements[13].split(".")[1] + "\t" + lineElements[14] + "\t" + str(int(lineElements[15]) + 1) + "\n")
	inputFile.close()
	outputInsertionFile.close()
	outputDeletionFile.close()
	outputDeletionTwoFile.close()

if __name__=="__main__":
   import sys
   inputFileName = sys.argv[1] 
   speciesName = sys.argv[2]
   outputInsertionFileName = sys.argv[3]
   outputDeletionFileName = sys.argv[4]
   speciesTwoName = sys.argv[5]
   outputDeletionTwoFileName = sys.argv[6]

   getIndelList(inputFileName, speciesName, outputInsertionFileName, outputDeletionFileName, speciesTwoName, outputDeletionTwoFileName)
