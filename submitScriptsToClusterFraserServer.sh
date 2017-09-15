#!/bin/sh

Filename='/science/irene/PrimateSNPProject/src/runFIMOCommonFibroblastpanTro3100kb.sh'
Ouptprefix='/science/irene/PrimateSNPProject/src/runFIMOCommonFibroblastpanTro3100kb'
Name='runFIMOCommonFibroblastpanTro3100kb'
Count=0

while read line;
do
	((Count=Count+1));
	Outfilename=$Ouptprefix$Count".sh";
	echo -e "$line" > $Outfilename;
	command1="qsub -l nodes=1 -l mem=6G -w e -N $Name$Count -V -o ";
	command2="$Ouptprefix$Count.o -e ";
	command3="$Ouptprefix$Count.e ";
	command4=$Outfilename;
	$command1$command2$command3$command4;
	sleep .2;
done < $Filename
