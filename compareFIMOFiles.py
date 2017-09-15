def findBestScoreSeqDiff(first, lineList, lineUsed, TF, chrom, start, end, seqDiffChrom, seqDiffStart, seqDiffEnd, index, score):
	# Find the motif with the best score for a given TF, region, and sequence difference
	for j in range(first, len(lineList)):
		# Iterate through the remaining lines of the FIMO file and find those that have the same TF in the same region
		if lineUsed[j] == 1:
			# The line's information has already been recorded if appropriate, so continue
			continue
		if lineList[j][0] == "#":
			# The current line is a header, so do not include it
			# HEADERS ARE INCLUDED WHEN COUNTING LINES
			lineUsed[j] = 1
			continue
		lineElementsj = lineList[j].split("\t")
		if lineElementsj[0] != TF:
			# The line has information for a different TF, so continue
			continue
		locationInfoj = lineElementsj[1].split("_")
		if ((locationInfoj[1] != chrom) or ((int(locationInfoj[2]) != start) or (int(locationInfoj[3]) != end))) or ((locationInfoj[4] != seqDiffChrom) or ((int(locationInfoj[5]) != seqDiffStart) or (int(locationInfoj[6]) != seqDiffEnd))):
			# The line has information for a different region or sequence difference, so continue
			continue
		scorej = float(lineElementsj[5])
		if scorej > score:
			# The current TF-binding site has a greater score than the greatest so far, so replace the score with the current score
			score = scorej
			index = j
		lineUsed[j] = 1
	return [lineUsed, index, score]


def findBestScoreTwo(first, lineList, lineUsed, TF, chrom, start, end, index, score):
	# Find the motif with the best score for a given TF and region, allow regions that have been used to be used again (might be multiple sequence differences for a single region)
	for j in range(first, len(lineList)):
		# Iterate through the remaining lines of the FIMO file and find those that have the same TF in the same region
		if lineList[j][0] == "#":
			# The current line is a header, so do not include it
			# HEADERS ARE INCLUDED WHEN COUNTING LINES
			lineUsed[j] = 1
			continue
		lineElementsj = lineList[j].split("\t")
		if lineElementsj[0] != TF:
			# The line has information for a different TF, so continue
			continue
		locationInfoj = lineElementsj[1].split("_")
		if (locationInfoj[1] != chrom) or ((int(locationInfoj[2]) != start) or (int(locationInfoj[3]) != end)):
			# The line has information for a different region, so continue
			continue
		scorej = float(lineElementsj[5])
		if scorej > score:
			# The current TF-binding site has a greater score than the greatest so far, so replace the score with the current score
			score = scorej
			# The previously strongest motif for the TF is not the overall strongest, so record that it has been used
			lineUsed[index] = 1
			index = j
		else:
			# The current TF's motif is not the motif for the TF, so record that it has been used
			lineUsed[j] = 1
		# DO NOT RECORD THAT THE STRONGEST MOTIF FOR THE CURRENT TF HAS BEEN USED BECAUSE IT MIGHT NOT BE USED FOR EVERY SEQUENCE DIFFERENCE
	return [lineUsed, index, score]


def findBestScore(first, lineList, lineUsed, TF, chrom, start, end, index, score):
	# Find the motif with the best score for a given TF and region
	for j in range(first, len(lineList)):
		# Iterate through the remaining lines of the FIMO file and find those that have the same TF in the same region
		if lineUsed[j] == 1:
			# The line's information has already been recorded if appropriate, so continue
			continue
		if lineList[j][0] == "#":
			# The current line is a header, so do not include it
			# HEADERS ARE INCLUDED WHEN COUNTING LINES
			lineUsed[j] = 1
			continue
		lineElementsj = lineList[j].split("\t")
		if lineElementsj[0] != TF:
			# The line has information for a different TF, so continue
			continue
		locationInfoj = lineElementsj[1].split("_")
		if (locationInfoj[1] != chrom) or ((int(locationInfoj[2]) != start) or (int(locationInfoj[3]) != end)):
			# The line has information for a different region, so continue
			continue
		scorej = float(lineElementsj[5])
		if scorej > score:
			# The current TF-binding site has a greater score than the greatest so far, so replace the score with the current score
			score = scorej
			index = j
		lineUsed[j] = 1
	return [lineUsed, index, score]


