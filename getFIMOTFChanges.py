def getFIMODict(FIMOFileName):
	# Get a dictionary for a FIMO file
	FIMOFile = open(FIMOFileName)
	FIMOFile.readline() # Remove the header
	FIMODict = {}

	for line in FIMOFile:
		# Iterate through the lines of the first FIMO file and add their information to the first FIMO dictionary
		lineElements = line.split()
		region = lineElements[1]
		if region not in FIMODict:
			# The region is not yet in the first FIMO dictionary, so create an entry for it
			FIMODict[region] = {}
		TF = lineElements[0]
		likelihood = float(lineElements[5])
		if TF not in FIMODict[region]:
			# The TF is not yet in the first FIMO dictionary entry for the region, so create an entry for it
			FIMODict[region][TF] = likelihood
		elif likelihood > FIMODict[region][TF]:
			# The current likelihood for the TF is larger than the previous likelihoods, so replace the entry
			FIMODict[region][TF] = likelihood
	FIMOFile.close()
	return FIMODict


def getFIMOTFChanges(FIMOOneFileName, FIMOTwoFileName, regionFileName, outputFileName):
	# Get the following information comparing the 2 FIMO files for each region:
	# Column 1: Number of TFs with motif in file 1 but not in file 2
	# Column 2: Number of TFs with motif in file 2 but not in file 1
	# Column 3: Number of TFs with larger likelihood in file 1 than in file 2 (TFs with gained motifs included)
	# Column 4: Number of TFs with larger likelihood in file 2 than in file 1 (TFs with gained motifs included)
	FIMOOneDict = getFIMODict(FIMOOneFileName)
	FIMOTwoDict = getFIMODict(FIMOTwoFileName)
	regionFile = open(regionFileName)
	outputFile = open(outputFileName, 'w+')
	for line in regionFile:
		# Iterate through the regions and find the TF information for each
		region = line.strip()
		TFGainCount = 0
		TFLossCount = 0
		likelihoodUpCount = 0
		likelihoodDownCount = 0
		if region in FIMOOneDict:
			# The region is in the first FIMO dictionary
			if region in FIMOTwoDict:
				# The region is in the second FIMO dictionary

				for TF in FIMOOneDict[region]:
					# Iterate through the TFs in the first FIMO dictionary entry for the region
					if TF == "ZNF263":
						continue
					if TF in FIMOTwoDict[region]:
						# Check if the likelihood differs for the TF
						if FIMOOneDict[region][TF] > FIMOTwoDict[region][TF]:
							# The likelihood is higher in the first FIMO file
							likelihoodUpCount = likelihoodUpCount + 1
						elif FIMOOneDict[region][TF] < FIMOTwoDict[region][TF]:
							# The likelihood is higher in the second FIMO file
							likelihoodDownCount = likelihoodDownCount + 1
					else:
						TFGainCount = TFGainCount + 1
						likelihoodUpCount = likelihoodUpCount + 1
				for TF in FIMOTwoDict[region]:
					# Iterate through the TFs in the second FIMO dictionary entry for the region
					if TF == "ZNF263":
						continue
					if TF not in FIMOOneDict[region]:
						# The TF is not in the first FIMO dictionary for the region
						TFLossCount = TFLossCount + 1
						likelihoodDownCount = likelihoodDownCount + 1

			else:
				TFGainCount = TFGainCount + len(FIMOOneDict[region])
				likelihoodUpCount = likelihoodUpCount + len(FIMOOneDict[region])
				if "ZNF263" in FIMOOneDict[region]:
					TFGainCount = TFGainCount - 1
					likelihoodUpCount = likelihoodUpCount - 1
		elif region in FIMOTwoDict:
			TFLossCount = TFLossCount + len(FIMOTwoDict[region])
			likelihoodDownCount = likelihoodDownCount + len(FIMOTwoDict[region])
			if "ZNF263" in FIMOTwoDict[region]:
				TFLossCount = TFLossCount - 1
				likelihoodDownCount = likelihoodDownCount - 1
		outputFile.write(region + "\t" + str(TFGainCount) + "\t" + str(TFLossCount) + "\t" + str(likelihoodUpCount) + "\t" + str(likelihoodDownCount) + "\n")


if __name__=="__main__":
   import sys
   FIMOOneFileName = sys.argv[1] # Name of the first FIMO file
   FIMOTwoFileName = sys.argv[2] # Name of the second FIMO file
   regionFileName = sys.argv[3]
   outputFileName = sys.argv[4]

   getFIMOTFChanges(FIMOOneFileName, FIMOTwoFileName, regionFileName, outputFileName)
