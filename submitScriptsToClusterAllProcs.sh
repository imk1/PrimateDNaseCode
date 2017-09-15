#!/bin/sh

Filename='/science/irene/PrimateSNPProject/src/runbaySeq.sh'
Ouptprefix='/science/irene/PrimateSNPProject/src/runbaySeq'
Name='runbaySeq'
Count=0

while read line;
do
	((Count=Count+1));
	Outfilename=$Ouptprefix$Count".sh";
	echo -e "$line" > $Outfilename;
	command1="qsub -l procs=8 -l mem=2G -w e -N $Name$Count -V -o ";
	command2="$Ouptprefix$Count.o -e ";
	command3="$Ouptprefix$Count.e ";
	command4=$Outfilename;
	$command1$command2$command3$command4;
done < $Filename
