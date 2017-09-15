def outputAllZeros(outputFileList):
	# Output a 0 entry in every file

	for outputFile in outputFileList:
		# Iterate through the output files and write a 0 to each
		outputFile.write("0\t")


def outputPWMFeaturesTFSpecific(FIMORegionsTFsFilt, FIMORegionsLikelihoodsFilt, FIMORegionsDistancesFilt, FIMOSequencesTFsFilt, FIMOSequencesLikelihoodsFilt, FIMOSequencesDistancesFilt, outputFileList, maxDist, TFList):
	# Output the PWM features for the current sequence difference to the outputFile
	# Output each feature TF-specifically
	# Each output file will have a matrix that is number of sequence differences by number of TFs
	# Each entry (i,j) of the matrix will be the feature for sequence difference i and TF j
	for i in range(len(TFList)):
		TF = TFList[i]
		if (TF not in FIMORegionsTFsFilt) and (TF not in FIMOSequencesTFsFilt):
			# The current TF is not in the region with or without the sequence difference, so all features are 0
			outputAllZeros(outputFileList)
			continue
		featureList = []
		for i in range(len(outputFileList)):
			# Initialize all features to be 0
			featureList.append(0)
		strongestRegionLikelihood = 0
		closestRegionDistance = maxDist
		strongestSequenceLikelihood = 0
		closestSequenceDistance = maxDist

		if TF in FIMORegionsTFsFilt:
			# The TF has a motif in the current region, so use its binding information to compute the features
			indices = [i for i, x in enumerate(FIMORegionsTFsFilt) if x == TF]
			for i in indices:
				# Iterate through TF motifs for the current TF
				regionLikelihood = FIMORegionsLikelihoodsFilt[i]
				if regionLikelihood > strongestRegionLikelihood:
					# A new motif with the strongest likelihood had been found
					strongestRegionLikelihood = regionLikelihood
				regionCenterDistance = FIMORegionsDistancesFilt[i]
				if regionCenterDistance < closestRegionDistance:
					# A new motif with the closest center to the center of the region has been found
					closestRegionDistance = regionCenterDistance
			if TF not in FIMOSequencesTFsFilt:
				# There is a TF whose motif is lost with the sequence difference
				featureList[0] = 1
				featureList[2] = 1

		if TF in FIMOSequencesTFsFilt:
			indices = [j for j, x in enumerate(FIMOSequencesTFsFilt) if x == TF]
			for j in indices:
				# Iterate through TF motifs for the current TF
				sequenceLikelihood = FIMOSequencesLikelihoodsFilt[j]
				if sequenceLikelihood > strongestSequenceLikelihood:
					# A new motif with the strongest likelihood had been found
					strongestSequenceLikelihood = sequenceLikelihood
				sequenceCenterDistance = FIMOSequencesDistancesFilt[j]
				if sequenceCenterDistance < closestSequenceDistance:
					# A new motif with the closest center to the center of the region has been found
					closestSequenceDistance = sequenceCenterDistance
			if TF not in FIMORegionsTFsFilt:
				# There is a TF whose motif is gained with the sequence difference
				featureList[0] = 1
				featureList[1] = 1

		featureList[3] = abs(strongestRegionLikelihood - strongestSequenceLikelihood)
		featureList[4] = strongestSequenceLikelihood - strongestRegionLikelihood
		featureList[5] = strongestRegionLikelihood - strongestSequenceLikelihood
		featureList[6] = abs(closestRegionDistance - closestSequenceDistance)
		# Larger feature if seq. diff. allows for closer motif
		featureList[7] = closestRegionDistance - closestSequenceDistance 
		featureList[8] = closestSequenceDistance - closestRegionDistance
		for i in range(len(outputFileList)):
			# Write all of the features to their outputFiles
			outputFileList[i].write(str(featureList[i]) + "\t")

	for outputFile in outputFileList:
		# Make a new line in each output file for the data from the next sequence difference
		outputFile.write("\n")


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


def makeTFList(TFListFileName):
	# Make a list of TFs from the TF file
	TFListFile = open(TFListFileName)
	TFList = []
	for line in TFListFile:
		# Iterate through the TFs and add each to the list
		TFList.append(string.upper(line.strip()))
	TFListFile.close()
	return TFList
	

