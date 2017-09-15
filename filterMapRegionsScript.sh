python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO15D282M652Filt ../DNasePeaks/HumanUpFibroblastLinesFDR05 ../DNaseRegionData/HumanUpFibroblastFDR05 0
./liftOver ../DNaseRegionData/HumanUpFibroblastFDR05 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/HumanUpFibroblastFDR05panTro2 ../DNaseRegionData/HumanUpFibroblastFDR05Unmapped
subtractBed -a ../DNaseRegionData/HumanUpFibroblastFDR05 -b ../DNaseRegionData/HumanUpFibroblastFDR05Unmapped > ../DNaseRegionData/HumanUpFibroblastFDR05MappanTro2
./liftOver ../DNaseRegionData/HumanUpFibroblastFDR05 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/HumanUpFibroblastFDR05rheMac2 ../DNaseRegionData/HumanUpFibroblastFDR05UnmappedrheMac2
subtractBed -a ../DNaseRegionData/HumanUpFibroblastFDR05MappanTro2 -b ../DNaseRegionData/HumanUpFibroblastFDR05UnmappedrheMac2 > ../DNaseRegionData/HumanUpFibroblastFDR05MappanTro2rheMac2
sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/HumanUpFibroblastFDR05MappanTro2rheMac2 > ../DNaseRegionData/HumanUpFibroblastFDR05MappanTro2rheMac2Sorted
python getRegionsOfInterest.py ../DNaseRegionData/HumanUpFibroblastFDR05MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/HumanUpFibroblastFDR05MapRegionSorted100bp

python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO15D282M652Filt ../DNasePeaks/HumanDownFibroblastLinesFDR05 ../DNaseRegionData/HumanDownFibroblastFDR05 0
./liftOver ../DNaseRegionData/HumanDownFibroblastFDR05 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/HumanDownFibroblastFDR05panTro2 ../DNaseRegionData/HumanDownFibroblastFDR05Unmapped
subtractBed -a ../DNaseRegionData/HumanDownFibroblastFDR05 -b ../DNaseRegionData/HumanDownFibroblastFDR05Unmapped > ../DNaseRegionData/HumanDownFibroblastFDR05MappanTro2
./liftOver ../DNaseRegionData/HumanDownFibroblastFDR05 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/HumanDownFibroblastFDR05rheMac2 ../DNaseRegionData/HumanDownFibroblastFDR05UnmappedrheMac2
subtractBed -a ../DNaseRegionData/HumanDownFibroblastFDR05MappanTro2 -b ../DNaseRegionData/HumanDownFibroblastFDR05UnmappedrheMac2 > ../DNaseRegionData/HumanDownFibroblastFDR05MappanTro2rheMac2
sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/HumanDownFibroblastFDR05MappanTro2rheMac2 > ../DNaseRegionData/HumanDownFibroblastFDR05MappanTro2rheMac2Sorted
python getRegionsOfInterest.py ../DNaseRegionData/HumanDownFibroblastFDR05MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/HumanDownFibroblastFDR05MapRegionSorted100bp

python filterPeakWindowsLineNums.py ../DNasePeaks/allPeaksWindowsO15D282M652Filt ../DNasePeaks/CommonFibroblastLinesFDR05 ../DNaseRegionData/CommonFibroblastFDR05 0
./liftOver ../DNaseRegionData/CommonFibroblastFDR05 ../LiftoverChains/hg19ToPanTro2.over.chain ../DNaseRegionData/CommonFibroblastFDR05panTro2 ../DNaseRegionData/CommonFibroblastFDR05Unmapped
subtractBed -a ../DNaseRegionData/CommonFibroblastFDR05 -b ../DNaseRegionData/CommonFibroblastFDR05Unmapped > ../DNaseRegionData/CommonFibroblastFDR05MappanTro2
./liftOver ../DNaseRegionData/CommonFibroblastFDR05 ../LiftoverChains/hg19ToRheMac2.over.chain ../DNaseRegionData/CommonFibroblastFDR05rheMac2 ../DNaseRegionData/CommonFibroblastFDR05UnmappedrheMac2
subtractBed -a ../DNaseRegionData/CommonFibroblastFDR05MappanTro2 -b ../DNaseRegionData/CommonFibroblastFDR05UnmappedrheMac2 > ../DNaseRegionData/CommonFibroblastFDR05MappanTro2rheMac2
sort -u -k1,1 -k2,2n -k3,3n ../DNaseRegionData/CommonFibroblastFDR05MappanTro2rheMac2 > ../DNaseRegionData/CommonFibroblastFDR05MappanTro2rheMac2Sorted
python getRegionsOfInterest.py ../DNaseRegionData/CommonFibroblastFDR05MappanTro2rheMac2Sorted 0 1 2 100 1 0 0 1 0 0 ../DNaseRegionData/CommonFibroblastFDR05MapRegionSorted100bp
