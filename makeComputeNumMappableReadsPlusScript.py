def makeComputeNumMappableReadsScript(fastaFileNameListFileName, uniqueFileNameSuffix, path, readLength, scriptFileName):
	# Make a script that will compute the number of mappable reads in a fasta file as well as the number of each k-mer
	fastaFileNameListFile = open(fastaFileNameListFileName)
	scriptFile = open(scriptFileName, 'w+')
	for line in fastaFileNameListFile:
		# Iterate through the fasta lines and write the python command for each
		uniqueFileName = path + line.strip() + "." + uniqueFileNameSuffix
		scriptFile.write("python /afs/cs.stanford.edu/u/imk1/scr/PrimateSNPProject/src/computeNumMappableReadsPlus.py " + path + line.strip() + " " + str(readLength) + " " + uniqueFileName + "\n")
	fastaFileNameListFile.close()
	scriptFile.close()

if __name__=="__main__":
   import sys
   fastaFileNameListFileName = sys.argv[1] 
   path = sys.argv[2]
   readLength = int(sys.argv[3])
   scriptFileName = sys.argv[4]
   uniqueFileNameSuffix = sys.argv[5]
   makeComputeNumMappableReadsScript(fastaFileNameListFileName, uniqueFileNameSuffix, path, readLength, scriptFileName)
