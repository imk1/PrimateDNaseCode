def makeSubstitutionList (substitutionFileName):
	# Make a list of all of the substitutions in the file, where each element is a (chromosome, location) tuple
	# Also make a list of the coordinates corresponding to the substitution in the other species
	# ASSUMES THAT SUBSTITUTIONS >=100 BASES ARE MISTAKES
	substitutionFile = open(substitutionFileName)
	substitutionListCurrentSpecies = []
	substitutionListOtherSpecies = []
	substitutionFile.readline()
	currentLine = substitutionFile.readline()
	while currentLine != "":
		# Iterate through the lines of the substitution file and put them in the appropriate lists
		otherSpeciesLine = substitutionFile.readline()
		currentLineElements = currentLine.split("\t")
		if int(currentLineElements[2]) - int(currentLineElements[1]) >= 100:
			# Substitution is too large, so exclude it
			currentLine = substitutionFile.readline()
			continue
		otherSpeciesLineElements = otherSpeciesLine.split("\t")
		if int(currentLineElements[2]) - int(currentLineElements[1]) != int(otherSpeciesLineElements[2]) - int(otherSpeciesLineElements[1]):
			# The substitution is a different length in the different species, so exclude it
			currentLine = substitutionFile.readline()
			continue
		substitutionListCurrentSpecies.append((currentLineElements[0], int(currentLineElements[1]), int(currentLineElements[2])))
		substitutionListOtherSpecies.append((otherSpeciesLineElements[0], int(otherSpeciesLineElements[1]), int(otherSpeciesLineElements[2])))
		currentLine = substitutionFile.readline()
	substitutionFile.close()
	return [substitutionListCurrentSpecies, substitutionListOtherSpecies]

	
def getIntersectingSubstitutions (substitutionFileOneName, substitutionFileTwoName, outputFileCurrentName, outputFileOneName, outputFileTwoName):
	# Get the substitutions that occur in the alignments with both other species
	# ASSUMES THAT SUBSTITUTIONS >=100 BASES ARE MISTAKES
	[substitutionListCurrentSpecies, substitutionListOtherSpeciesOne] = makeSubstitutionList (substitutionFileOneName)
	substitutionFileTwo = open(substitutionFileTwoName)
	outputFileCurrent = open(outputFileCurrentName, 'w+')
	outputFileOne = open(outputFileOneName, 'w+')
	outputFileTwo = open(outputFileTwoName, 'w+')
	substitutionFileTwo.readline()
	currentLineIndex = 0
	currentLine = substitutionFileTwo.readline()

	while currentLine != "":
		# Iterate through the lines of the substitution file and find those that are in the other substitution file
		currentLineIndex = currentLineIndex + 1
		otherSpeciesTwoLine = substitutionFileTwo.readline()
		currentLineElements = currentLine.split("\t")
		if int(currentLineElements[2]) - int(currentLineElements[1]) >= 100:
			# Substitution is too large, so exclude it
			currentLine = substitutionFileTwo.readline()
			continue
		currentLineTuple = (currentLineElements[0], int(currentLineElements[1]), int(currentLineElements[2]))
		otherSpeciesOneIndex = -1
		for i in range(len(substitutionListCurrentSpecies)):
			# Iterate through locations to determine if the substitution has occurred in both species
			locationTuple = substitutionListCurrentSpecies[i]
			if currentLineTuple[0] != locationTuple[0]:
				# The chromosome is different, so continue
				continue
			if (currentLineTuple[1] in range(locationTuple[1], locationTuple[2] + 1)) or (currentLineTuple[2] in range(locationTuple[1], locationTuple[2] + 1)):
				# There is overlap between the current substitution and one in the other species
				otherSpeciesOneIndex = i
				break

		if otherSpeciesOneIndex >= 0:
			# The substitution has occurred for both species, so record it
			otherSpeciesTwoLineElements = otherSpeciesTwoLine.split("\t")
			if currentLineTuple[2] - currentLineTuple[1] != int(otherSpeciesTwoLineElements[2]) - int(otherSpeciesTwoLineElements[1]):
				# The substitution is a different length in the different species, so exclude it
				currentLine = substitutionFileTwo.readline()
				continue

			currentChromElements = currentLineTuple[0].split(".")
			currentLineTuplePlus = substitutionListCurrentSpecies[otherSpeciesOneIndex]
			currentStart = max(currentLineTuple[1], currentLineTuplePlus[1]) # Finding intersection start
			currentEnd = min(currentLineTuple[2], currentLineTuplePlus[2]) # Finding intersection end
			outputFileCurrent.write(currentChromElements[1] + "\t" + str(currentStart) + "\t" + str(currentEnd + 1) + "\n") # Adding 1 to end so that final base is included when getting fasta

			otherSpeciesOneTuple = substitutionListOtherSpeciesOne[otherSpeciesOneIndex]
			otherSpeciesOneChromElements = otherSpeciesOneTuple[0].split(".")
			otherStartOne = otherSpeciesOneTuple[1] + (currentStart - currentLineTuplePlus[1])
			otherEndOne = otherSpeciesOneTuple[2] - (currentLineTuplePlus[2] - currentEnd)
			outputFileOne.write(otherSpeciesOneChromElements[1] + "\t" + str(otherStartOne) + "\t" + str(otherEndOne + 1) + "\n") # Adding 1 to end so that final base is included when getting fasta

			otherSpeciesTwoChromElements = otherSpeciesTwoLineElements[0].split(".")
			otherStartTwo = int(otherSpeciesTwoLineElements[1]) + (currentStart - currentLineTuple[1])
			otherEndTwo = int(otherSpeciesTwoLineElements[2]) - (currentLineTuple[2] - currentEnd)
			outputFileTwo.write(otherSpeciesTwoChromElements[1] + "\t" + str(otherStartTwo) + "\t" + str(otherEndTwo + 1) + "\n") # Adding 1 to end so that final base is included when getting fasta
		currentLine = substitutionFileTwo.readline()

	substitutionFileTwo.close()
	outputFileCurrent.close()
	outputFileOne.close()
	outputFileTwo.close()


if __name__=="__main__":
   import sys
   substitutionFileOneName = sys.argv[1] 
   substitutionFileTwoName = sys.argv[2]
   outputFileCurrentName = sys.argv[3]
   outputFileOneName = sys.argv[4]
   outputFileTwoName = sys.argv[5]

   getIntersectingSubstitutions (substitutionFileOneName, substitutionFileTwoName, outputFileCurrentName, outputFileOneName, outputFileTwoName)
