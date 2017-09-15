#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO30D282M652Filt ../DNasePeaks/HumanUpFibroblastLinesO30 ../DNaseRegionData/HumanUpFibroblastO30 0
#./liftOver ../DNaseRegionData/HumanUpFibroblastO30 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/HumanUpFibroblastO30panTro2 ../DNaseRegionData/HumanUpFibroblastO30Unmapped
#subtractBed -a ../DNaseRegionData/HumanUpFibroblastO30 -b ../DNaseRegionData/HumanUpFibroblastO30Unmapped > ../DNaseRegionData/HumanUpFibroblastO30MappanTro2
#./liftOver ../DNaseRegionData/HumanUpFibroblastO30 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/HumanUpFibroblastO30rheMac2 ../DNaseRegionData/HumanUpFibroblastO30UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/HumanUpFibroblastO30MappanTro2 -b ../DNaseRegionData/HumanUpFibroblastO30UnmappedrheMac2 > ../DNaseRegionData/HumanUpFibroblastO30MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/HumanUpFibroblastO30MappanTro2rheMac2 > ../DNaseRegionData/HumanUpFibroblastO30MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/HumanUpFibroblastO30MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/HumanUpFibroblastO30MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/HumanUpFibroblastO30MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/HumanUpFibroblastO30MapRegionSorted100bp

#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO30D282M652Filt ../DNasePeaks/CommonUpFibroblastLinesO30 ../DNaseRegionData/CommonUpFibroblastO30 0
#./liftOver ../DNaseRegionData/CommonUpFibroblastO30 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/CommonUpFibroblastO30panTro2 ../DNaseRegionData/CommonUpFibroblastO30Unmapped
#subtractBed -a ../DNaseRegionData/CommonUpFibroblastO30 -b ../DNaseRegionData/CommonUpFibroblastO30Unmapped > ../DNaseRegionData/CommonUpFibroblastO30MappanTro2
#./liftOver ../DNaseRegionData/CommonUpFibroblastO30 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/CommonUpFibroblastO30rheMac2 ../DNaseRegionData/CommonUpFibroblastO30UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/CommonUpFibroblastO30MappanTro2 -b ../DNaseRegionData/CommonUpFibroblastO30UnmappedrheMac2 > ../DNaseRegionData/CommonUpFibroblastO30MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/CommonUpFibroblastO30MappanTro2rheMac2 > ../DNaseRegionData/CommonUpFibroblastO30MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/CommonUpFibroblastO30MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/CommonUpFibroblastO30MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/CommonUpFibroblastO30MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/CommonUpFibroblastO30MapRegionSorted100bp

#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO76D282M652Filt ../DNasePeaks/HumanUpFibroblastLinesO76 ../DNaseRegionData/HumanUpFibroblastO76 0
#./liftOver ../DNaseRegionData/HumanUpFibroblastO76 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/HumanUpFibroblastO76panTro2 ../DNaseRegionData/HumanUpFibroblastO76Unmapped
#subtractBed -a ../DNaseRegionData/HumanUpFibroblastO76 -b ../DNaseRegionData/HumanUpFibroblastO76Unmapped > ../DNaseRegionData/HumanUpFibroblastO76MappanTro2
#./liftOver ../DNaseRegionData/HumanUpFibroblastO76 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/HumanUpFibroblastO76rheMac2 ../DNaseRegionData/HumanUpFibroblastO76UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/HumanUpFibroblastO76MappanTro2 -b ../DNaseRegionData/HumanUpFibroblastO76UnmappedrheMac2 > ../DNaseRegionData/HumanUpFibroblastO76MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/HumanUpFibroblastO76MappanTro2rheMac2 > ../DNaseRegionData/HumanUpFibroblastO76MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/HumanUpFibroblastO76MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/HumanUpFibroblastO76MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/HumanUpFibroblastO76MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/HumanUpFibroblastO76MapRegionSorted100bp

