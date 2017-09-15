cat ../PWMData/HumanUpFibroblastFDR1SubFeatures100bp ../PWMData/HumanUpFibroblastFDR1InsertFeatures100bp ../PWMData/HumanUpFibroblastFDR1DelFeatures100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiffFUnsorted100bp
cat ../PWMData/HumanUpFibroblastFDR1SubFeaturesUp100bp ../PWMData/HumanUpFibroblastFDR1InsertFeaturesUp100bp ../PWMData/HumanUpFibroblastFDR1DelFeaturesUp100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiffFUnsortedUp100bp
cat ../PWMData/HumanUpFibroblastFDR1SubFeaturesDown100bp ../PWMData/HumanUpFibroblastFDR1InsertFeaturesDown100bp ../PWMData/HumanUpFibroblastFDR1DelFeaturesDown100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiffFUnsortedDown100bp
#cat ../PWMData/HumanUpFibroblastFDR1Sub100kbFeatures100bp ../PWMData/HumanUpFibroblastFDR1Insert100kbFeatures100bp ../PWMData/HumanUpFibroblastFDR1Del100kbFeatures100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFUnsorted100bp
#cat ../PWMData/HumanUpFibroblastFDR1Sub100kbFeaturesUp100bp ../PWMData/HumanUpFibroblastFDR1Insert100kbFeaturesUp100bp ../PWMData/HumanUpFibroblastFDR1Del100kbFeaturesUp100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFUnsortedUp100bp
#cat ../PWMData/HumanUpFibroblastFDR1Sub100kbFeaturesDown100bp ../PWMData/HumanUpFibroblastFDR1Insert100kbFeaturesDown100bp ../PWMData/HumanUpFibroblastFDR1Del100kbFeaturesDown100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFUnsortedDown100bp
cat ../PWMData/CommonFibroblastFDR1SubFeatures100bp ../PWMData/CommonFibroblastFDR1InsertFeatures100bp ../PWMData/CommonFibroblastFDR1DelFeatures100bp > ../PWMData/CommonFibroblastFDR1SeqDiffFUnsorted100bp
cat ../PWMData/CommonFibroblastFDR1SubFeaturesUp100bp ../PWMData/CommonFibroblastFDR1InsertFeaturesUp100bp ../PWMData/CommonFibroblastFDR1DelFeaturesUp100bp > ../PWMData/CommonFibroblastFDR1SeqDiffFUnsortedUp100bp
cat ../PWMData/CommonFibroblastFDR1SubFeaturesDown100bp ../PWMData/CommonFibroblastFDR1InsertFeaturesDown100bp ../PWMData/CommonFibroblastFDR1DelFeaturesDown100bp > ../PWMData/CommonFibroblastFDR1SeqDiffFUnsortedDown100bp
#cat ../PWMData/CommonFibroblastFDR1Sub100kbFeatures100bp ../PWMData/CommonFibroblastFDR1Insert100kbFeatures100bp ../PWMData/CommonFibroblastFDR1Del100kbFeatures100bp > ../PWMData/CommonFibroblastFDR1SeqDiff100kbFUnsorted100bp
#cat ../PWMData/CommonFibroblastFDR1Sub100kbFeaturesUp100bp ../PWMData/CommonFibroblastFDR1Insert100kbFeaturesUp100bp ../PWMData/CommonFibroblastFDR1Del100kbFeaturesUp100bp > ../PWMData/CommonFibroblastFDR1SeqDiff100kbFUnsortedUp100bp
#cat ../PWMData/CommonFibroblastFDR1Sub100kbFeaturesDown100bp ../PWMData/CommonFibroblastFDR1Insert100kbFeaturesDown100bp ../PWMData/CommonFibroblastFDR1Del100kbFeaturesDown100bp > ../PWMData/CommonFibroblastFDR1SeqDiff100kbFUnsortedDown100bp

