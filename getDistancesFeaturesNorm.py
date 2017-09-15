def outputDistanceFeatures(DNaseLocation, seqDiffLocation, regionDistance, windowDistance, outputFile):
	# Outputs the distance features to the file
	DNaseCenter = math.floor((.5 * float(DNaseLocation[2] - DNaseLocation[1])) + float(DNaseLocation[1]))
	seqDiffCenter = math.floor((.5 * float(seqDiffLocation[2] - seqDiffLocation[1])) + float(seqDiffLocation[1]))
	featureOne = 0
	featureTwo = 0
	if (seqDiffCenter >= DNaseLocation[1]) and (seqDiffCenter <= DNaseLocation[2]):
		# The center of the sequence differences is in the DNase site
		featureOne = 1
		featureTwo = regionDistance
	elif seqDiffCenter < DNaseLocation[1]:
		# The center of the sequence difference is upstream of the DNase site
		featureTwo = regionDistance - (DNaseLocation[1] - seqDiffCenter)
	else:
		featureTwo = regionDistance - (seqDiffCenter - DNaseLocation[2])
	featureThree = (regionDistance + math.floor((.5 * float(windowDistance)))) - abs(DNaseCenter - seqDiffCenter)
	featureOneNorm = float(featureOne)/float(windowDistance)
	featureTwoNorm = float(featureTwo)/float(windowDistance)
	featureThreeNorm = float(featureThree)/float(windowDistance)
	outputFile.write(str(featureOneNorm) + "\t" + str(featureTwoNorm) + "\t" + str(featureThreeNorm) + "\n")

def getDistancesFeatures(sequenceDifferenceFileName, regionsToDifferencesFileName, regionDistance, outputFileName):
	# Get the following distance-related features that are normalized by the region length:
	# Column 1: (Is the center of the sequence difference in the DNase hypersensitivity site?)/(window dist.) (Binary)
	# Column 2: (regionDistance - (How far is the center of the sequence difference from the closest edge of DNase hypersensitivity site?))/(window dist.) [regionDistance if in the site]
	# Column 3: ((regionDistance + .5windowDistance) - (How far is the center of the sequence difference from the center of the DNase hypersensitivity site?)) / (window dist.)
	# ASSUMES THAT NO 2 REGIONS OVERLAP
	# ASSUMES THAT THERE ARE NO SEQUENCE DIFFERENCES IN MULTIPLE REGIONS
	# ASSUMES THAT THE REGION FILE IS SORTED BY CHROM, START, END AND THAT THE SEQUENCE DIFFERENCES REFERRED TO ARE SORTED IN THE SAME WAY
	sequenceDifferenceFile = open(sequenceDifferenceFileName)
	sequenceDifferenceLines = sequenceDifferenceFile.readlines()
	sequenceDifferenceFile.close()
	regionsToDifferencesFile = open(regionsToDifferencesFileName)
	outputFile = open(outputFileName, 'w+')

	for line in regionsToDifferencesFile:
		# Iterate through regions and find the features for each of the corresponding sequence differences
		lineElements = line.split("\t")
		if len(lineElements) < 5:
			# There are no sequence differences for the current region, so do not consider it
			continue
		regionLocation = (lineElements[1], int(lineElements[2]), int(lineElements[3]))
		DNaseLocation = (regionLocation[0], regionLocation[1] + regionDistance, regionLocation[2] - regionDistance)
		windowDistance = DNaseLocation[2] - DNaseLocation[1]

		for seqDiffIndexStr in lineElements[4:]:
			# Iterate through the sequence differences associated with the current region and get the PWM features for each
			seqDiffIndex = int(seqDiffIndexStr.strip())
			seqDiffInfo = sequenceDifferenceLines[seqDiffIndex].split("\t")
			seqDiffLocation = (seqDiffInfo[0], int(seqDiffInfo[1]), int(seqDiffInfo[2]))
			outputDistanceFeatures(DNaseLocation, seqDiffLocation, regionDistance, windowDistance, outputFile)

	regionsToDifferencesFile.close()
	outputFile.close()


if __name__=="__main__":
   import sys
   import math
   sequenceDifferenceFileName = sys.argv[1] # Name of file with the sequence differences
   regionsToDifferencesFileName = sys.argv[2] # Name of file with the regions mapped to their corresponding sequence differences sequence differences
   regionDistance = int(sys.argv[3])
   outputFileName = sys.argv[4]

   getDistancesFeatures(sequenceDifferenceFileName, regionsToDifferencesFileName, regionDistance, outputFileName)