#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO76D282M652Filt ../DNasePeaks/CommonUpFibroblastLinesO76 ../DNaseRegionData/CommonUpFibroblastO76 0
#./liftOver ../DNaseRegionData/CommonUpFibroblastO76 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/CommonUpFibroblastO76panTro2 ../DNaseRegionData/CommonUpFibroblastO76Unmapped
#subtractBed -a ../DNaseRegionData/CommonUpFibroblastO76 -b ../DNaseRegionData/CommonUpFibroblastO76Unmapped > ../DNaseRegionData/CommonUpFibroblastO76MappanTro2
#./liftOver ../DNaseRegionData/CommonUpFibroblastO76 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/CommonUpFibroblastO76rheMac2 ../DNaseRegionData/CommonUpFibroblastO76UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/CommonUpFibroblastO76MappanTro2 -b ../DNaseRegionData/CommonUpFibroblastO76UnmappedrheMac2 > ../DNaseRegionData/CommonUpFibroblastO76MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/CommonUpFibroblastO76MappanTro2rheMac2 > ../DNaseRegionData/CommonUpFibroblastO76MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/CommonUpFibroblastO76MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/CommonUpFibroblastO76MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/CommonUpFibroblastO76MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/CommonUpFibroblastO76MapRegionSorted100bp

#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO152D282M652Filt ../DNasePeaks/HumanUpFibroblastLinesO152 ../DNaseRegionData/HumanUpFibroblastO152 0
#./liftOver ../DNaseRegionData/HumanUpFibroblastO152 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/HumanUpFibroblastO152panTro2 ../DNaseRegionData/HumanUpFibroblastO152Unmapped
#subtractBed -a ../DNaseRegionData/HumanUpFibroblastO152 -b ../DNaseRegionData/HumanUpFibroblastO152Unmapped > ../DNaseRegionData/HumanUpFibroblastO152MappanTro2
#./liftOver ../DNaseRegionData/HumanUpFibroblastO152 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/HumanUpFibroblastO152rheMac2 ../DNaseRegionData/HumanUpFibroblastO152UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/HumanUpFibroblastO152MappanTro2 -b ../DNaseRegionData/HumanUpFibroblastO152UnmappedrheMac2 > ../DNaseRegionData/HumanUpFibroblastO152MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/HumanUpFibroblastO152MappanTro2rheMac2 > ../DNaseRegionData/HumanUpFibroblastO152MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/HumanUpFibroblastO152MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/HumanUpFibroblastO152MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/HumanUpFibroblastO152MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/HumanUpFibroblastO152MapRegionSorted100bp

#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO152D282M652Filt ../DNasePeaks/CommonUpFibroblastLinesO152 ../DNaseRegionData/CommonUpFibroblastO152 0
#./liftOver ../DNaseRegionData/CommonUpFibroblastO152 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/CommonUpFibroblastO152panTro2 ../DNaseRegionData/CommonUpFibroblastO152Unmapped
#subtractBed -a ../DNaseRegionData/CommonUpFibroblastO152 -b ../DNaseRegionData/CommonUpFibroblastO152Unmapped > ../DNaseRegionData/CommonUpFibroblastO152MappanTro2
#./liftOver ../DNaseRegionData/CommonUpFibroblastO152 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/CommonUpFibroblastO152rheMac2 ../DNaseRegionData/CommonUpFibroblastO152UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/CommonUpFibroblastO152MappanTro2 -b ../DNaseRegionData/CommonUpFibroblastO152UnmappedrheMac2 > ../DNaseRegionData/CommonUpFibroblastO152MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/CommonUpFibroblastO152MappanTro2rheMac2 > ../DNaseRegionData/CommonUpFibroblastO152MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/CommonUpFibroblastO152MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/CommonUpFibroblastO152MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/CommonUpFibroblastO152MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/CommonUpFibroblastO152MapRegionSorted100bp

#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO282D282M652Filt ../DNasePeaks/HumanUpFibroblastLinesO282 ../DNaseRegionData/HumanUpFibroblastO282 0
#./liftOver ../DNaseRegionData/HumanUpFibroblastO282 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/HumanUpFibroblastO282panTro2 ../DNaseRegionData/HumanUpFibroblastO282Unmapped
#subtractBed -a ../DNaseRegionData/HumanUpFibroblastO282 -b ../DNaseRegionData/HumanUpFibroblastO282Unmapped > ../DNaseRegionData/HumanUpFibroblastO282MappanTro2
#./liftOver ../DNaseRegionData/HumanUpFibroblastO282 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/HumanUpFibroblastO282rheMac2 ../DNaseRegionData/HumanUpFibroblastO282UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/HumanUpFibroblastO282MappanTro2 -b ../DNaseRegionData/HumanUpFibroblastO282UnmappedrheMac2 > ../DNaseRegionData/HumanUpFibroblastO282MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/HumanUpFibroblastO282MappanTro2rheMac2 > ../DNaseRegionData/HumanUpFibroblastO282MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/HumanUpFibroblastO282MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/HumanUpFibroblastO282MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/HumanUpFibroblastO282MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/HumanUpFibroblastO282MapRegionSorted100bp

#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO282D282M652Filt ../DNasePeaks/CommonUpFibroblastLinesO282 ../DNaseRegionData/CommonUpFibroblastO282 0
#./liftOver ../DNaseRegionData/CommonUpFibroblastO282 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/CommonUpFibroblastO282panTro2 ../DNaseRegionData/CommonUpFibroblastO282Unmapped
#subtractBed -a ../DNaseRegionData/CommonUpFibroblastO282 -b ../DNaseRegionData/CommonUpFibroblastO282Unmapped > ../DNaseRegionData/CommonUpFibroblastO282MappanTro2
#./liftOver ../DNaseRegionData/CommonUpFibroblastO282 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/CommonUpFibroblastO282rheMac2 ../DNaseRegionData/CommonUpFibroblastO282UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/CommonUpFibroblastO282MappanTro2 -b ../DNaseRegionData/CommonUpFibroblastO282UnmappedrheMac2 > ../DNaseRegionData/CommonUpFibroblastO282MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/CommonUpFibroblastO282MappanTro2rheMac2 > ../DNaseRegionData/CommonUpFibroblastO282MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/CommonUpFibroblastO282MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/CommonUpFibroblastO282MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/CommonUpFibroblastO282MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/CommonUpFibroblastO282MapRegionSorted100bp


#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO30D282M652Filt ../DNasePeaks/CommonUpLFibroblastLinesO30 ../DNaseRegionData/CommonUpLFibroblastO30 0
#./liftOver ../DNaseRegionData/CommonUpLFibroblastO30 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/CommonUpLFibroblastO30panTro2 ../DNaseRegionData/CommonUpLFibroblastO30Unmapped
#subtractBed -a ../DNaseRegionData/CommonUpLFibroblastO30 -b ../DNaseRegionData/CommonUpLFibroblastO30Unmapped > ../DNaseRegionData/CommonUpLFibroblastO30MappanTro2
#./liftOver ../DNaseRegionData/CommonUpLFibroblastO30 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/CommonUpLFibroblastO30rheMac2 ../DNaseRegionData/CommonUpLFibroblastO30UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/CommonUpLFibroblastO30MappanTro2 -b ../DNaseRegionData/CommonUpLFibroblastO30UnmappedrheMac2 > ../DNaseRegionData/CommonUpLFibroblastO30MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/CommonUpLFibroblastO30MappanTro2rheMac2 > ../DNaseRegionData/CommonUpLFibroblastO30MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/CommonUpLFibroblastO30MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/CommonUpLFibroblastO30MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/CommonUpLFibroblastO30MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/CommonUpLFibroblastO30MapRegionSorted100bp

#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO76D282M652Filt ../DNasePeaks/CommonUpLFibroblastLinesO76 ../DNaseRegionData/CommonUpLFibroblastO76 0
#./liftOver ../DNaseRegionData/CommonUpLFibroblastO76 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/CommonUpLFibroblastO76panTro2 ../DNaseRegionData/CommonUpLFibroblastO76Unmapped
#subtractBed -a ../DNaseRegionData/CommonUpLFibroblastO76 -b ../DNaseRegionData/CommonUpLFibroblastO76Unmapped > ../DNaseRegionData/CommonUpLFibroblastO76MappanTro2
#./liftOver ../DNaseRegionData/CommonUpLFibroblastO76 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/CommonUpLFibroblastO76rheMac2 ../DNaseRegionData/CommonUpLFibroblastO76UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/CommonUpLFibroblastO76MappanTro2 -b ../DNaseRegionData/CommonUpLFibroblastO76UnmappedrheMac2 > ../DNaseRegionData/CommonUpLFibroblastO76MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/CommonUpLFibroblastO76MappanTro2rheMac2 > ../DNaseRegionData/CommonUpLFibroblastO76MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/CommonUpLFibroblastO76MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/CommonUpLFibroblastO76MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/CommonUpLFibroblastO76MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/CommonUpLFibroblastO76MapRegionSorted100bp

