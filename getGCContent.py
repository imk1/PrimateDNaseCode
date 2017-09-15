def getGContent(inputFileName, outputFileName, lineByLine):
	# Gets the GC-content of a FASTA file
	numAs = 0
	numCs = 0
	numGs = 0
	numTs = 0
	inputFile = open(inputFileName)
	lineCount = 0
	for line in inputFile:
		# Iterate through the lines of the FASTA file and count the numbers of As, Cs, Gs, and Ts
		if lineCount % 1000000 == 0:
			print lineCount
		if line[0] == ">":
			# The line is a header, so skip it
			if (lineByLine == True) and (lineCount > 0):
				# Write the fractions from the previous line to the file
				totalBases = numAs + numCs + numGs + numTs
				fracAs = float(numAs)/float(totalBases)
				fracCs = float(numCs)/float(totalBases)
				fracGs = float(numGs)/float(totalBases)
				fracTs = float(numTs)/float(totalBases)
				fracAT = fracAs + fracTs
				fracGC = fracCs + fracGs
				outputFile = open(outputFileName+str(lineCount), 'w+')
				outputFile.write("# tuple" + "\t" + "frequency" + "\n")
				outputFile.write("a" + "\t" + str(fracAT/float(2)) + "\n")
				outputFile.write("c" + "\t" + str(fracGC/float(2)) + "\n")
				outputFile.write("g" + "\t" + str(fracGC/float(2)) + "\n")
				outputFile.write("t" + "\t" + str(fracAT/float(2)) + "\n")
				outputFile.close()
				numAs = 0
				numCs = 0
				numGs = 0
				numTs = 0
			lineCount = lineCount + 1
			continue
		for base in line:
			# Itereate through the bases and add the appropriate numbers to the counts
			if base.upper() == "A":
				# Add a count to the As
				numAs = numAs + 1
			elif base.upper() == "C":
				# Add a count to the Cs
				numCs = numCs + 1
			elif base.upper() == "G":
				# Add a count to the Gs
				numGs = numGs + 1
			elif base.upper() == "T":
				# Add a count to the Ts
				numTs = numTs + 1
	totalBases = numAs + numCs + numGs + numTs
	fracAs = float(numAs)/float(totalBases)
	fracCs = float(numCs)/float(totalBases)
	fracGs = float(numGs)/float(totalBases)
	fracTs = float(numTs)/float(totalBases)
	fracAT = fracAs + fracTs
	fracGC = fracCs + fracGs
	outputFile = open(outputFileName+str(lineCount), 'w+')
	outputFile.write("# tuple" + "\t" + "frequency" + "\n")
	outputFile.write("a" + "\t" + str(fracAT/float(2)) + "\n")
	outputFile.write("c" + "\t" + str(fracGC/float(2)) + "\n")
	outputFile.write("g" + "\t" + str(fracGC/float(2)) + "\n")
	outputFile.write("t" + "\t" + str(fracAT/float(2)) + "\n")
	outputFile.close()

if __name__=="__main__":
   import sys
   inputFileName = sys.argv[1] 
   outputFileName = sys.argv[2]
   lineByLineInt = int(sys.argv[3])
   lineByLine = bool(lineByLineInt)
   getGContent(inputFileName, outputFileName, lineByLine)
