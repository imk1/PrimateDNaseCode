def getRegionsOfInterest(inputFileName, chromCol, startCol, endCol, cutoff, upStart, downStart, upEnd, downEnd, useStart, useEnd, outputFileName):
	# Gets the regions of interest based on an input file, cutoff, and desired regions
	# ASSUMES THAT NO REGION OF INTEREST COULD EXTEND PAST THE END OF A CHROMOSOME
	inputFile = open(inputFileName)
	outputFile = open(outputFileName, 'w+')
	for line in inputFile:
		# Iterate through regions and get the desired regions
		lineElements = line.split("\t")
		chrom = lineElements[chromCol]
		start = int(lineElements[startCol])
		end = int(lineElements[endCol])

		if (((upStart == True) and (upEnd == True)) or ((downStart == True) and (upEnd == True))) or (((downStart == True) and (downEnd == True)) or (((upStart == True) and (downEnd == True)) and (useStart == True))):
			# Need to get separate regions for each end of the region
			outputFile.write(chrom + "\t")
			if upStart == True:
				# Need to go upstream of the start of the region
				startCoord = start - cutoff
				if startCoord > 0:
					# Write the starting coordinate to the file
					outputFile.write(str(startCoord) + "\t")
				else:
					outputFile.write("1\t")
			else:
				outputFile.write(str(start) + "\t")
			if downStart == True:
				# Need to go downstream of the start of the region
				outputFile.write(str(start + cutoff) + "\n")
			else:
				outputFile.write(str(start) + "\n")
			outputFile.write(chrom + "\t")
			if upEnd == True:
				# Need to go upstream of the end of the region
				endCoord = end - cutoff
				if endCoord > 0:
					# Write the starting coordinate to the file
					outputFile.write(str(endCoord) + "\t")
				else:
					outputFile.write("1\t")
			else:
				outputFile.write(str(end) + "\t")
			if downEnd == True:
				# Need to go downstream of the end of the region
				outputFile.write(str(end + cutoff) + "\n")
			else:
				outputFile.write(str(end) + "\n")

		else:
			outputFile.write(chrom + "\t")
			if upStart == True:
				# Need to go upstream of the start of the region
				startCoord = start - cutoff
				if startCoord > 0:
					# Write the starting coordinate to the file
					outputFile.write(str(startCoord) + "\t")
				else:
					outputFile.write("1\t")
				if downStart == True:
					# Need to go downstream of the start of the region
					outputFile.write(str(start + cutoff) + "\n")
				elif downEnd == True:
					# Need to go downstream of the end of the region
					outputFile.write(str(end + cutoff) + "\n")
				elif useStart == True:
					# Region of interest ends with the start of the region from the input file
					outputFile.write(str(start) + "\n")
				else:
					# Region of interest ends with the end of the region from the input file
					outputFile.write(str(end) + "\n")
			elif downStart == True:
				# Region of interest goes from the start of the region to in the input file to a cutoff
				outputFile.write(str(start) + "\t" + str(start + cutoff) + "\n")
			elif upEnd == True:
				# Need to go upstream of the start of the region
				endCoord = end - cutoff
				if endCoord > 0:
					# Write the starting coordinate to the file
					outputFile.write(str(endCoord) + "\t")
				else:
					outputFile.write("1\t")
				if downEnd == True:
					# Need to go downstream of the end of the region
					outputFile.write(str(end + cutoff) + "\n")
				else:
					# Region of interest ends with the end of the region from the input file
					outputFile.write(str(end) + "\n")
			else:
				# Region of interest goes from the end of the region in the input file to a cutoff
				outputFile.write(str(end) + "\t" + str(end + cutoff) + "\n")

	inputFile.close()
	outputFile.close()


if __name__=="__main__":
   import sys
   inputFileName = sys.argv[1] 
   chromCol = int(sys.argv[2])
   startCol = int(sys.argv[3])
   endCol = int(sys.argv[4])
   cutoff = int(sys.argv[5])
   upStartInt = int(sys.argv[6])
   downStartInt = int(sys.argv[7])
   upEndInt = int(sys.argv[8])
   downEndInt = int(sys.argv[9])
   useStartInt = int(sys.argv[10])
   useEndInt = int(sys.argv[11])
   outputFileName = sys.argv[12]

   upStart = bool(upStartInt)
   downStart = bool(downStartInt)
   upEnd = bool(upEndInt)
   downEnd = bool(downEndInt)
   useStart = bool(useStartInt)
   useEnd = bool(useEndInt)

   getRegionsOfInterest(inputFileName, chromCol, startCol, endCol, cutoff, upStart, downStart, upEnd, downEnd, useStart, useEnd, outputFileName)