#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO152D282M652Filt ../DNasePeaks/CommonUpLFibroblastLinesO152 ../DNaseRegionData/CommonUpLFibroblastO152 0
#./liftOver ../DNaseRegionData/CommonUpLFibroblastO152 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/CommonUpLFibroblastO152panTro2 ../DNaseRegionData/CommonUpLFibroblastO152Unmapped
#subtractBed -a ../DNaseRegionData/CommonUpLFibroblastO152 -b ../DNaseRegionData/CommonUpLFibroblastO152Unmapped > ../DNaseRegionData/CommonUpLFibroblastO152MappanTro2
#./liftOver ../DNaseRegionData/CommonUpLFibroblastO152 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/CommonUpLFibroblastO152rheMac2 ../DNaseRegionData/CommonUpLFibroblastO152UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/CommonUpLFibroblastO152MappanTro2 -b ../DNaseRegionData/CommonUpLFibroblastO152UnmappedrheMac2 > ../DNaseRegionData/CommonUpLFibroblastO152MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/CommonUpLFibroblastO152MappanTro2rheMac2 > ../DNaseRegionData/CommonUpLFibroblastO152MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/CommonUpLFibroblastO152MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/CommonUpLFibroblastO152MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/CommonUpLFibroblastO152MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/CommonUpLFibroblastO152MapRegionSorted100bp

#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO282D282M652Filt ../DNasePeaks/CommonUpLFibroblastLinesO282 ../DNaseRegionData/CommonUpLFibroblastO282 0
#./liftOver ../DNaseRegionData/CommonUpLFibroblastO282 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/CommonUpLFibroblastO282panTro2 ../DNaseRegionData/CommonUpLFibroblastO282Unmapped
#subtractBed -a ../DNaseRegionData/CommonUpLFibroblastO282 -b ../DNaseRegionData/CommonUpLFibroblastO282Unmapped > ../DNaseRegionData/CommonUpLFibroblastO282MappanTro2
#./liftOver ../DNaseRegionData/CommonUpLFibroblastO282 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/CommonUpLFibroblastO282rheMac2 ../DNaseRegionData/CommonUpLFibroblastO282UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/CommonUpLFibroblastO282MappanTro2 -b ../DNaseRegionData/CommonUpLFibroblastO282UnmappedrheMac2 > ../DNaseRegionData/CommonUpLFibroblastO282MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/CommonUpLFibroblastO282MappanTro2rheMac2 > ../DNaseRegionData/CommonUpLFibroblastO282MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/CommonUpLFibroblastO282MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/CommonUpLFibroblastO282MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/CommonUpLFibroblastO282MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/CommonUpLFibroblastO282MapRegionSorted100bp


#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO15D282M652Filt ../DNasePeaks/HumanUpFibroblastLinesFDR001 ../DNaseRegionData/HumanUpFibroblastFDR001 0
#./liftOver ../DNaseRegionData/HumanUpFibroblastFDR001 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/HumanUpFibroblastFDR001panTro2 ../DNaseRegionData/HumanUpFibroblastFDR001Unmapped
#subtractBed -a ../DNaseRegionData/HumanUpFibroblastFDR001 -b ../DNaseRegionData/HumanUpFibroblastFDR001Unmapped > ../DNaseRegionData/HumanUpFibroblastFDR001MappanTro2
#./liftOver ../DNaseRegionData/HumanUpFibroblastFDR001 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/HumanUpFibroblastFDR001rheMac2 ../DNaseRegionData/HumanUpFibroblastFDR001UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/HumanUpFibroblastFDR001MappanTro2 -b ../DNaseRegionData/HumanUpFibroblastFDR001UnmappedrheMac2 > ../DNaseRegionData/HumanUpFibroblastFDR001MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/HumanUpFibroblastFDR001MappanTro2rheMac2 > ../DNaseRegionData/HumanUpFibroblastFDR001MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/HumanUpFibroblastFDR001MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/HumanUpFibroblastFDR001MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/HumanUpFibroblastFDR001MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/HumanUpFibroblastFDR001MapRegionSorted100bp

