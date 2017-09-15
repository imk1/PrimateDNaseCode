#!/usr/bin/env python2.4
"""
Create a bed file listing all the divergent sites between three specific species 
in a maf.  This identifies sites that are different between the reference and the two other species, and the other two species are the same.  It identifies only substitutions (not insertions and deletions).

usage: %prog maf_file reference_species_name other_species_one_name other_species_two_name
"""

import sys
import bx.align.maf
import bx.bitset
from bx.bitset_builders import *
from itertools import *


bitsets = {}
bitsetsOtherOne = {} # Will hold the locations of the first non-ref. species where the seq. differs from the ref. species
bitsetsOtherTwo = {} # Will hold the locations of the second non-ref. species where the seq. differs from the ref. species
substitutionsChromsOtherOne = {} # Will hold the chromosomes that the substitutions are on in the first other species
substitutionsChromsOtherTwo = {} # Will hold the chromosomes that the substitutions are on in the second other species
maf = sys.argv[1]
reference_sp, other_sp_one, other_sp_two = sys.argv[2], sys.argv[3], sys.argv[4]
outputFileNameOne = sys.argv[5] # Will hold the substitution locations for the first other species
outputFileNameTwo = sys.argv[6] # Will hold the substitution locations for the second other species

for block in bx.align.maf.Reader( open(maf) ):
	# Iterate through maf blocks
	ref = block.get_component_by_src_start( reference_sp )
	other_one = block.get_component_by_src_start( other_sp_one )
	other_two = block.get_component_by_src_start( other_sp_two )

	if (not ref or not other_one) or (not other_two): continue # Do not consider sequences from non-listed species
	ref_chrom = ref.src.split( '.' )[1]
	ref_start = ref.start
	ref_end = ref.end
	chrom_size = ref.get_src_size()
	other_one_chrom = other_one.src.split( '.' )[1]
	other_one_start = other_one.start
	other_one_end = other_one.end
	other_one_chrom_size = other_one.get_src_size()
	other_two_chrom = other_two.src.split( '.' )[1]
	other_two_start = other_two.start
	other_two_end = other_two.end
	other_two_chrom_size = other_two.get_src_size()

	if ref_chrom not in bitsets:
		# Create new dictionary entries for the current chromosome
		bitsets[ ref_chrom ] = bx.bitset.BinnedBitSet( chrom_size )
		bitsetsOtherOne[ ref_chrom ] = bx.bitset.BinnedBitSet( other_one_chrom_size ) # INDEXED BY REFERENCE CHROMOSOME
		bitsetsOtherTwo[ ref_chrom ] = bx.bitset.BinnedBitSet( other_two_chrom_size ) # INDEXED BY REFERENCE CHROMOSOME
		substitutionsChromsOtherOne[ ref_chrom ] = [] # INDEXED BY REFERENCE CHROMOSOME
		substitutionsChromsOtherTwo[ ref_chrom ] = [] # INDEXED BY REFERENCE CHROMOSOME

	pos = ref_start
	posOtherOne = other_one_start
	posOtherTwo = other_two_start
	for i,j,k in izip( ref.text.upper(), other_one.text.upper(), other_two.text.upper() ):
		# Iterate through sequences and identify differences
		if i != '-':
			# Not a deletion in the reference
			if (i != j) and (j == k): # mismatch between reference and others, but others agree
				if i != 'N' and j != 'N' and j != '-': 
					# set if all valid chars
					bitsets[ ref_chrom ].set( pos )
					bitsetsOtherOne[ ref_chrom ].set( posOtherOne )
					bitsetsOtherTwo[ ref_chrom ].set( posOtherTwo )
					substitutionsChromsOtherOne[ ref_chrom ].append(other_one_chrom)
					substitutionsChromsOtherTwo[ ref_chrom ].append(other_two_chrom)
			pos += 1
		if j != '-':
			# Not a deletion in the first other species
			posOtherOne += 1
		if k != '-':
			# Not a deletion in the second other species
			posOtherTwo += 1

	
# bits --> bed file
outputFileOne = open(outputFileNameOne, 'w+')
outputFileTwo = open(outputFileNameTwo, 'w+')
for chrom in bitsets:
	# Print the data from each chromosome
	bits = bitsets[chrom]
	bitsOtherOne = bitsetsOtherOne[chrom]
	bitsOtherTwo = bitsetsOtherTwo[chrom]
	substitutionCount = 0
	end = 0
	while 1:
		# Iterate through sequence differences and print each
		start = bits.next_set( end )
		if start == bits.size: break # At end of sequence differences list for the current chromosome
		end = bits.next_clear( start )
		print "%s\t%d\t%d\n" % ( chrom, start, end )
		chromOtherOne = substitutionsChromsOtherOne[ ref_chrom ][substitutionCount]
		startOtherOne = bitsOtherOne.next_set( endOtherOne )
		endOtherOne = bitsOtherOne.next_clear( startOtherOne )
		outputFileOne.write(chromOtherOne + "\t" + str(startOtherOne) + "\t" + str(endOtherOne) + "\n")
		chromOtherTwo = substitutionsChromsOtherTwo[ ref_chrom ][substitutionCount]
		startOtherTwo = bitsOtherTwo.next_set( endOtherTwo )
		endOtherTwo = bitsOtherTwo.next_clear( startOtherTwo )
		outputFileTwo.write(chromOtherTwo + "\t" + str(startOtherTwo) + "\t" + str(endOtherTwo) + "\n")
		substitutionCount = substitutionCount + 1
outputFileOne.close()
outputFileTwo.close()

