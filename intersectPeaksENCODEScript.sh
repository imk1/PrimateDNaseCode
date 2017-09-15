intersectBed -a ../DNasePeaks/HumanFibroblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/AG10803Merged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged
intersectBed -a ../DNasePeaks/HumanFibroblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/NHDF_AdMerged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged
intersectBed -a ../DNasePeaks/HumanFibroblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/NHDF_NeoMerged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged
intersectBed -a ../DNasePeaks/HumanFibroblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/allSkinFibroblastMerged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged
intersectBed -a ../DNasePeaks/HumanFibroblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/GM06990Merged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged
intersectBed -a ../DNasePeaks/HumanFibroblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/GM12865Merged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged
intersectBed -a ../DNasePeaks/HumanFibroblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/allLCLMerged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged

intersectBed -a ../DNasePeaks/HumanLymphoblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/AG10803Merged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged
intersectBed -a ../DNasePeaks/HumanLymphoblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/NHDF_AdMerged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged
intersectBed -a ../DNasePeaks/HumanLymphoblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/NHDF_NeoMerged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged
intersectBed -a ../DNasePeaks/HumanLymphoblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/allSkinFibroblastMerged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged
intersectBed -a ../DNasePeaks/HumanLymphoblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/GM06990Merged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged
intersectBed -a ../DNasePeaks/HumanLymphoblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/GM12865Merged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged
intersectBed -a ../DNasePeaks/HumanLymphoblastAllPeaks_peaksSortedMerged.bed -b ../ENCODEData/allLCLMerged.peaks.hg19.bed > temp
sort -u -k1,1 -k2,2n -k3,3n temp > tempSorted
mergeBed -i tempSorted -d -15 > tempMerged
wc tempMerged