def getPWMFeaturesTFSpecific(FIMORegionsFileName, FIMOSequencesFileName, sequenceDifferenceFileName, regionsToDifferencesFileName, TFListFileName, outputFileNamePrefix, outputUpFileNamePrefix, outputDownFileNamePrefix):
	# Get the following PWM-related features for each TF:
	# File 1: Is the TF's motif added/removed? (Binary)
	# File 2: |log-likelihood(TF's strongest motif) - log-likelihood(TF's strongest motif in other file)|
	# File 3: |(distance of TF's motif motif that is closest to ctr. from ctr.) - (distance of TF's motif that is closest to ctr. from ctr. in other file)| (Use 1/2 of reg. len. for dist. when no motif in 1 file)
	# outputUpFileName gets the same features with up direction (added, pos./neg., pos./neg.)
	# outputDownFileName gets the same features with down direction (removed, neg./pos., neg./pos.)
	# ASSUMES THAT NO 2 REGIONS OVERLAP
	# ASSUMES THAT THERE ARE NO SEQUENCE DIFFERENCES IN MULTIPLE REGIONS
	# ASSUMES THAT THE REGION FILE IS SORTED BY CHROM, START, END AND THAT THE REGIONS REFERRED TO ARE SORTED IN THE SAME WAY
	[FIMORegionsLocations, FIMORegionsTFs, FIMORegionsLikelihoods, FIMORegionsCenterDistances] = getRegionTFFIMOInfo(FIMORegionsFileName)
	[FIMOSequencesLocations, FIMOSequencesTFs, FIMOSequencesLikelihoods, FIMOSequencesCenterDistances] = getSequenceTFFIMOInfo(FIMOSequencesFileName)
	sequenceDifferenceFile = open(sequenceDifferenceFileName)
	sequenceDifferenceLines = sequenceDifferenceFile.readlines()
	sequenceDifferenceFile.close()
	regionsToDifferencesFile = open(regionsToDifferencesFileName)
	TFList = makeTFList(TFListFileName) #FINISH (maybe modify sequence for loop)
	outputFileList = []
	outputFileList.append(open(outputFileNamePrefix+"TFChanged", 'w+'))
	outputFileList.append(open(outputUpFileNamePrefix+"TFChanged", 'w+'))
	outputFileList.append(open(outputDownFileNamePrefix+"TFChanged", 'w+'))
	outputFileList.append(open(outputFileNamePrefix+"LikelihoodChanged", 'w+'))
	outputFileList.append(open(outputUpFileNamePrefix+"LikelihoodChanged", 'w+'))
	outputFileList.append(open(outputDownFileNamePrefix+"LikelihoodChanged", 'w+'))
	outputFileList.append(open(outputFileNamePrefix+"DistanceChanged", 'w+'))
	outputFileList.append(open(outputUpFileNamePrefix+"DistanceChanged", 'w+'))
	outputFileList.append(open(outputDownFileNamePrefix+"DistanceChanged", 'w+'))

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
			outputPWMFeaturesTFSpecific(FIMORegionsTFsFilt, FIMORegionsLikelihoodsFilt, FIMORegionsCenterDistancesFilt, FIMOSequencesTFsFilt, FIMOSequencesLikelihoodsFilt, FIMOSequencesCenterDistancesFilt, outputFileList, maxDist, TFList)

	regionsToDifferencesFile.close()
	for outputFile in outputFileList:
		# Close all of the output files
		outputFile.close()


if __name__=="__main__":
   import sys
   import string
   FIMORegionsFileName = sys.argv[1] # Name of file with FIMO information without sequence differences
   FIMOSequencesFileName = sys.argv[2] # Name of file with FIMO information with sequence differences
   sequenceDifferenceFileName = sys.argv[3]
   regionsToDifferencesFileName = sys.argv[4]
   TFListFileName = sys.argv[5]
   outputFileNamePrefix = sys.argv[6]
   outputUpFileNamePrefix = sys.argv[7]
   outputDownFileNamePrefix = sys.argv[8]

   print "Getting PWM features from " + FIMOSequencesFileName
   getPWMFeaturesTFSpecific(FIMORegionsFileName, FIMOSequencesFileName, sequenceDifferenceFileName, regionsToDifferencesFileName, TFListFileName, outputFileNamePrefix, outputUpFileNamePrefix, outputDownFileNamePrefix)
