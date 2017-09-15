import sys
import argparse
import pybedtools as bt

def parseArgument():
	# Parse the input
	parser = argparse.ArgumentParser(description="Make fasta files for regions surrounding peak summits")
	parser.add_argument("--narrowPeakListFileName", required=True, help="List of narrowPeak files")
	parser.add_argument("--genomeFileName", required=False, default="/mnt/data/annotations/by_organism/human/hg20.GRCh38/GRCh38.genome.fa",\
		help="Name of fasta file with genome sequence")
	parser.add_argument("--summitDist", required=False, type=int, default=1000,\
		help="Distance from peak summit in each direction whose sequence will be extracted")
	options = parser.parse_args()
	return options

def makeSurroundingSummitFastas(options):
	narrowPeakListFile = open(options.narrowPeakListFileName)
	for line in narrowPeakListFile:
		# Iterate through the peak files and make a fasta file for the region around each peak's summit
		narrowPeakFileName = line.strip()
		narrowPeakFileNameElements = narrowPeakFileName.split(".")
		narrowPeakFileNamePrefix = ".".join(narrowPeakFileNameElements[0:-2])
		bedFileName = narrowPeakFileNamePrefix + ".summitPlusMinus" + str(options.summitDist) + "bp.bed"
		if not os.path.isfile(bedFileName):
			# Make a bed file
			if os.path.isfile(narrowPeakFileName):
				# The file is gzipped
				os.system(" ".join(["zcat", narrowPeakFileName, \
					"| grep -v chrUn | grep -v random | awk 'BEGIN{OFS=\"\t\"} print $1,$2+10-" + str(options.summitDist) + ",$2+$10+" + str(options.summitDist), \
					"| sort -k1,1 -k2,2n -k3,3n -k10,10n >", bedFileName]))
			else:
				# The file is not gzipped
				os.system(" ".join(["| grep -v chrUn", ".".join(narrowPeakFileNameElements[0:-1], \
					"| grep -v random | awk 'BEGIN{OFS=\"\t\"} print $1,$2+10-" + str(options.summitDist) + ",$2+$10+" + str(options.summitDist), \
					"| sort -k1,1 -k2,2n -k3,3n -k10,10n >", bedFileName]))
		regionList = bt.BedTool(bedFileName)
		fastaFileName = narrowPeakFileNamePrefix + ".summitPlusMinus" + str(options.summitDist) + "bp.fa"
		fastaList = regionList.sequence(fi = options.genomeFileName, fo = fastaFileName)
		os.remove(bedFileName)
	narrowPeakListFile.close()

if __name__ == "__main__":
	options = parseArgument()
	makeSurroundingSummitFastas(options)
