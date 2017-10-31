#!/usr/bin/python
import sys
import subprocess
import datetime

### Declare global variables
#################################
def global_dec():
        global  recD ,       prev_zip , prev_date , prev_med
        global  prev_medD ,  tot_amt ,  tot_amtD ,  tot_trn
        global  tot_trnD ,   cnt ,      curr_list
        global  curr_listD , amtD ,     cntD , amt
        global NUMBER_OF_RECORDS , file_name, file_nameW, fileout1, fileout2
        global filetmp1, filetmp2, file_zip, file_dat
        NUMBER_OF_RECORDS = 0
        recD=" "
        prev_zip=" "
        prev_date=" "
        prev_med=0
        prev_medD=0
        tot_amt  = 0
        tot_amtD  = 0
        tot_trn  = 0
        tot_trnD  = 0
        cnt = 0
        cntD = 0
        curr_list=[]
        curr_listD=[]
        amt = 0
        amtD = 0
        sorted_curr_list=[]
 
### Initialize function

def initialize():
        global file_name, file_nameW, file_zip, file_dat
        global file_name_out1, file_name_out2
        global file_name_tmp1, file_name_tmp2
        global_dec()
        NUMBER_OF_RECORDS=10000
        file_name=sys.argv[1]
        file_nameW="data_REV"
        file_name_tmp1="./output/medianvals_by_zip.tmp"
        file_name_tmp2="./output/medianvals_by_date.tmp"
        file_name_out1=sys.argv[2]
        file_name_out2=sys.argv[3]
        file_zip="./output/medianvals_zip"
        file_dat="./output/medianvals_date"
 

###  Calculate median

def calculate_median(curr_list):
        n = len(curr_list)
        index = (n -1) // 2
        if (n % 2):
                return curr_list[index]
        else:
                med = (int(curr_list[index]) + int(curr_list[index +1])) // 2
                if (int(curr_list[index]) + int(curr_list[index +1]))% 2:
                        return med+1
                else:
                        return med
 
###  Process by ZIP

def process_by_zip(lineID):
    global  prev_zip, prev_CMTYID, curr_list, tot_trn, tot_amt, cnt,filetmp1
    if(lineID[2] == prev_zip and lineID[1] == prev_CMTYID):
        curr_list.append(lineID[3])
  	curr_list.sort(key=int)
        prev_med  = calculate_median(curr_list)
        tot_trn += 1
        amt = lineID[3]
        tot_amt = int(tot_amt)+int(amt)
        cnt += 1
        rec = lineID[0]+'|'+lineID[1]+'|'+lineID[2]+'|'+str(prev_med)+'|'+str(tot_trn)+'|'+str(tot_amt)+"\n"
        filetmp1.write(rec)
    else:
        cnt = 0
        curr_list=[]
        prev_med = lineID[3]
        tot_amt  = lineID[3]
        tot_trn  = 1
        prev_zip = lineID[2]
        prev_CMTYID = lineID[1]
        curr_list.append(lineID[3])
        rec = lineID[0]+'|'+lineID[1]+'|'+lineID[2]+'|'+str(prev_med)+'|'+str(tot_trn)+'|'+str(tot_amt)+"\n"
        filetmp1.write(rec)


def process_by_date(lineID):
    global  prev_date, prev_CMTYIDD, curr_listD, tot_trnD, tot_amtD, cntD, prev_medD,recD, filetmp2
    if(lineID[2] == prev_date and lineID[1] == prev_CMTYIDD):
        curr_listD.append(lineID[3])
  	curr_listD.sort(key=int)
        prev_medD  = calculate_median(curr_listD)
        tot_trnD += 1
        amtD = lineID[3]
        tot_amtD = int(tot_amtD)+int(amtD)
        cntD += 1
        recD = lineID[0]+'|'+lineID[1]+'|'+lineID[2]+'|'+str(prev_medD)+'|'+str(tot_trnD)+'|'+str(tot_amtD)+"\n"
    else:
        if(cntD != 0):
                filetmp2.write(recD)
        cntD = 1
        curr_listD=[]
        prev_medD = lineID[3]
        tot_amtD  = lineID[3]
        tot_trnD  = 1
        prev_date = lineID[2]
        prev_CMTYIDD = lineID[1]
        curr_listD.append(lineID[3])
        recD = lineID[0]+'|'+lineID[1]+'|'+lineID[2]+'|'+str(prev_medD)+'|'+str(tot_trnD)+'|'+str(tot_amtD)+"\n"
 
