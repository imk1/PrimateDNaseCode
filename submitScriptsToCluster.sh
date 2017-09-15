#!/bin/sh

Filename='/afs/cs.stanford.edu/u/imk1/scr/PrimateSNPProject/src/runFIMOCommonUpFibroblast.sh'
Ouptprefix='/afs/cs.stanford.edu/u/imk1/scr/PrimateSNPProject/src/runFIMOCommonUpFibroblast'
Name='runFIMOCommonUpFibroblast'
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
done < $Filename
