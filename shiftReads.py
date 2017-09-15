def shiftReads(readsFileName, readsShiftedFileName, shiftDist):
	# Shift reads so that MACS can run on them
	readsFile = open(readsFileName)
	readsShiftedFile = open(readsShiftedFileName, 'w+')
	for line in readsFile:
		# Iterate through the reads and shift them appropriately
		lineElements = line.split()
		chrom = lineElements[0]
		strand = lineElements[5].strip()
		start = -1
		end = -1
		if strand == "+":
			# Shift the read in the negative direction
			start = int(lineElements[1]) - shiftDist
			end = int(lineElements[2]) - shiftDist
		else:
			start = int(lineElements[1]) + shiftDist
			end = int(lineElements[2]) + shiftDist
		readsShiftedFile.write(chrom + "\t" + str(start) + "\t" + str(end) + "\t" + lineElements[3] + "\t" + lineElements[4] + "\t" + strand + "\n")
	readsFile.close()
	readsShiftedFile.close()

def shiftReadsLoop(readsListFileName, readsShiftedFileNameSuffix, shiftDist):
	# Iterate through the files and shift the reads for all of them
	readsListFile = open(readsListFileName)
	for line in readsListFile:
		# Iterate through the file names with reads and shift each
		print "Shifting reads for " + line.strip()
		readsShiftedFileName = line.strip() + "." + readsShiftedFileNameSuffix
		shiftReads(line.strip(), readsShiftedFileName, shiftDist)
	readsListFile.close()

if __name__=="__main__":
   import sys
   readsListFileName = sys.argv[1] 
   readsShiftedFileNameSuffix = sys.argv[2]
   shiftDist = int(sys.argv[3])
   isLoop = int(sys.argv[4])
   if isLoop == 1:
	# Shift the reads for multiple files
   	shiftReadsLoop(readsListFileName, readsShiftedFileNameSuffix, shiftDist)
   else:
	readsShiftedFileName = readsListFileName + "." + readsShiftedFileNameSuffix
	shiftReads(readsListFileName, readsShiftedFileName, shiftDist)