paste ../DNaseRegionData/HumanUpFibroblastFDR1SeqDiffs100bp ../PWMData/HumanUpFibroblastFDR1SeqDiffFUnsorted100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiffFULoc100bp
paste ../DNaseRegionData/HumanUpFibroblastFDR1SeqDiffs100bp ../PWMData/HumanUpFibroblastFDR1SeqDiffFUnsortedUp100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiffFULocUp100bp
paste ../DNaseRegionData/HumanUpFibroblastFDR1SeqDiffs100bp ../PWMData/HumanUpFibroblastFDR1SeqDiffFUnsortedDown100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiffFULocDown100bp
#paste ../DNaseRegionData/HumanUpFibroblastFDR1SeqDiffs100bp ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFUnsorted100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFULoc100bp
#paste ../DNaseRegionData/HumanUpFibroblastFDR1SeqDiffs100bp ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFUnsortedUp100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFULocUp100bp
#paste ../DNaseRegionData/HumanUpFibroblastFDR1SeqDiffs100bp ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFUnsortedDown100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFULocDown100bp
paste ../DNaseRegionData/CommonFibroblastFDR1SeqDiffs100bp ../PWMData/CommonFibroblastFDR1SeqDiffFUnsorted100bp > ../PWMData/CommonFibroblastFDR1SeqDiffFULoc100bp
paste ../DNaseRegionData/CommonFibroblastFDR1SeqDiffs100bp ../PWMData/CommonFibroblastFDR1SeqDiffFUnsortedUp100bp > ../PWMData/CommonFibroblastFDR1SeqDiffFULocUp100bp
paste ../DNaseRegionData/CommonFibroblastFDR1SeqDiffs100bp ../PWMData/CommonFibroblastFDR1SeqDiffFUnsortedDown100bp > ../PWMData/CommonFibroblastFDR1SeqDiffFULocDown100bp
#paste ../DNaseRegionData/CommonFibroblastFDR1SeqDiffs100bp ../PWMData/CommonFibroblastFDR1SeqDiff100kbFUnsorted100bp > ../PWMData/CommonFibroblastFDR1SeqDiff100kbFULoc100bp
#paste ../DNaseRegionData/CommonFibroblastFDR1SeqDiffs100bp ../PWMData/CommonFibroblastFDR1SeqDiff100kbFUnsortedUp100bp > ../PWMData/CommonFibroblastFDR1SeqDiff100kbFULocUp100bp
#paste ../DNaseRegionData/CommonFibroblastFDR1SeqDiffs100bp ../PWMData/CommonFibroblastFDR1SeqDiff100kbFUnsortedDown100bp > ../PWMData/CommonFibroblastFDR1SeqDiff100kbFULocDown100bp

sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanUpFibroblastFDR1SeqDiffFULoc100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiffFSLoc100bp
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanUpFibroblastFDR1SeqDiffFULocUp100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiffFSLocUp100bp
sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanUpFibroblastFDR1SeqDiffFULocDown100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiffFSLocDown100bp
#sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFULoc100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFSLoc100bp
#sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFULocUp100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFSLocUp100bp
#sort -k1,1 -k2,2n -k3,3n ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFULocDown100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFSLocDown100bp
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastFDR1SeqDiffFULoc100bp > ../PWMData/CommonFibroblastFDR1SeqDiffFSLoc100bp
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastFDR1SeqDiffFULocUp100bp > ../PWMData/CommonFibroblastFDR1SeqDiffFSLocUp100bp
sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastFDR1SeqDiffFULocDown100bp > ../PWMData/CommonFibroblastFDR1SeqDiffFSLocDown100bp
#sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastFDR1SeqDiff100kbFULoc100bp > ../PWMData/CommonFibroblastFDR1SeqDiff100kbFSLoc100bp
#sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastFDR1SeqDiff100kbFULocUp100bp > ../PWMData/CommonFibroblastFDR1SeqDiff100kbFSLocUp100bp
#sort -k1,1 -k2,2n -k3,3n ../PWMData/CommonFibroblastFDR1SeqDiff100kbFULocDown100bp > ../PWMData/CommonFibroblastFDR1SeqDiff100kbFSLocDown100bp

