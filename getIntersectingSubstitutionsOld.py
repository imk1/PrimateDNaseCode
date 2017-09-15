def makeSubstitutionList (substitutionFileName):
	# Make a list of all of the substitutions in the file, where each element is a (chromosome, location) tuple
	# Also make a list of the coordinates corresponding to the substitution in the other species
	substitutionFile = open(substitutionFileName)
	substitutionListCurrentSpecies = []
	substitutionListOtherSpecies = []
	substitutionFile.readline()
	currentLine = substitutionFile.readline()
	while currentLine != "":
		# Iterate through the lines of the substitution file and put them in the appropriate lists
		otherSpeciesLine = substitutionFile.readline()
		currentLineElements = currentLine.split("\t")
		otherSpeciesLineElements = otherSpeciesLine.split("\t")
		substitutionListCurrentSpecies.append((currentLineElements[0], int(currentLineElements[1]), int(currentLineElements[1]) + 1))
		substitutionListOtherSpecies.append((otherSpeciesLineElements[0], int(otherSpeciesLineElements[1]), int(otherSpeciesLineElements[1]) + 1))
		currentLine = substitutionFile.readline()
	substitutionFile.close()
	return [substitutionListCurrentSpecies, substitutionListOtherSpecies]

	
def getIntersectingSubstitutions (substitutionFileOneName, substitutionFileTwoName, outputFileCurrentName, outputFileOneName, outputFileTwoName):
	# Get the substitutions that occur in the alignments with both other species
	# ASSUMES THAT SUBSTITUTIONS ARE ONLY 1 BASE LONG
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
		currentLineTuple = (currentLineElements[0], int(currentLineElements[1]), int(currentLineElements[1]) + 1)
		if currentLineTuple in substitutionListCurrentSpecies:
			# The substitution has occurred for both species, so record it
			currentChromElements = currentLineTuple[0].split(".")
			outputFileCurrent.write(currentChromElements[1] + "\t" + str(currentLineTuple[1]) + "\t" + str(currentLineTuple[2]) + "\n")
			otherSpeciesOneIndex = substitutionListCurrentSpecies.index(currentLineTuple)
			otherSpeciesOneTuple = substitutionListOtherSpeciesOne[otherSpeciesOneIndex]
			otherSpeciesOneChromElements = otherSpeciesOneTuple[0].split(".")
			outputFileOne.write(otherSpeciesOneChromElements[1] + "\t" + str(otherSpeciesOneTuple[1]) + "\t" + str(otherSpeciesOneTuple[2]) + "\n")
			otherSpeciesTwoLineElements = otherSpeciesTwoLine.split("\t")
			otherSpeciesTwoChromElements = otherSpeciesTwoLineElements[0].split(".")
			outputFileTwo.write(otherSpeciesTwoChromElements[1] + "\t" + otherSpeciesTwoLineElements[1] + "\t" + str(int(otherSpeciesTwoLineElements[1]) + 1) + "\n")
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
