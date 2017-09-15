def outputFeatures(likelihoodRegionList, likelihoodSeqDiffList, outputFile):
	# Output the features to the output file
	if len(likelihoodRegionList) == 0:
		# There are no motifs with and without the sequence difference
		outputFile.write("0\t0\t0\t0\n")
		return
	if (0 in likelihoodRegionList) or (0 in likelihoodSeqDiffList):
		# There is a TF whose motif is added or removed
		outputFile.write("1\t")
	else:
		outputFile.write("0\t")

	maxTuple = (max(likelihoodRegionList), max(likelihoodSeqDiffList))
	likelihoodDiffGen = abs(maxTuple[0] - maxTuple[1])
	maxMotifScore = max(maxTuple)
	maxMotifTupleIndex = maxTuple.index(maxMotifScore)
	oneWritten = False

	if maxMotifTupleIndex == 0:
		# The motif with the highest score is from the region without the sequence difference (or there is a tie)
		maxMotifIndex = likelihoodRegionList.index(maxMotifScore)
		currentIndex = maxMotifIndex + 1
		likelihoodDiffSpecific = abs(maxTuple[0] - likelihoodSeqDiffList[maxMotifIndex])
		if likelihoodSeqDiffList[maxMotifIndex] == 0:
			# A TF with the maximum motif score has no motif in the file with the sequence difference
			outputFile.write("1\t")
			oneWritten = True
		if maxMotifScore in likelihoodRegionList[maxMotifIndex + 1:]:
			# There is a tie for the motif with the maximum score
			for motifScore in likelihoodRegionList[maxMotifIndex + 1:]:
				# Iterate through the other TFs determine whether their motifs have the same score
				if motifScore == maxMotifScore:
					# The tied motif has been found
					if (likelihoodSeqDiffList[currentIndex] == 0) and (oneWritten == False):
						# A TF with the maximum motif score has no motif in the file with the sequence difference
						outputFile.write("1\t")
						oneWritten = True
					if abs(motifScore - likelihoodSeqDiffList[currentIndex]) > likelihoodDiffSpecific:
						# A larger strongest motif difference has been found, so replace the current strongest motif difference
						likelihoodDiffSpecific = abs(motifScore - likelihoodSeqDiffList[currentIndex])
				currentIndex = currentIndex + 1
		if maxMotifScore in likelihoodSeqDiffList:
			# There is a tie for the motif with the maximum likelihood score, where the tie occurs in the region with the sequence difference
			currentIndex = 0
			for motifScore in likelihoodSeqDiffList:
				# Iterate through the TFs with motifs in the region with the sequence difference and determine whether their motifs have the same score
				if motifScore == maxMotifScore:
					# The tied motif has been found
					if (likelihoodRegionList[currentIndex] == 0) and (oneWritten == False):
						# A TF with the maximum motif score has no motif in the file with the sequence difference
						outputFile.write("1\t")
						oneWritten = True
					if abs(motifScore - likelihoodRegionList[currentIndex]) > likelihoodDiffSpecific:
						# A larger strongest motif difference has been found, so replace the current strongest motif difference
						likelihoodDiffSpecific = abs(motifScore - likelihoodRegionList[currentIndex])
				currentIndex = currentIndex + 1
		if oneWritten == False:
			# The motif with the largest score is present without the sequence difference
			outputFile.write("0\t")
		outputFile.write(str(likelihoodDiffGen) + "\t" + str(likelihoodDiffSpecific) + "\n")

	else:
		# The motif with the highest score is from the region with the sequence difference
		maxMotifIndex = likelihoodSeqDiffList.index(maxMotifScore)
		likelihoodDiffSpecific = abs(maxTuple[1] - likelihoodRegionList[maxMotifIndex])
		if likelihoodRegionList[maxMotifIndex] == 0:
			# A TF with the maximum motif score has no motif in the file with the sequence difference
			outputFile.write("1\t")
			oneWritten = True
		if maxMotifScore in likelihoodSeqDiffList[maxMotifIndex + 1:]:
			# There is a tie for the motif with the maximum score
			currentIndex = maxMotifIndex + 1
			for motifScore in likelihoodSeqDiffList[maxMotifIndex + 1:]:
				# Iterate through the other TFs determine whether their motifs have the same score
				if motifScore == maxMotifScore:
					# The tied motif has been found
					if (likelihoodRegionList[currentIndex] == 0) and (oneWritten == False):
						# A TF with the maximum motif score has no motif in the file with the sequence difference
						outputFile.write("1\t")
						oneWritten = True
					if abs(motifScore - likelihoodRegionList[currentIndex]) > likelihoodDiffSpecific:
						# A larger strongest motif difference has been found, so replace the current strongest motif difference
						likelihoodDiffSpecific = abs(motifScore - likelihoodRegionList[currentIndex])
		if oneWritten == False:
			# The motif with the largest score is present without the sequence difference
			outputFile.write("0\t")
		outputFile.write(str(likelihoodDiffGen) + "\t" + str(likelihoodDiffSpecific) + "\n")
	