cut -f4,5,6,7,8,9,10,11 ../PWMData/HumanUpFibroblastFDR1SeqDiffFSLoc100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiffFSorted100bp
cut -f4,5,6,7,8,9,10,11 ../PWMData/HumanUpFibroblastFDR1SeqDiffFSLocUp100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiffFSortedUp100bp
cut -f4,5,6,7,8,9,10,11 ../PWMData/HumanUpFibroblastFDR1SeqDiffFSLocDown100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiffFSortedDown100bp
#cut -f4,5,6,7,8,9,10,11 ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFSLoc100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFSorted100bp
#cut -f4,5,6,7,8,9,10,11 ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFSLocUp100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFSortedUp100bp
#cut -f4,5,6,7,8,9,10,11 ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFSLocDown100bp > ../PWMData/HumanUpFibroblastFDR1SeqDiff100kbFSortedDown100bp
cut -f4,5,6,7,8,9,10,11 ../PWMData/CommonFibroblastFDR1SeqDiffFSLoc100bp > ../PWMData/CommonFibroblastFDR1SeqDiffFSorted100bp
cut -f4,5,6,7,8,9,10,11 ../PWMData/CommonFibroblastFDR1SeqDiffFSLocUp100bp > ../PWMData/CommonFibroblastFDR1SeqDiffFSortedUp100bp
cut -f4,5,6,7,8,9,10,11 ../PWMData/CommonFibroblastFDR1SeqDiffFSLocDown100bp > ../PWMData/CommonFibroblastFDR1SeqDiffFSortedDown100bp
#cut -f4,5,6,7,8,9,10,11 ../PWMData/CommonFibroblastFDR1SeqDiff100kbFSLoc100bp > ../PWMData/CommonFibroblastFDR1SeqDiff100kbFSorted100bp
#cut -f4,5,6,7,8,9,10,11 ../PWMData/CommonFibroblastFDR1SeqDiff100kbFSLocUp100bp > ../PWMData/CommonFibroblastFDR1SeqDiff100kbFSortedUp100bp
#cut -f4,5,6,7,8,9,10,11 ../PWMData/CommonFibroblastFDR1SeqDiff100kbFSLocDown100bp > ../PWMData/CommonFibroblastFDR1SeqDiff100kbFSortedDown100bp

#python combineFeatureFiles.py ../DNaseRegionData/HumanUpFibroblastFDR1SeqDiffsSorted100bp ../FeatureData/HumanUpFibroblastFDR1FeatureFileNames ../FeatureData/HumanUpFibroblastFDR1Features100bp
python combineFeatureFiles.py ../DNaseRegionData/HumanUpFibroblastFDR1SeqDiffsSorted100bp ../FeatureData/HumanUpFibroblastFDR1FeatureFileNamesUp ../FeatureData/HumanUpFibroblastFDR1FeaturesUp100bp
#python combineFeatureFiles.py ../DNaseRegionData/HumanUpFibroblastFDR1SeqDiffsSorted100bp ../FeatureData/HumanUpFibroblastFDR1FeatureFileNamesDown ../FeatureData/HumanUpFibroblastFDR1FeaturesDown100bp
#python combineFeatureFiles.py ../DNaseRegionData/CommonFibroblastFDR1SeqDiffsSorted100bp ../FeatureData/CommonFibroblastFDR1FeatureFileNames ../FeatureData/CommonFibroblastFDR1Features100bp
python combineFeatureFiles.py ../DNaseRegionData/CommonFibroblastFDR1SeqDiffsSorted100bp ../FeatureData/CommonFibroblastFDR1FeatureFileNamesUp ../FeatureData/CommonFibroblastFDR1FeaturesUp100bp
#python combineFeatureFiles.py ../DNaseRegionData/CommonFibroblastFDR1SeqDiffsSorted100bp ../FeatureData/CommonFibroblastFDR1FeatureFileNamesDown ../FeatureData/CommonFibroblastFDR1FeaturesDown100bp