#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO15D282M652Filt ../DNasePeaks/CommonUpFibroblastLinesFDR001 ../DNaseRegionData/CommonUpFibroblastFDR001 0
#./liftOver ../DNaseRegionData/CommonUpFibroblastFDR001 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/CommonUpFibroblastFDR001panTro2 ../DNaseRegionData/CommonUpFibroblastFDR001Unmapped
#subtractBed -a ../DNaseRegionData/CommonUpFibroblastFDR001 -b ../DNaseRegionData/CommonUpFibroblastFDR001Unmapped > ../DNaseRegionData/CommonUpFibroblastFDR001MappanTro2
#./liftOver ../DNaseRegionData/CommonUpFibroblastFDR001 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/CommonUpFibroblastFDR001rheMac2 ../DNaseRegionData/CommonUpFibroblastFDR001UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/CommonUpFibroblastFDR001MappanTro2 -b ../DNaseRegionData/CommonUpFibroblastFDR001UnmappedrheMac2 > ../DNaseRegionData/CommonUpFibroblastFDR001MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/CommonUpFibroblastFDR001MappanTro2rheMac2 > ../DNaseRegionData/CommonUpFibroblastFDR001MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/CommonUpFibroblastFDR001MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/CommonUpFibroblastFDR001MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/CommonUpFibroblastFDR001MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/CommonUpFibroblastFDR001MapRegionSorted100bp

#python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO15D282M652Filt ../DNasePeaks/CommonUpLFibroblastLinesFDR001 ../DNaseRegionData/CommonUpLFibroblastFDR001 0
#./liftOver ../DNaseRegionData/CommonUpLFibroblastFDR001 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/CommonUpLFibroblastFDR001panTro2 ../DNaseRegionData/CommonUpLFibroblastFDR001Unmapped
#subtractBed -a ../DNaseRegionData/CommonUpLFibroblastFDR001 -b ../DNaseRegionData/CommonUpLFibroblastFDR001Unmapped > ../DNaseRegionData/CommonUpLFibroblastFDR001MappanTro2
#./liftOver ../DNaseRegionData/CommonUpLFibroblastFDR001 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/CommonUpLFibroblastFDR001rheMac2 ../DNaseRegionData/CommonUpLFibroblastFDR001UnmappedrheMac2
#subtractBed -a ../DNaseRegionData/CommonUpLFibroblastFDR001MappanTro2 -b ../DNaseRegionData/CommonUpLFibroblastFDR001UnmappedrheMac2 > ../DNaseRegionData/CommonUpLFibroblastFDR001MappanTro2rheMac2
#sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/CommonUpLFibroblastFDR001MappanTro2rheMac2 > ../DNaseRegionData/CommonUpLFibroblastFDR001MappanTro2rheMac2Sorted
#python getRegionsOfInterest.py ../DNaseRegionData/CommonUpLFibroblastFDR001MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/CommonUpLFibroblastFDR001MapRegionSorted100bp
#intersectBed -a ../DNaseRegionData/CommonUpLFibroblastFDR001MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
#wc temp
#wc ../DNaseRegionData/CommonUpLFibroblastFDR001MapRegionSorted100bp

python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO15D282M652Filt ../DNasePeaks/HumanUpFibroblastLinesFDR1 ../DNaseRegionData/HumanUpFibroblastFDR1 0
./liftOver ../DNaseRegionData/HumanUpFibroblastFDR1 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/HumanUpFibroblastFDR1panTro2 ../DNaseRegionData/HumanUpFibroblastFDR1Unmapped
subtractBed -a ../DNaseRegionData/HumanUpFibroblastFDR1 -b ../DNaseRegionData/HumanUpFibroblastFDR1Unmapped > ../DNaseRegionData/HumanUpFibroblastFDR1MappanTro2
./liftOver ../DNaseRegionData/HumanUpFibroblastFDR1 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/HumanUpFibroblastFDR1rheMac2 ../DNaseRegionData/HumanUpFibroblastFDR1UnmappedrheMac2
subtractBed -a ../DNaseRegionData/HumanUpFibroblastFDR1MappanTro2 -b ../DNaseRegionData/HumanUpFibroblastFDR1UnmappedrheMac2 > ../DNaseRegionData/HumanUpFibroblastFDR1MappanTro2rheMac2
sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/HumanUpFibroblastFDR1MappanTro2rheMac2 > ../DNaseRegionData/HumanUpFibroblastFDR1MappanTro2rheMac2Sorted
python getRegionsOfInterest.py ../DNaseRegionData/HumanUpFibroblastFDR1MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/HumanUpFibroblastFDR1MapRegionSorted100bp
intersectBed -a ../DNaseRegionData/HumanUpFibroblastFDR1MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
wc temp
wc ../DNaseRegionData/HumanUpFibroblastFDR1MapRegionSorted100bp

