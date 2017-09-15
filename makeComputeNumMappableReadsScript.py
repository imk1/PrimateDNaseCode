def makeComputeNumMappableReadsScript(fastaFileNameListFileName, outputFileNameSuffix, uniqueFileNameSuffix, path, readLength, scriptFileName):
	# Make a script that will compute the number of mappable reads in a fasta file as well as the number of each k-mer
	fastaFileNameListFile = open(fastaFileNameListFileName)
	scriptFile = open(scriptFileName, 'w+')
	for line in fastaFileNameListFile:
		# Iterate through the fasta lines and write the python command for each
		outputFileName = path + line.strip() + "." + outputFileNameSuffix
		uniqueFileName = path + line.strip() + "." + uniqueFileNameSuffix
		scriptFile.write("python /science/irene/PrimateSNPProject/src/computeNumMappableReads.py " + path + line.strip() + " " + str(readLength) + " " + outputFileName + " " + uniqueFileName + "\n")
	fastaFileNameListFile.close()
	scriptFile.close()

if __name__=="__main__":
   import sys
   fastaFileNameListFileName = sys.argv[1] 
   outputFileNameSuffix = sys.argv[2]
   path = sys.argv[3]
   readLength = int(sys.argv[4])
   scriptFileName = sys.argv[5]
   uniqueFileNameSuffix = sys.argv[6]
   makeComputeNumMappableReadsScript(fastaFileNameListFileName, outputFileNameSuffix, uniqueFileNameSuffix, path, readLength, scriptFileName)
