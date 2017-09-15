def makeGetUniqueMersScript(uniqueMersFileListFileName, outputFileNameSuffix, scriptFileName):
	# Make a script that gets the unique mers from lists of files
	uniqueMersFileListFile = open(uniqueMersFileListFileName)
	scriptFile = open(scriptFileName, 'w+')
	for line in uniqueMersFileListFile:
		# Iterate through the names of the files with lists of file names of files with unique mers and add the command to get the unique mers for each to the script file
		scriptFile.write("python /science/irene/PrimateSNPProject/src/getUniqueMers.py " + line.strip() + " " + line.strip() + outputFileNameSuffix + "\n")
	uniqueMersFileListFile.close()
	scriptFile.close()

if __name__=="__main__":
   import sys
   uniqueMersFileListFileName = sys.argv[1] 
   outputFileNameSuffix = sys.argv[2]
   scriptFileName = sys.argv[3]
   makeGetUniqueMersScript(uniqueMersFileListFileName, outputFileNameSuffix, scriptFileName)
