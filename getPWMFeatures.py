def outputPWMFeatures(FIMORegionsTFsFilt, FIMORegionsLikelihoodsFilt, FIMORegionsDistancesFilt, FIMOSequencesTFsFilt, FIMOSequencesLikelihoodsFilt, FIMOSequencesDistancesFilt, outputFile, outputUpFile, outputDownFile, maxDist):
	# Output the PWM features for the current sequence difference to the outputFile
	# FOR FEATURE 6, USE THE SAME INDEXES THAT ARE USED FOR FEATURE 8 (likelihoods might not be optimal if tie)
	# FEATURES 5, 6, AND 8 TAKE MAXIMAL VALUE
	# FEATURE 7 TAKES THE MINIMAL VALUE
	strongestRegionIndexes = []
	strongestRegionLikelihood = 0
	closestRegionIndexes = []
	closestRegionDistance = maxDist
	strongestSequenceIndexes = []
	strongestSequenceLikelihood = 0
	closestSequenceIndexes = []
	closestSequenceDistance = maxDist

	featureOne = 0
	featureTwo = 0
	featureThree = 0
	featureFour = 0
	featureFive = 0
	featureSix = 0
	featureSeven = 0
	featureEight = 0
	featureOneUp = 0
	featureTwoUp = 0
	featureThreeUp = 0
	featureFourUp = 0
	featureFiveUp = 0
	featureSixUp = 0
	featureSevenUp = 0
	featureEightUp = 0
	featureOneDown = 0
	featureTwoDown = 0
	featureThreeDown = 0
	featureFourDown = 0
	featureFiveDown = 0
	featureSixDown = 0
	featureSevenDown = 0
	featureEightDown = 0

	for i in range(len(FIMORegionsTFsFilt)):
		# Iterate through the information for the region file to start computing features
		regionTF = FIMORegionsTFsFilt[i]
		if regionTF not in FIMOSequencesTFsFilt:
			# There is a TF whose motif is lost with the sequence difference
			featureOne = 1
			featureOneDown = 1
		regionLikelihood = FIMORegionsLikelihoodsFilt[i]
		if regionLikelihood > strongestRegionLikelihood:
			# A new motif with the strongest likelihood had been found
			strongestRegionLikelihood = regionLikelihood
			strongestRegionIndexes = []
			strongestRegionIndexes.append(i)
		elif regionLikelihood == strongestRegionLikelihood:
			# A new motif has been found whose likelihood is tied with the strongest likelihood
			strongestRegionIndexes.append(i)
		regionCenterDistance = FIMORegionsDistancesFilt[i]
		if regionCenterDistance < closestRegionDistance:
			# A new motif with the closest center to the center of the region has been found
			closestRegionDistance = regionCenterDistance
			closestRegionIndexes = []
			closestRegionIndexes.append(i)
		elif regionCenterDistance == closestRegionDistance:
			# A new motif has been found whose distance from the region center is tied with the closest motif
			closestRegionIndexes.append(i)
	for i in range(len(FIMOSequencesTFsFilt)):
		# Iterate through the information for the region file to start computing features
		sequenceTF = FIMOSequencesTFsFilt[i]
		if sequenceTF not in FIMORegionsTFsFilt:
			# There is a TF whose motif is gained with the sequence difference
			featureOne = 1
			featureOneUp = 1
		sequenceLikelihood = FIMOSequencesLikelihoodsFilt[i]
		if sequenceLikelihood > strongestSequenceLikelihood:
			# A new motif with the strongest likelihood had been found
			strongestSequenceLikelihood = sequenceLikelihood
			strongestSequenceIndexes = []
			strongestSequenceIndexes.append(i)
		elif sequenceLikelihood == strongestSequenceLikelihood:
			# A new motif has been found whose likelihood is tied with the strongest likelihood
			strongestSequenceIndexes.append(i)
		sequenceCenterDistance = FIMOSequencesDistancesFilt[i]
		if sequenceCenterDistance < closestSequenceDistance:
			# A new motif with the closest center to the center of the region has been found
			closestSequenceDistance = sequenceCenterDistance
			closestSequenceIndexes = []
			closestSequenceIndexes.append(i)
		elif sequenceCenterDistance == closestSequenceDistance:
			# A new motif has been found whose distance from the region center is tied with the closest motif
			closestSequenceIndexes.append(i)

	if strongestRegionLikelihood >= strongestSequenceLikelihood:
		# The strongest motif is in the region without the sequence difference
		for ri in strongestRegionIndexes:
			# Iterate through the TFs with the strongest motifs
			currentDiff = strongestRegionLikelihood
			if FIMORegionsTFsFilt[ri] not in FIMOSequencesTFsFilt:
				# The strongest motif's TF has no motif with the sequence difference
				featureTwo = 1
				featureTwoDown = 1
			else:
				seqIndex = FIMOSequencesTFsFilt.index(FIMORegionsTFsFilt[ri])
				currentMax = FIMOSequencesLikelihoodsFilt[seqIndex]
				for i in range(seqIndex + 1, len(FIMOSequencesTFsFilt)):
					# Find other occurrences of the same TF
					if FIMOSequencesTFsFilt[i] == FIMORegionsTFsFilt[ri]:
						# Another motif for the same TF has been found
						if FIMOSequencesLikelihoodsFilt[i] > currentMax:
							# The other motif is stronger
							currentMax = FIMOSequencesLikelihoodsFilt[i]
				currentDiff = abs(strongestRegionLikelihood - currentMax)
			if currentDiff > featureFour:
				# A new largest difference for the strongest motif has been found
				featureFour = currentDiff
				featureFourUp = -currentDiff
				featureFourDown = currentDiff
	if strongestSequenceLikelihood >= strongestRegionLikelihood:
		# The strongest motif is in the region with the sequence difference
		for si in strongestSequenceIndexes:
			# Iterate through the TFs with the strongest motifs
			currentDiff = strongestSequenceLikelihood
			if FIMOSequencesTFsFilt[si] not in FIMORegionsTFsFilt:
				# The strongest motif's TF has no motif without the sequence difference
				featureTwo = 1
				featureTwoUp = 1
			else:
				regIndex = FIMORegionsTFsFilt.index(FIMOSequencesTFsFilt[si])
				currentMax = FIMORegionsLikelihoodsFilt[regIndex]
				for i in range(regIndex + 1, len(FIMORegionsTFsFilt)):
					# Find other occurrences of the same TF
					if FIMORegionsTFsFilt[i] == FIMOSequencesTFsFilt[si]:
						# Another motif for the same TF has been found
						if FIMORegionsLikelihoodsFilt[i] > currentMax:
							# The other motif is stronger
							currentMax = FIMORegionsLikelihoodsFilt[i]
				currentDiff = abs(strongestSequenceLikelihood - currentMax)
			if currentDiff > featureFour:
				# A new largest difference for the strongest motif has been found
				featureFour = currentDiff
				featureFourUp = currentDiff
				featureFourDown = -currentDiff
	featureThree = abs(strongestRegionLikelihood - strongestSequenceLikelihood)
	featureThreeUp = strongestSequenceLikelihood - strongestRegionLikelihood
	featureThreeDown = strongestRegionLikelihood - strongestSequenceLikelihood

	if closestRegionDistance <= closestSequenceDistance:
		# The closest motif to the center is in the region without the sequence difference
		for ri in closestRegionIndexes:
			# Iterate through the TFs whose motifs are closest to the center
			currentDiff = abs(closestRegionDistance - maxDist)
			lasti = -1
			if FIMORegionsTFsFilt[ri] not in FIMOSequencesTFsFilt:
				# The closest motif to the center's TF has no motif with the sequence difference
				featureFive = 1
				featureFiveDown = 1
			else:
				seqIndex = FIMOSequencesTFsFilt.index(FIMORegionsTFsFilt[ri])
				lasti = seqIndex
				currentMin = FIMOSequencesDistancesFilt[seqIndex]
				for i in range(seqIndex + 1, len(FIMOSequencesTFsFilt)):
					# Find other occurrences of the same TF
					if FIMOSequencesTFsFilt[i] == FIMORegionsTFsFilt[ri]:
						# Another motif for the same TF has been found
						if FIMOSequencesDistancesFilt[i] < currentMin:
							# The other motif is closer to the center
							lasti = i
							currentMin = FIMOSequencesDistancesFilt[i]
				currentDiff = abs(closestRegionDistance - currentMin)
			if currentDiff > featureEight:
				# A new largest difference for the motif closest to the center has been found
				featureEight = currentDiff
				featureEightUp = -currentDiff
				featureEightDown = currentDiff
				if lasti == -1:
					# The TF closest to the center has no motif with the sequence difference
					featureSix = FIMORegionsLikelihoodsFilt[ri]
					featureSixUp = -FIMORegionsLikelihoodsFilt[ri]
					featureSixDown = FIMORegionsLikelihoodsFilt[ri]
				else:
					featureSix = abs(FIMORegionsLikelihoodsFilt[ri] - FIMOSequencesLikelihoodsFilt[lasti])
					featureSixUp = FIMOSequencesLikelihoodsFilt[lasti] - FIMORegionsLikelihoodsFilt[ri]
					featureSixDown = FIMORegionsLikelihoodsFilt[ri] - FIMOSequencesLikelihoodsFilt[lasti]
	if closestSequenceDistance <= closestRegionDistance:
		# The closest motif to the center is in the region with the sequence difference
		for si in closestSequenceIndexes:
			# Iterate through the TFs whose motifs are closest to the center
			currentDiff = abs(closestSequenceDistance - maxDist)
			lasti = -1
			if FIMOSequencesTFsFilt[si] not in FIMORegionsTFsFilt:
				# The strongest motif's TF has no motif without the sequence difference
				featureFive = 1
				featureFiveUp = 1
			else:
				regIndex = FIMORegionsTFsFilt.index(FIMOSequencesTFsFilt[si])
				lasti = regIndex
				currentMin = FIMORegionsDistancesFilt[regIndex]
				for i in range(regIndex + 1, len(FIMORegionsTFsFilt)):
					# Find other occurrences of the same TF
					if FIMORegionsTFsFilt[i] == FIMOSequencesTFsFilt[si]:
						# Another motif for the same TF has been found
						if FIMORegionsDistancesFilt[i] < currentMin:
							# The other motif is closer to the center
							lasti = i
							currentMin = FIMORegionsDistancesFilt[i]
				currentDiff = abs(closestSequenceDistance - currentMin)
			if currentDiff > featureEight:
				# A new largest distance for the motif closest to the center has been found
				featureEight = currentDiff
				featureEightUp = currentDiff
				featureEightDown = -currentDiff
				if lasti == -1:
					# The TF closest to the center has no motif without the sequence difference
					featureSix = FIMOSequencesLikelihoodsFilt[si]
					featureSixUp = FIMOSequencesLikelihoodsFilt[si]
					featureSixDown = -FIMOSequencesLikelihoodsFilt[si]
				else:
					featureSix = abs(FIMORegionsLikelihoodsFilt[lasti] - FIMOSequencesLikelihoodsFilt[si])
					featureSixUp = FIMOSequencesLikelihoodsFilt[si] - FIMORegionsLikelihoodsFilt[lasti]
					featureSixDown = FIMORegionsLikelihoodsFilt[lasti] - FIMOSequencesLikelihoodsFilt[si]
	featureSeven = abs(closestRegionDistance - closestSequenceDistance)
	# Larger feature if seq. diff. allows for closer motif
	featureSevenUp = closestRegionDistance - closestSequenceDistance
	featureSevenDown = closestSequenceDistance - closestRegionDistance

	outputFile.write(str(featureOne) + "\t" + str(featureTwo) + "\t" + str(featureThree) + "\t" + str(featureFour) + "\t" + str(featureFive) + "\t" + str(featureSix) + "\t" + str(featureSeven) + "\t" + str(featureEight) + "\n")
	outputUpFile.write(str(featureOneUp) + "\t" + str(featureTwoUp) + "\t" + str(featureThreeUp) + "\t" + str(featureFourUp) + "\t" + str(featureFiveUp) + "\t" + str(featureSixUp) + "\t" + str(featureSevenUp) + "\t" + str(featureEightUp) + "\n")
	outputDownFile.write(str(featureOneDown) + "\t" + str(featureTwoDown) + "\t" + str(featureThreeDown) + "\t" + str(featureFourDown) + "\t" + str(featureFiveDown) + "\t" + str(featureSixDown) + "\t" + str(featureSevenDown) + "\t" + str(featureEightDown) + "\n")


def getRegionTFFIMOInfo(FIMORegionsFileName):
	FIMORegionsFile = open(FIMORegionsFileName)
	FIMORegionsLocations = []
	FIMORegionsTFs = []
	FIMORegionsLikelihoods = []
	FIMORegionsCenterDistances = []
	for line in FIMORegionsFile:
		# Iterate through the FIMO information for the regions and extract the region locations, TFs, and likelihoods
		if line[0] == "#":
			# The current line is a header, so skip it
			continue
		lineElements = line.split("\t")
		motifStartNum = int(lineElements[2])
		motifEndNum = int(lineElements[3])
		motifCtrNum = float(motifStartNum + motifEndNum)/float(2)
		locationElements = lineElements[1].split("_")
		locationCtr = float(int(locationElements[3]) + int(locationElements[2]))/float(2)
		motifCtrLoc = int(locationElements[2]) + motifCtrNum
		FIMORegionsLocations.append((locationElements[1], int(locationElements[2]), int(locationElements[3])))
		FIMORegionsTFs.append(lineElements[0])
		FIMORegionsLikelihoods.append(float(lineElements[5]))
		FIMORegionsCenterDistances.append(abs(locationCtr - motifCtrLoc))
	FIMORegionsFile.close()
	return [FIMORegionsLocations, FIMORegionsTFs, FIMORegionsLikelihoods, FIMORegionsCenterDistances]


def getSequenceTFFIMOInfo(FIMOSequencesFileName):
	FIMOSequencesFile = open(FIMOSequencesFileName)
	FIMOSequencesLocations = []
	FIMOSequencesTFs = []
	FIMOSequencesLikelihoods = []
	FIMOSequencesCenterDistances = []
	for line in FIMOSequencesFile:
		# Iterate through the FIMO information for the sequences and extract the sequence locations, TFs, and likelihoods
		if line[0] == "#":
			# The current line is a header, so skip it
			continue
		lineElements = line.split("\t")
		motifStartNum = int(lineElements[2])
		motifEndNum = int(lineElements[3])
		motifCtrNum = float(motifStartNum + motifEndNum)/float(2)
		locationElements = lineElements[1].split("_")
		locationCtr = float(int(locationElements[3]) + int(locationElements[2]))/float(2)
		motifCtrLoc = int(locationElements[2]) + motifCtrNum
		FIMOSequencesLocations.append((locationElements[4], int(locationElements[5]), int(locationElements[6])))
		FIMOSequencesTFs.append(lineElements[0])
		FIMOSequencesLikelihoods.append(float(lineElements[5]))
		FIMOSequencesCenterDistances.append(abs(locationCtr - motifCtrLoc))
	FIMOSequencesFile.close()
	return [FIMOSequencesLocations, FIMOSequencesTFs, FIMOSequencesLikelihoods, FIMOSequencesCenterDistances]
	

