#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
rm ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt ./output/medianvals_by_zip.tmp ./output/medianvals_by_date.tmp
rm ./output/medianvals_zip ./output/medianvals_date
rm ./output/
touch ./output/medianvals_by_zip.txt
touch ./output/medianvals_by_date.txt
touch ./output/medianvals_by_zip.tmp
touch ./output/medianvals_by_date.tmp
touch ./output/medianvals_zip
touch ./output/medianvals_date




python ./src/find_political_donors.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt
