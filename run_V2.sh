#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#

del()
{
	if [[ -f $1 ]]
 	then
		rm $1
	fi
}


for file_name in ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt ./output/medianvals_by_zip.tmp ./output/medianvals_by_date.tmp ./output/medianvals_zip ./output/medianvals_date
do
     del ${file_name}
     touch ${file_name}
done

python ./src/find_political_donors.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt


for filename in ./output/medianvals_by_zip.tmp ./output/medianvals_by_date.tmp ./output/medianvals_zip ./output/medianvals_date
do
     del ${filename}
done