def getPWMFeatures(FIMORegionsFileName, FIMOSequencesFileName, sequenceDifferenceFileName, regionsToDifferencesFileName, outputFileName, outputUpFileName, outputDownFileName):
	# Get the following PWM-related features:
	# Column 1: Is there a TF whose motif that is added/removed? (Binary)
	# Column 2: Is the TF with the overall strongest motif's motif added/removed? (Binary) [If there is a tie for the overall strongest motif, choose 1 if any of the strongest motifs are added/removed]
	# Column 3: |log-likelihood(strongest motif without sequence difference) - log-likelihood(strongest motif with sequence difference)|
	# Column 4: |log-likelihood(overall strongest motif) - log-likelihood(overall strongest motif in other file)| [If there is a tie for the overall strongest motif, choose the largest difference]
	# Column 5: Is the TF whose motif is closest to the center of the region added/removed?
	# Column 6: |log-likelihood(motif overall closest to ctr.) - log-likelihood(motif in other file in location that is closest to the ctr.)|
	# Column 7: |(distance of motif overall closest to ctr. from ctr. without sequence difference) - (distance of motif overall closest to ctr. from ctr. with sequence difference)| (Use 1/2 of reg. len. for dist. when no motif in 1 file)
	# Column 8: |(distance of motif overall closest to ctr. from ctr.) - (distance of motif overall closest to ctr. from ctr. in other file)| (Use 1/2 of reg. len. for dist. when no motif in 1 file)
	# outputUpFileName gets the same features with up direction (added, added, neg., neg./pos., added, neg., neg./pos.)
	# outputDownFileName gets the same features with down direction (removed, removed, pos., neg./pos., removed, neg., neg./pos.)
	# ASSUMES THAT NO 2 REGIONS OVERLAP
	# ASSUMES THAT THERE ARE NO SEQUENCE DIFFERENCES IN MULTIPLE REGIONS
	# ASSUMES THAT THE REGION FILE IS SORTED BY CHROM, START, END AND THAT THE REGIONS REFERRED TO ARE SORTED IN THE SAME WAY
	[FIMORegionsLocations, FIMORegionsTFs, FIMORegionsLikelihoods, FIMORegionsCenterDistances] = getRegionTFFIMOInfo(FIMORegionsFileName)
	[FIMOSequencesLocations, FIMOSequencesTFs, FIMOSequencesLikelihoods, FIMOSequencesCenterDistances] = getSequenceTFFIMOInfo(FIMOSequencesFileName)
	sequenceDifferenceFile = open(sequenceDifferenceFileName)
	sequenceDifferenceLines = sequenceDifferenceFile.readlines()
	sequenceDifferenceFile.close()
	regionsToDifferencesFile = open(regionsToDifferencesFileName)
	outputFile = open(outputFileName, 'w+')
	outputUpFile = open(outputUpFileName, 'w+')
	outputDownFile = open(outputDownFileName, 'w+')

	for line in regionsToDifferencesFile:
		# Iterate through regions and find the features for each of the corresponding sequence differences
		lineElements = line.split("\t")
		if len(lineElements) < 5:
			# There are no sequence differences for the current region, so do not consider it
			continue
		regionLocation = (lineElements[1], int(lineElements[2]), int(lineElements[3]))
		maxDist = int(lineElements[3]) - int(lineElements[2])
		FIMORegionsTFsFilt = []
		FIMORegionsLikelihoodsFilt = []
		FIMORegionsCenterDistancesFilt = []
		for i in range(len(FIMORegionsLocations)):
			# Iterate through region locations with FIMO information and find those that are for the current region
			if FIMORegionsLocations[i] == regionLocation:
				# FIMO information for the current region has been found
				FIMORegionsTFsFilt.append(FIMORegionsTFs[i])
				FIMORegionsLikelihoodsFilt.append(FIMORegionsLikelihoods[i])
				FIMORegionsCenterDistancesFilt.append(FIMORegionsCenterDistances[i])

		for seqDiffIndexStr in lineElements[4:]:
			# Iterate through the sequence differences associated with the current region and get the PWM features for each
			seqDiffIndex = int(seqDiffIndexStr.strip())
			seqDiffInfo = sequenceDifferenceLines[seqDiffIndex].split("\t")
			seqDiffLocation = (seqDiffInfo[0], int(seqDiffInfo[1]), int(seqDiffInfo[2]))
			FIMOSequencesTFsFilt = []
			FIMOSequencesLikelihoodsFilt = []
			FIMOSequencesCenterDistancesFilt = []
			for i in range(len(FIMOSequencesLocations)):
				# Iterate through the sequence difference locations with FIMO information and find those that are for the current region
				if FIMOSequencesLocations[i] == seqDiffLocation:
					# FIMO information for the current sequence difference has been found
					FIMOSequencesTFsFilt.append(FIMOSequencesTFs[i])
					FIMOSequencesLikelihoodsFilt.append(FIMOSequencesLikelihoods[i])
					FIMOSequencesCenterDistancesFilt.append(FIMOSequencesCenterDistances[i])
			outputPWMFeatures(FIMORegionsTFsFilt, FIMORegionsLikelihoodsFilt, FIMORegionsCenterDistancesFilt, FIMOSequencesTFsFilt, FIMOSequencesLikelihoodsFilt, FIMOSequencesCenterDistancesFilt, outputFile, outputUpFile, outputDownFile, maxDist)

	regionsToDifferencesFile.close()
	outputFile.close()
	outputUpFile.close()
	outputDownFile.close()


if __name__=="__main__":
   import sys
   FIMORegionsFileName = sys.argv[1] # Name of file with FIMO information without sequence differences
   FIMOSequencesFileName = sys.argv[2] # Name of file with FIMO information with sequence differences
   sequenceDifferenceFileName = sys.argv[3]
   regionsToDifferencesFileName = sys.argv[4]
   outputFileName = sys.argv[5]
   outputUpFileName = sys.argv[6]
   outputDownFileName = sys.argv[7]

   print "Getting PWM features from " + FIMOSequencesFileName
   getPWMFeatures(FIMORegionsFileName, FIMOSequencesFileName, sequenceDifferenceFileName, regionsToDifferencesFileName, outputFileName, outputUpFileName, outputDownFileName)
