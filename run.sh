#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
if [[ -f ./output/medianvals_by_zip.txt ]]
then
     rm ./output/medianvals_by_zip.txt 
fi

if [[ -f ./output/medianvals_by_date.txt ]]
then
     rm ./output/medianvals_by_date.txt
fi
if [[ -f ./output/medianvals_by_zip.tmp ]]
then
     rm ./output/medianvals_by_zip.tmp
fi

if [[ -f ./output/medianvals_by_date.tmp ]]
then
     rm ./output/medianvals_by_date.tmp
fi

if [[ -f ./output/medianvals_zip ]]
then
     rm ./output/medianvals_zip
fi

if [[ -f ./output/medianvals_date ]]
then
     rm ./output/medianvals_date
fi
touch ./output/medianvals_by_zip.txt
touch ./output/medianvals_by_date.txt
touch ./output/medianvals_by_zip.tmp
touch ./output/medianvals_by_date.tmp
touch ./output/medianvals_zip
touch ./output/medianvals_date

python ./src/find_political_donors.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt

if [[ -f ./output/medianvals_by_zip.tmp ]]
then
     rm ./output/medianvals_by_zip.tmp
fi

if [[ -f ./output/medianvals_by_date.tmp ]]
then
     rm ./output/medianvals_by_date.tmp
fi

if [[ -f ./output/medianvals_zip ]]
then
     rm ./output/medianvals_zip
fi

if [[ -f ./output/medianvals_date ]]
then
     rm ./output/medianvals_date
fi
