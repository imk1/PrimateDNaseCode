def associateSeqDiffsToTFClusters(regionsToDifferencesFileName, regionsToClustersFileName, outputFileName):
	# Get the TF clusters for each sequence difference
	regionsToDifferencesFile = open(regionsToDifferencesFileName)
	regionsToClustersFile = open(regionsToClustersFileName)
	outputFile = open(outputFileName, 'w+')

	for line in regionsToDifferencesFile:
		# Iterate through regions and find the features for each of the corresponding sequence differences
		lineElements = line.split("\t")
		regionClusters = regionsToClustersFile.readline() # NEED TO READ THE CLUSTER FOR EVERY REGION
		if len(lineElements) < 5:
			# There are no sequence differences for the current region, so do not consider it
			continue
		for seqDiffIndexStr in lineElements[4:]:
			# Iterate through the sequence differences associated with the current region and record the TF clusters for the region
			outputFile.write(regionClusters)

	regionsToDifferencesFile.close()
	regionsToClustersFile.close()
	outputFile.close()


if __name__=="__main__":
	import sys
	regionsToDifferencesFileName = sys.argv[1]
	regionsToClustersFileName = sys.argv[2]
	outputFileName = sys.argv[3]
                        
	associateSeqDiffsToTFClusters(regionsToDifferencesFileName, regionsToClustersFileName, outputFileName)
