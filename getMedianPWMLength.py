def getMedianPWMLength(PWMFileNameListFileName):
	# Get the length of the median PWM
	PWMFileNameListFile = open(PWMFileNameListFileName)
	PWMLengthList = []
	for line in PWMFileNameListFile:
		# Iterate through the PWM files and get the length of each PWM
		PWMFile = open(line.strip())
		PWMLines = PWMFile.readlines()
		lastLine = PWMLines[len(PWMLines) - 1]
		lastLineElements = lastLine.split("\t")
		PWMLengthList.append(int(lastLineElements[0]))
		PWMFile.close()
	PWMFileNameListFile.close()
	PWMLengthArray = numpy.array(PWMLengthList)
	print "Median " + str(numpy.median(PWMLengthArray))
	print "Mean " + str(numpy.mean(PWMLengthArray))

if __name__=="__main__":
   import sys
   import numpy
   PWMFileNameListFileName = sys.argv[1] 
   getMedianPWMLength(PWMFileNameListFileName)
