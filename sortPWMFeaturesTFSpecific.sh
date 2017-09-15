cat ../PWMData/HumanDDFibroblastSubFeatures100bpTFChanged ../PWMData/HumanDDFibroblastInsertFeatures100bpTFChanged ../PWMData/HumanDDFibroblastDelFeatures100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiffFUnsorted100bpTFChanged
cat ../PWMData/HumanDDFibroblastSubFeaturesUp100bpTFChanged ../PWMData/HumanDDFibroblastInsertFeaturesUp100bpTFChanged ../PWMData/HumanDDFibroblastDelFeaturesUp100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiffFUnsortedUp100bpTFChanged
cat ../PWMData/HumanDDFibroblastSubFeaturesDown100bpTFChanged ../PWMData/HumanDDFibroblastInsertFeaturesDown100bpTFChanged ../PWMData/HumanDDFibroblastDelFeaturesDown100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiffFUnsortedDown100bpTFChanged
cat ../PWMData/HumanDDFibroblastSub100kbFeatures100bpTFChanged ../PWMData/HumanDDFibroblastInsert100kbFeatures100bpTFChanged ../PWMData/HumanDDFibroblastDel100kbFeatures100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsorted100bpTFChanged
cat ../PWMData/HumanDDFibroblastSub100kbFeaturesUp100bpTFChanged ../PWMData/HumanDDFibroblastInsert100kbFeaturesUp100bpTFChanged ../PWMData/HumanDDFibroblastDel100kbFeaturesUp100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsortedUp100bpTFChanged
cat ../PWMData/HumanDDFibroblastSub100kbFeaturesDown100bpTFChanged ../PWMData/HumanDDFibroblastInsert100kbFeaturesDown100bpTFChanged ../PWMData/HumanDDFibroblastDel100kbFeaturesDown100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsortedDown100bpTFChanged
cat ../PWMData/CommonFibroblastSubFeatures100bpTFChanged ../PWMData/CommonFibroblastInsertFeatures100bpTFChanged ../PWMData/CommonFibroblastDelFeatures100bpTFChanged > ../PWMData/CommonFibroblastSeqDiffFUnsorted100bpTFChanged
cat ../PWMData/CommonFibroblastSubFeaturesUp100bpTFChanged ../PWMData/CommonFibroblastInsertFeaturesUp100bpTFChanged ../PWMData/CommonFibroblastDelFeaturesUp100bpTFChanged > ../PWMData/CommonFibroblastSeqDiffFUnsortedUp100bpTFChanged
cat ../PWMData/CommonFibroblastSubFeaturesDown100bpTFChanged ../PWMData/CommonFibroblastInsertFeaturesDown100bpTFChanged ../PWMData/CommonFibroblastDelFeaturesDown100bpTFChanged > ../PWMData/CommonFibroblastSeqDiffFUnsortedDown100bpTFChanged
cat ../PWMData/CommonFibroblastSub100kbFeatures100bpTFChanged ../PWMData/CommonFibroblastInsert100kbFeatures100bpTFChanged ../PWMData/CommonFibroblastDel100kbFeatures100bpTFChanged > ../PWMData/CommonFibroblastSeqDiff100kbFUnsorted100bpTFChanged
cat ../PWMData/CommonFibroblastSub100kbFeaturesUp100bpTFChanged ../PWMData/CommonFibroblastInsert100kbFeaturesUp100bpTFChanged ../PWMData/CommonFibroblastDel100kbFeaturesUp100bpTFChanged > ../PWMData/CommonFibroblastSeqDiff100kbFUnsortedUp100bpTFChanged
cat ../PWMData/CommonFibroblastSub100kbFeaturesDown100bpTFChanged ../PWMData/CommonFibroblastInsert100kbFeaturesDown100bpTFChanged ../PWMData/CommonFibroblastDel100kbFeaturesDown100bpTFChanged > ../PWMData/CommonFibroblastSeqDiff100kbFUnsortedDown100bpTFChanged

paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiffFUnsorted100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiffFULoc100bpTFChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiffFUnsortedUp100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiffFULocUp100bpTFChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiffFUnsortedDown100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiffFULocDown100bpTFChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsorted100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFULoc100bpTFChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsortedUp100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFULocUp100bpTFChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsortedDown100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFULocDown100bpTFChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiffFUnsorted100bpTFChanged > ../PWMData/CommonFibroblastSeqDiffFULoc100bpTFChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiffFUnsortedUp100bpTFChanged > ../PWMData/CommonFibroblastSeqDiffFULocUp100bpTFChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiffFUnsortedDown100bpTFChanged > ../PWMData/CommonFibroblastSeqDiffFULocDown100bpTFChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiff100kbFUnsorted100bpTFChanged > ../PWMData/CommonFibroblastSeqDiff100kbFULoc100bpTFChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiff100kbFUnsortedUp100bpTFChanged > ../PWMData/CommonFibroblastSeqDiff100kbFULocUp100bpTFChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiff100kbFUnsortedDown100bpTFChanged > ../PWMData/CommonFibroblastSeqDiff100kbFULocDown100bpTFChanged

sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiffFULoc100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiffFSLoc100bpTFChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiffFULocUp100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiffFSLocUp100bpTFChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiffFULocDown100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiffFSLocDown100bpTFChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiff100kbFULoc100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFSLoc100bpTFChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiff100kbFULocUp100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFSLocUp100bpTFChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiff100kbFULocDown100bpTFChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFSLocDown100bpTFChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiffFULoc100bpTFChanged > ../PWMData/CommonFibroblastSeqDiffFSLoc100bpTFChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiffFULocUp100bpTFChanged > ../PWMData/CommonFibroblastSeqDiffFSLocUp100bpTFChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiffFULocDown100bpTFChanged > ../PWMData/CommonFibroblastSeqDiffFSLocDown100bpTFChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiff100kbFULoc100bpTFChanged > ../PWMData/CommonFibroblastSeqDiff100kbFSLoc100bpTFChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiff100kbFULocUp100bpTFChanged > ../PWMData/CommonFibroblastSeqDiff100kbFSLocUp100bpTFChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiff100kbFULocDown100bpTFChanged > ../PWMData/CommonFibroblastSeqDiff100kbFSLocDown100bpTFChanged

cat ../PWMData/HumanDDFibroblastSubFeatures100bpLikelihoodChanged ../PWMData/HumanDDFibroblastInsertFeatures100bpLikelihoodChanged ../PWMData/HumanDDFibroblastDelFeatures100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiffFUnsorted100bpLikelihoodChanged
cat ../PWMData/HumanDDFibroblastSubFeaturesUp100bpLikelihoodChanged ../PWMData/HumanDDFibroblastInsertFeaturesUp100bpLikelihoodChanged ../PWMData/HumanDDFibroblastDelFeaturesUp100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiffFUnsortedUp100bpLikelihoodChanged
cat ../PWMData/HumanDDFibroblastSubFeaturesDown100bpLikelihoodChanged ../PWMData/HumanDDFibroblastInsertFeaturesDown100bpLikelihoodChanged ../PWMData/HumanDDFibroblastDelFeaturesDown100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiffFUnsortedDown100bpLikelihoodChanged
cat ../PWMData/HumanDDFibroblastSub100kbFeatures100bpLikelihoodChanged ../PWMData/HumanDDFibroblastInsert100kbFeatures100bpLikelihoodChanged ../PWMData/HumanDDFibroblastDel100kbFeatures100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsorted100bpLikelihoodChanged
cat ../PWMData/HumanDDFibroblastSub100kbFeaturesUp100bpLikelihoodChanged ../PWMData/HumanDDFibroblastInsert100kbFeaturesUp100bpLikelihoodChanged ../PWMData/HumanDDFibroblastDel100kbFeaturesUp100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsortedUp100bpLikelihoodChanged
cat ../PWMData/HumanDDFibroblastSub100kbFeaturesDown100bpLikelihoodChanged ../PWMData/HumanDDFibroblastInsert100kbFeaturesDown100bpLikelihoodChanged ../PWMData/HumanDDFibroblastDel100kbFeaturesDown100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsortedDown100bpLikelihoodChanged
cat ../PWMData/CommonFibroblastSubFeatures100bpLikelihoodChanged ../PWMData/CommonFibroblastInsertFeatures100bpLikelihoodChanged ../PWMData/CommonFibroblastDelFeatures100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiffFUnsorted100bpLikelihoodChanged
cat ../PWMData/CommonFibroblastSubFeaturesUp100bpLikelihoodChanged ../PWMData/CommonFibroblastInsertFeaturesUp100bpLikelihoodChanged ../PWMData/CommonFibroblastDelFeaturesUp100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiffFUnsortedUp100bpLikelihoodChanged
cat ../PWMData/CommonFibroblastSubFeaturesDown100bpLikelihoodChanged ../PWMData/CommonFibroblastInsertFeaturesDown100bpLikelihoodChanged ../PWMData/CommonFibroblastDelFeaturesDown100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiffFUnsortedDown100bpLikelihoodChanged
cat ../PWMData/CommonFibroblastSub100kbFeatures100bpLikelihoodChanged ../PWMData/CommonFibroblastInsert100kbFeatures100bpLikelihoodChanged ../PWMData/CommonFibroblastDel100kbFeatures100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiff100kbFUnsorted100bpLikelihoodChanged
cat ../PWMData/CommonFibroblastSub100kbFeaturesUp100bpLikelihoodChanged ../PWMData/CommonFibroblastInsert100kbFeaturesUp100bpLikelihoodChanged ../PWMData/CommonFibroblastDel100kbFeaturesUp100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiff100kbFUnsortedUp100bpLikelihoodChanged
cat ../PWMData/CommonFibroblastSub100kbFeaturesDown100bpLikelihoodChanged ../PWMData/CommonFibroblastInsert100kbFeaturesDown100bpLikelihoodChanged ../PWMData/CommonFibroblastDel100kbFeaturesDown100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiff100kbFUnsortedDown100bpLikelihoodChanged

paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiffFUnsorted100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiffFULoc100bpLikelihoodChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiffFUnsortedUp100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiffFULocUp100bpLikelihoodChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiffFUnsortedDown100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiffFULocDown100bpLikelihoodChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsorted100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFULoc100bpLikelihoodChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsortedUp100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFULocUp100bpLikelihoodChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsortedDown100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFULocDown100bpLikelihoodChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiffFUnsorted100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiffFULoc100bpLikelihoodChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiffFUnsortedUp100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiffFULocUp100bpLikelihoodChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiffFUnsortedDown100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiffFULocDown100bpLikelihoodChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiff100kbFUnsorted100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiff100kbFULoc100bpLikelihoodChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiff100kbFUnsortedUp100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiff100kbFULocUp100bpLikelihoodChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiff100kbFUnsortedDown100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiff100kbFULocDown100bpLikelihoodChanged

sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiffFULoc100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiffFSLoc100bpLikelihoodChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiffFULocUp100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiffFSLocUp100bpLikelihoodChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiffFULocDown100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiffFSLocDown100bpLikelihoodChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiff100kbFULoc100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFSLoc100bpLikelihoodChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiff100kbFULocUp100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFSLocUp100bpLikelihoodChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiff100kbFULocDown100bpLikelihoodChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFSLocDown100bpLikelihoodChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiffFULoc100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiffFSLoc100bpLikelihoodChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiffFULocUp100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiffFSLocUp100bpLikelihoodChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiffFULocDown100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiffFSLocDown100bpLikelihoodChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiff100kbFULoc100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiff100kbFSLoc100bpLikelihoodChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiff100kbFULocUp100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiff100kbFSLocUp100bpLikelihoodChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiff100kbFULocDown100bpLikelihoodChanged > ../PWMData/CommonFibroblastSeqDiff100kbFSLocDown100bpLikelihoodChanged

cat ../PWMData/HumanDDFibroblastSubFeatures100bpDistanceChanged ../PWMData/HumanDDFibroblastInsertFeatures100bpDistanceChanged ../PWMData/HumanDDFibroblastDelFeatures100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiffFUnsorted100bpDistanceChanged
cat ../PWMData/HumanDDFibroblastSubFeaturesUp100bpDistanceChanged ../PWMData/HumanDDFibroblastInsertFeaturesUp100bpDistanceChanged ../PWMData/HumanDDFibroblastDelFeaturesUp100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiffFUnsortedUp100bpDistanceChanged
cat ../PWMData/HumanDDFibroblastSubFeaturesDown100bpDistanceChanged ../PWMData/HumanDDFibroblastInsertFeaturesDown100bpDistanceChanged ../PWMData/HumanDDFibroblastDelFeaturesDown100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiffFUnsortedDown100bpDistanceChanged
cat ../PWMData/HumanDDFibroblastSub100kbFeatures100bpDistanceChanged ../PWMData/HumanDDFibroblastInsert100kbFeatures100bpDistanceChanged ../PWMData/HumanDDFibroblastDel100kbFeatures100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsorted100bpDistanceChanged
cat ../PWMData/HumanDDFibroblastSub100kbFeaturesUp100bpDistanceChanged ../PWMData/HumanDDFibroblastInsert100kbFeaturesUp100bpDistanceChanged ../PWMData/HumanDDFibroblastDel100kbFeaturesUp100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsortedUp100bpDistanceChanged
cat ../PWMData/HumanDDFibroblastSub100kbFeaturesDown100bpDistanceChanged ../PWMData/HumanDDFibroblastInsert100kbFeaturesDown100bpDistanceChanged ../PWMData/HumanDDFibroblastDel100kbFeaturesDown100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsortedDown100bpDistanceChanged
cat ../PWMData/CommonFibroblastSubFeatures100bpDistanceChanged ../PWMData/CommonFibroblastInsertFeatures100bpDistanceChanged ../PWMData/CommonFibroblastDelFeatures100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiffFUnsorted100bpDistanceChanged
cat ../PWMData/CommonFibroblastSubFeaturesUp100bpDistanceChanged ../PWMData/CommonFibroblastInsertFeaturesUp100bpDistanceChanged ../PWMData/CommonFibroblastDelFeaturesUp100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiffFUnsortedUp100bpDistanceChanged
cat ../PWMData/CommonFibroblastSubFeaturesDown100bpDistanceChanged ../PWMData/CommonFibroblastInsertFeaturesDown100bpDistanceChanged ../PWMData/CommonFibroblastDelFeaturesDown100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiffFUnsortedDown100bpDistanceChanged
cat ../PWMData/CommonFibroblastSub100kbFeatures100bpDistanceChanged ../PWMData/CommonFibroblastInsert100kbFeatures100bpDistanceChanged ../PWMData/CommonFibroblastDel100kbFeatures100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiff100kbFUnsorted100bpDistanceChanged
cat ../PWMData/CommonFibroblastSub100kbFeaturesUp100bpDistanceChanged ../PWMData/CommonFibroblastInsert100kbFeaturesUp100bpDistanceChanged ../PWMData/CommonFibroblastDel100kbFeaturesUp100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiff100kbFUnsortedUp100bpDistanceChanged
cat ../PWMData/CommonFibroblastSub100kbFeaturesDown100bpDistanceChanged ../PWMData/CommonFibroblastInsert100kbFeaturesDown100bpDistanceChanged ../PWMData/CommonFibroblastDel100kbFeaturesDown100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiff100kbFUnsortedDown100bpDistanceChanged

paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiffFUnsorted100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiffFULoc100bpDistanceChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiffFUnsortedUp100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiffFULocUp100bpDistanceChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiffFUnsortedDown100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiffFULocDown100bpDistanceChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsorted100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFULoc100bpDistanceChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsortedUp100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFULocUp100bpDistanceChanged
paste ../DNaseRegionData/HumanDDFibroblastSeqDiffs100bp ../PWMData/HumanDDFibroblastSeqDiff100kbFUnsortedDown100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFULocDown100bpDistanceChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiffFUnsorted100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiffFULoc100bpDistanceChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiffFUnsortedUp100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiffFULocUp100bpDistanceChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiffFUnsortedDown100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiffFULocDown100bpDistanceChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiff100kbFUnsorted100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiff100kbFULoc100bpDistanceChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiff100kbFUnsortedUp100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiff100kbFULocUp100bpDistanceChanged
paste ../DNaseRegionData/CommonFibroblastSeqDiffs100bp ../PWMData/CommonFibroblastSeqDiff100kbFUnsortedDown100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiff100kbFULocDown100bpDistanceChanged

sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiffFULoc100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiffFSLoc100bpDistanceChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiffFULocUp100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiffFSLocUp100bpDistanceChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiffFULocDown100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiffFSLocDown100bpDistanceChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiff100kbFULoc100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFSLoc100bpDistanceChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiff100kbFULocUp100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFSLocUp100bpDistanceChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanDDFibroblastSeqDiff100kbFULocDown100bpDistanceChanged > ../PWMData/HumanDDFibroblastSeqDiff100kbFSLocDown100bpDistanceChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiffFULoc100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiffFSLoc100bpDistanceChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiffFULocUp100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiffFSLocUp100bpDistanceChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiffFULocDown100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiffFSLocDown100bpDistanceChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiff100kbFULoc100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiff100kbFSLoc100bpDistanceChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiff100kbFULocUp100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiff100kbFSLocUp100bpDistanceChanged
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastSeqDiff100kbFULocDown100bpDistanceChanged > ../PWMData/CommonFibroblastSeqDiff100kbFSLocDown100bpDistanceChanged

python combineFeatureFiles.py ../DNaseRegionData/HumanDDFibroblastSeqDiffsSorted100bp ../FeatureData/HumanDDFibroblastFeatureFileNames ../FeatureData/HumanDDFibroblastFeatures100bp
python combineFeatureFiles.py ../DNaseRegionData/HumanDDFibroblastSeqDiffsSorted100bp ../FeatureData/HumanDDFibroblastFeatureFileNamesUp ../FeatureData/HumanDDFibroblastFeaturesUp100bp
python combineFeatureFiles.py ../DNaseRegionData/HumanDDFibroblastSeqDiffsSorted100bp ../FeatureData/HumanDDFibroblastFeatureFileNamesDown ../FeatureData/HumanDDFibroblastFeaturesDown100bp
python combineFeatureFiles.py ../DNaseRegionData/CommonFibroblastSeqDiffsSorted100bp ../FeatureData/CommonFibroblastFeatureFileNames ../FeatureData/CommonFibroblastFeatures100bp
python combineFeatureFiles.py ../DNaseRegionData/CommonFibroblastSeqDiffsSorted100bp ../FeatureData/CommonFibroblastFeatureFileNamesUp ../FeatureData/CommonFibroblastFeaturesUp100bp
python combineFeatureFiles.py ../DNaseRegionData/CommonFibroblastSeqDiffsSorted100bp ../FeatureData/CommonFibroblastFeatureFileNamesDown ../FeatureData/CommonFibroblastFeaturesDown100bp
