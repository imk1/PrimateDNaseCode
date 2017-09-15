def recordGeneInfo(geneName, chrom, start, end, outFile, geneNameOutFirst):
	# Records a gene and its location to a file
	if geneNameOutFirst == 1:
		# The gene name should go at the beggining of each line in the output file
		outFile.write(geneName)
		outFile.write("\t")
	outFile.write(chrom)
	outFile.write("\t")
	outFile.write(str(start))
	outFile.write("\t")
	outFile.write(str(end))
	if geneNameOutFirst == 0:
		# The gene name goes at the end of each line in the output file
		outFile.write("\t")
		outFile.write(geneName)
	outFile.write("\n")

def mergeTranscripts(geneLocationFileName, outFileName, geneNameCol, chromCol, startCol, endCol, geneNameOutFirst):
	# Iterate through genes, merge multiple transcripts, and output the location of each gene to a file (gene name, chromosome, start, end)
	# ASSUMES THAT ALL TRANSCRIPTS FROM THE SAME GENES HAVE BEEN LISTED CONSECUTIVELY
	# ASSUMES THAT THE LOCATION INFORMATION FOR EACH GENE HAS BEEN SORTED BY CHROMOSOME, THEN BY START, AND THEN BY END
	geneLocationInfoFile = open(geneLocationFileName)
	outFile = open(outFileName, 'w+')
	lastGeneName = ""
	chrom = ""
	start = 0
	end = 0
	for line in geneLocationInfoFile:
		# Iterate through the DNase information for each gene and keep the information for genes that do not need to be filtered
		lineElements = line.split("\t")
		geneName = string.upper(lineElements[geneNameCol].strip())
		if geneName != lastGeneName:
			# A new gene has been reached, so record the information about the last gene
			if chrom != "":
				# The last gene was not filtered, and this is not the first gene, so record
				recordGeneInfo(lastGeneName, chrom, start, end, outFile, geneNameOutFirst)
			chrom = lineElements[chromCol]
			start = int(lineElements[startCol])
			end = int(lineElements[endCol])
			lastGeneName = geneName
		else:
			chromNew = lineElements[chromCol]
			if chromNew != chrom:
				# There are transcripts on different chromosomes, so remove the gene
				print geneName
				print chrom
				print chromNew
				chrom = ""
				continue
			startNew = int(lineElements[startCol])
			if startNew >= end:
				# The transcripts do not overlap, so remove the gene
				# There are transcripts on different chromosomes, so remove the gene
				print geneName
				print end
				print startNew
				chrom = ""
				continue
			endNew = int(lineElements[endCol])
			if endNew > end:
				# The end of the new transcript comes after the end of the old transcript
				end = endNew
	if geneName != "":
		# The final gene should not be filtered, so record its information
		recordGeneInfo(geneName, chrom, start, end, outFile, geneNameOutFirst)
	geneLocationInfoFile.close()
	outFile.close()

if __name__=="__main__":
	import sys
	import string
	geneLocationFileName = sys.argv[1]
	outFileName = sys.argv[2]
	geneNameCol = int(sys.argv[3])
	chromCol = int(sys.argv[4])
	startCol = int(sys.argv[5])
	endCol = int(sys.argv[6])
	geneNameOutFirst = int(sys.argv[7])
                        
	mergeTranscripts(geneLocationFileName, outFileName, geneNameCol, chromCol, startCol, endCol, geneNameOutFirst)