def valid_record(id,zip,dt,amt,other):
	try:
		datetime.datetime.strptime(dt, '%m%d%Y')
		valid_dt=1
	except ValueError:
		valid_dt=0

    	if( len(other) > 0 or len(zip) < 5 or len(id) == 0 or len(amt) == 0 or valid_dt == 0):
       		return 1
    	else:
       		return 0

initialize()
try:
  # open file stream
  file_zip_ = open(file_zip, "r+")
except IOError:
  print "1 There was an error writing to", file_zip
  sys.exit()

try:
  # open file stream
  file_dat_ = open(file_dat, "r+")
except IOError:
  print "2 There was an error writing to", file_dat
  sys.exit()

try:
  # open file stream
  file = open(file_name, "r")
except IOError:
  print "3 There was an error writing to", file_name
  sys.exit()

try:
  fileW = open(file_nameW, "r+")
except IOError:
  print "4 There was an error writing to", file_nameW
  sys.exit()

try:
  filetmp1 = open(file_name_tmp1, "r+")
except IOError:
  print "5 There was an error writing to", file_name_tmp1
  sys.exit()

try:
  filetmp2 = open(file_name_tmp2, "r+")
except IOError:
  print "6 There was an error writing to", file_name_tmp2
  sys.exit()

try:
  fileout1 = open(file_name_out1, "r+")
except IOError:
  print "7 There was an error writing to", file_name_out1
  sys.exit()

try:
  fileout2 = open(file_name_out2, "r+")
except IOError:
  print "8 There was an error writing to", file_name_out2
  sys.exit()

rowid = 0

### For each line in input file:
###  Grab only fields needed: 0, 10,13,14 and 15
###  Check if it is a valid record, add a field called rowid 
###  The rowid will be used to retain the position of the record in the file. 
###  Writes each valid record from the input file to output file

for line in file:
    lineID = line.split("|")
    CMTYID= lineID[0]
    ZIP= lineID[10]
    ZIP5=ZIP[0:5]
    trnDT= lineID[13]
    trnAMT= lineID[14]
    OTHER= lineID[15]
    if(valid_record(CMTYID,ZIP5,trnDT,trnAMT,OTHER) == 0):
        rowid += 1
        #rev_record = str(rowid)+"|"+CMTYID+"|"+ZIP5+"|"+trnDT+"|"+trnAMT+"\n"
        zip_record = str(rowid)+"|"+CMTYID+"|"+ZIP5+"|"+trnAMT+"\n"
        dat_record = str(rowid)+"|"+CMTYID+"|"+trnDT+"|"+trnAMT+"\n"
        file_zip_.write(zip_record)
        file_dat_.write(dat_record)

file.close()
file_zip_.close()
file_dat_.close()

### Sort the file in CMPYID, date and zip. This is required to process all records with the same CMPYID, date and ZIP together
proc = subprocess.Popen(['sort','-t|','-s', '-k 2,3',file_zip], stdout=subprocess.PIPE)

for line in proc.stdout:
    lineID2 = line.rstrip()
    lineID = lineID2.split("|")
    process_by_zip(lineID)


proc = subprocess.Popen(['sort','-t|','-s', '-k 2,3',file_dat], stdout=subprocess.PIPE)

for line in proc.stdout:
    lineID2 = line.rstrip()
    lineID = lineID2.split("|")
    process_by_date(lineID)
filetmp2.write(recD)

fileW.close()

proc.kill
filetmp1.close()
filetmp2.close()
try:
  filetmp1 = open(file_name_tmp1, "r")
except IOError:
  print "9 There was an error writing to", file_name_tmp1
  sys.exit()

try:
  filetmp2 = open(file_name_tmp2, "r")
except IOError:
  print " 10 There was an error writing to", file_name_tmp2
  sys.exit()


srt1 = subprocess.Popen(['sort','-t|','-g', '-k 1', "./output/medianvals_by_zip.tmp"], stdout=subprocess.PIPE)
for line in srt1.stdout:
        unsrt2=line.rstrip()
        lineID = unsrt2.split("|")
        rec=lineID[1]+'|'+lineID[2]+'|'+lineID[3]+'|'+lineID[4]+'|'+lineID[5]+"\n"
        fileout1.write(rec)

srt1 = subprocess.Popen(['sort','-g', '-t|','-s', '-k 2,3' ,"./output/medianvals_by_date.tmp"], stdout=subprocess.PIPE)
for line in srt1.stdout:
        unsrt2=line.rstrip()
        lineID = unsrt2.split("|")
        rec=lineID[1]+'|'+lineID[2]+'|'+lineID[3]+'|'+lineID[4]+'|'+lineID[5]+"\n"
        fileout2.write(rec)