python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO15D282M652Filt ../DNasePeaks/CommonUpFibroblastLinesFDR1 ../DNaseRegionData/CommonUpFibroblastFDR1 0
./liftOver ../DNaseRegionData/CommonUpFibroblastFDR1 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/CommonUpFibroblastFDR1panTro2 ../DNaseRegionData/CommonUpFibroblastFDR1Unmapped
subtractBed -a ../DNaseRegionData/CommonUpFibroblastFDR1 -b ../DNaseRegionData/CommonUpFibroblastFDR1Unmapped > ../DNaseRegionData/CommonUpFibroblastFDR1MappanTro2
./liftOver ../DNaseRegionData/CommonUpFibroblastFDR1 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/CommonUpFibroblastFDR1rheMac2 ../DNaseRegionData/CommonUpFibroblastFDR1UnmappedrheMac2
subtractBed -a ../DNaseRegionData/CommonUpFibroblastFDR1MappanTro2 -b ../DNaseRegionData/CommonUpFibroblastFDR1UnmappedrheMac2 > ../DNaseRegionData/CommonUpFibroblastFDR1MappanTro2rheMac2
sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/CommonUpFibroblastFDR1MappanTro2rheMac2 > ../DNaseRegionData/CommonUpFibroblastFDR1MappanTro2rheMac2Sorted
python getRegionsOfInterest.py ../DNaseRegionData/CommonUpFibroblastFDR1MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/CommonUpFibroblastFDR1MapRegionSorted100bp
intersectBed -a ../DNaseRegionData/CommonUpFibroblastFDR1MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
wc temp
wc ../DNaseRegionData/CommonUpFibroblastFDR1MapRegionSorted100bp

python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO15D282M652Filt ../DNasePeaks/CommonUpLFibroblastLinesFDR1 ../DNaseRegionData/CommonUpLFibroblastFDR1 0
./liftOver ../DNaseRegionData/CommonUpLFibroblastFDR1 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/CommonUpLFibroblastFDR1panTro2 ../DNaseRegionData/CommonUpLFibroblastFDR1Unmapped
subtractBed -a ../DNaseRegionData/CommonUpLFibroblastFDR1 -b ../DNaseRegionData/CommonUpLFibroblastFDR1Unmapped > ../DNaseRegionData/CommonUpLFibroblastFDR1MappanTro2
./liftOver ../DNaseRegionData/CommonUpLFibroblastFDR1 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/CommonUpLFibroblastFDR1rheMac2 ../DNaseRegionData/CommonUpLFibroblastFDR1UnmappedrheMac2
subtractBed -a ../DNaseRegionData/CommonUpLFibroblastFDR1MappanTro2 -b ../DNaseRegionData/CommonUpLFibroblastFDR1UnmappedrheMac2 > ../DNaseRegionData/CommonUpLFibroblastFDR1MappanTro2rheMac2
sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/CommonUpLFibroblastFDR1MappanTro2rheMac2 > ../DNaseRegionData/CommonUpLFibroblastFDR1MappanTro2rheMac2Sorted
python getRegionsOfInterest.py ../DNaseRegionData/CommonUpLFibroblastFDR1MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/CommonUpLFibroblastFDR1MapRegionSorted100bp
intersectBed -a ../DNaseRegionData/CommonUpLFibroblastFDR1MapRegionSorted100bp -b ../ENCODEData/NHDF_Ad/wgEncodeBroadHistoneNhdfadCtcfStdPk.broadPeak > temp
wc temp
wc ../DNaseRegionData/CommonUpLFibroblastFDR1MapRegionSorted100bp