def compareFIMOFiles(FIMOOneFileName, FIMOTwoFileName, outputFileName):
	# Create a file where each line is seq. chrom, start, end, seq. diff. chrom, start, end, TF, line with largest log-lik. in file 1, largest log-lik. in file 1, line with largest log-lik. in file 2, largest log-lik. in file 2, log-like. diff.
	# Use -1 when the TF is not present for the sequence in a file
	# ASSUMES THAT THE FIRST FILE HAS THE SEQUENCE DIFFERENCES
	FIMOOneFile = open(FIMOOneFileName)
	FIMOTwoFile = open(FIMOTwoFileName)
	outputFile = open(outputFileName, 'w+')
	FIMOOneFile.readline() # Remove the header
	FIMOOneLines = FIMOOneFile.readlines()
	FIMOOneLinesUsed = numpy.zeros(len(FIMOOneLines))
	FIMOOneFile.close()
	FIMOTwoFile.readline() # Remove the header
	FIMOTwoLines = FIMOTwoFile.readlines()
	FIMOTwoLinesUsed = numpy.zeros(len(FIMOTwoLines))
	FIMOTwoFile.close()

	for i in range(len(FIMOOneLines)):
		# Iterate through the lines of the first FIMO file and record the necessary information
		if FIMOOneLinesUsed[i] == 1:
			# The current line's information has already been recorded, so continue
			continue
		if FIMOOneLines[i][0] == "#":
			# The current line is a header, so do not include it
			# HEADERS ARE INCLUDED WHEN COUNTING LINES
			FIMOOneLinesUsed[i] = 1
			continue

		lineElements = FIMOOneLines[i].split("\t")
		TF = lineElements[0]
		locationInfo = lineElements[1].split("_")
		chrom = locationInfo[1]
		start = int(locationInfo[2])
		end = int(locationInfo[3])
		seqDiffChrom = locationInfo[4]
		seqDiffStart = int(locationInfo[5])
		seqDiffEnd = int(locationInfo[6])
		score = float(lineElements[5]) # Will hold the maximum score for the current TF
		index = i
		FIMOOneLinesUsed[i] = 1
		[FIMOOneLinesUsed, index, score] = findBestScoreSeqDiff(i+1, FIMOOneLines, FIMOOneLinesUsed, TF, chrom, start, end, seqDiffChrom, seqDiffStart, seqDiffEnd, index, score)

		scoreTwo = 0 # Initialize score for second FIMO file
		indexTwo = -1
		[FIMOTwoLinesUsed, indexTwo, scoreTwo] = findBestScoreTwo(0, FIMOTwoLines, FIMOTwoLinesUsed, TF, chrom, start, end, indexTwo, scoreTwo)

		scoreDiff = abs(score - scoreTwo)
		outputFile.write(chrom + "\t" + str(start) + "\t" + str(end) + "\t" + seqDiffChrom + "\t" + str(seqDiffStart) + "\t" + str(seqDiffEnd) + "\t")
		outputFile.write(TF + "\t" + str(index) + "\t" + str(score) + "\t" + str(indexTwo) + "\t" + str(scoreTwo) + "\t" + str(scoreDiff) + "\n")
	
	for i in range(len(FIMOTwoLines)):
		# Iterate through the lines of the second FIMO file and record the necessary information
		# PUT INFORMATION FOR ALL TFS INTO THE OUTPUT FILE BECAUSE SOME TFS WILL HAVE MOTIFS FOR SOME SEQUENCE DIFFERENCES BUT NOT OTHERS
		if FIMOTwoLinesUsed[i] == 1:
			# The current line's information has already been recorded, so continue
			continue
		if FIMOTwoLines[i][0] == "#":
			# The current line is a header, so do not include it
			# HEADERS ARE INCLUDED WHEN COUNTING LINES
			FIMOTwoLinesUsed[i] = 1
			continue

		lineElements = FIMOTwoLines[i].split("\t")
		TF = lineElements[0]
		locationInfo = lineElements[1].split("_")
		chrom = locationInfo[1]
		start = int(locationInfo[2])
		end = int(locationInfo[3])
		score = float(lineElements[5]) # Will hold the maximum score for the current TF
		index = i
		FIMOTwoLinesUsed[i] = 1
		[FIMOTwoLinesUsed, index, score] = findBestScore(i+1, FIMOTwoLines, FIMOTwoLinesUsed, TF, chrom, start, end, index, score)
		outputFile.write(chrom + "\t" + str(start) + "\t" + str(end) + "\t" + str(-1) + "\t" + str(-1) + "\t" + str(-1) + "\t" + TF + "\t" + str(-1) + "\t" + str(0) + "\t" + str(index) + "\t" + str(score) + "\t" + str(score) + "\n")
	outputFile.close()


if __name__=="__main__":
   import sys
   import numpy
   FIMOOneFileName = sys.argv[1] # Name of with sequence difference FIMO information
   FIMOTwoFileName = sys.argv[2]
   outputFileName = sys.argv[3]

   compareFIMOFiles(FIMOOneFileName, FIMOTwoFileName, outputFileName)