def getPWMFeatures(FIMOComparisonFileName, sequenceDifferenceFileName, outputFileName):
	# Get the following PWM-related features:
	# Column 1: Is there a TF whose motif that is added/removed? (Binary)
	# Column 2: Is the TF with the overall strongest motif's motif added/removed? (Binary) [If there is a tie for the overall strongest motif, choose 1 if any of the strongest motifs are added/removed]
	# Column 3: |log-likelihood(strongest motif without sequence difference) - log-likelihood(strongest motif with sequence difference)|
	# Column 4: |log-likelihood(overall strongest motif) - log-likelihood(overall strongest motif in other file)| [If there is a tie for the overall strongest motif, choose the largest difference]
	# ASSUMES THAT NO 2 REGIONS OVERLAP
	# ASSUMES THAT THE FIMO COMPARISON FILE IS SORTED BY REGION CHROM, REGION START, REGION END, SEQUENCE DIFFERENCE CHROM, SEQUENCE DIFFERENCE START, SEQUENCE DIFFERENCE END
	# ASSUMES THAT THE SEQUENCE DIFFERENCE FILE IS SORTED BY CHROM, START, END
	# ASSUMES THAT REGIONS IN THE FIMO COMPARISON FILE WITH MOTIFS THAT ARE NOT IN THE SEQUENCE DIFFERENCE REGIONS ARE LISTED FIRST
	FIMOComparisonFile = open(FIMOComparisonFileName)
	sequenceDifferenceFile = open(sequenceDifferenceFileName)
	outputFile = open(outputFileName, 'w+')

	sequenceDifferenceLine = sequenceDifferenceFile.readline()
	sequenceDifferenceLineElements = sequenceDifferenceLine.split("\t")
	sequenceDifferenceLocation = (sequenceDifferenceLineElements[0], int(sequenceDifferenceLineElements[1]), int(sequenceDifferenceLineElements[2]))
	
	likelihoodRegionList = []
	likelihoodSeqDiffList = []
	lastRegionLocation = ("", -1, -1)
	lastSequenceDifferenceLocation = ("-1", -1, -1)
	lastTFRegionIndex = 0
	TFList = []
	
	allDifferencesSeen = False
	for line in FIMOComparisonFile:
		# Iterate through the lines of the FIMO comparison file and use them to compute the PWM features
		lineElements = line.split("\t")
		regionLocation = (lineElements[0], int(lineElements[1]), int(lineElements[2]))
		currentSequenceDifferenceLocation = (lineElements[3], int(lineElements[4]), int(lineElements[5]))
		if currentSequenceDifferenceLocation != lastSequenceDifferenceLocation:
			# In a new sequence difference, so re-initialize if this is not the first sequence difference
			if lastSequenceDifferenceLocation != ("-1", -1, -1):
				# The previous sequence difference was not empty, so output the appropriate information
				outputFeatures(likelihoodRegionList, likelihoodSeqDiffList, outputFile)
				sequenceDifferenceLine = sequenceDifferenceFile.readline()
				if sequenceDifferenceLine == "":
					# All sequence differences have been seen, so stop
					allDifferencesSeen = True
					break
				sequenceDifferenceLineElements = sequenceDifferenceLine.split("\t")
				sequenceDifferenceLocation = (sequenceDifferenceLineElements[0], int(sequenceDifferenceLineElements[1]), int(sequenceDifferenceLineElements[2]))
				likelihoodRegionList = likelihoodRegionList[0:lastTFRegionIndex]
				likelihoodSeqDiffList = []
				for i in range(len(likelihoodRegionList)):
					# Initialize the log-likelihoods for the sequence differences to be zeros
					likelihoodSeqDiffList.append(0)
			if (lastRegionLocation != ("", -1, -1)) and (currentSequenceDifferenceLocation != ("-1", -1, -1)):
				# Not at beginning, so need to check that no sequence differences are being excluded
				while currentSequenceDifferenceLocation != sequenceDifferenceLocation:
					# A sequence difference region has no motifs
					outputFeatures(likelihoodRegionList, likelihoodSeqDiffList, outputFile)
					likelihoodSeqDiffList = []
					for i in range(len(likelihoodRegionList)):
						# Initialize the log-likelihoods for the sequence differences to be zeros
						likelihoodSeqDiffList.append(0)
					sequenceDifferenceLine = sequenceDifferenceFile.readline()
					if sequenceDifferenceLine == "":
						# All sequence differences have been seen, so stop
						allDifferencesSeen = True
						break
					sequenceDifferenceLineElements = sequenceDifferenceLine.split("\t")
					sequenceDifferenceLocation = (sequenceDifferenceLineElements[0], int(sequenceDifferenceLineElements[1]), int(sequenceDifferenceLineElements[2]))
			if allDifferencesSeen == True:
				# All sequence differences have been seen, so stop
				break
			lastSequenceDifferenceLocation = currentSequenceDifferenceLocation

		if regionLocation != lastRegionLocation:
			# The region has changed, so re-initialize everything
			likelihoodRegionList = []
			likelihoodSeqDiffList = []
			TFList = []
			lastRegionLocation = regionLocation
		if currentSequenceDifferenceLocation == ("-1", -1, -1):
			# Initializing current region
			TFList.append(lineElements[6])
			likelihoodRegionList.append(float(lineElements[10]))
			likelihoodSeqDiffList.append(float(0))
			lastTFRegionIndex = lastTFRegionIndex + 1
		elif lineElements[6] not in TFList:
			# The current sequence difference allows for a TF motif that was not previously present
			TFList.append(lineElements[6])
			likelihoodRegionList.append(float(0))
			likelihoodSeqDiffList.append(float(lineElements[8]))
		else:
			TFIndex = TFList.index(lineElements[6])
			likelihoodSeqDiffList[TFIndex] = float(lineElements[8])

	if allDifferencesSeen == False:
		# Some sequence differences still have not been seen
		outputFeatures(likelihoodRegionList, likelihoodSeqDiffList, outputFile)
		likelihoodRegionList = []
		likelihoodSeqDiffList = []
		TFList = []
		sequenceDifferenceLine = sequenceDifferenceFile.readline()
		while sequenceDifferenceLine != "":
			# Record sequence difference features to the output file for the remaining sequence differences
			sequenceDifferenceLineElements = sequenceDifferenceLine.split("\t")
			sequenceDifferenceLocation = (sequenceDifferenceLineElements[0], int(sequenceDifferenceLineElements[1]), int(sequenceDifferenceLineElements[2]))
			outputFeatures(likelihoodRegionList, likelihoodSeqDiffList, outputFile)
			sequenceDifferenceLine = sequenceDifferenceFile.readline()

	FIMOComparisonFile.close()	
	sequenceDifferenceFile.close()
	outputFile.close()


if __name__=="__main__":
   import sys
   FIMOComparisonFileName = sys.argv[1] # Name of with sequence difference FIMO information
   sequenceDifferenceFileName = sys.argv[2]
   outputFileName = sys.argv[3]

   getPWMFeatures(FIMOComparisonFileName, sequenceDifferenceFileName, outputFileName)
