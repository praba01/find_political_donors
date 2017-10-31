# find_political_donors

Scalability: I assign a UNIQUE RECORD ID to each valid record of input file. This will help us split the input file into multiple 
             files(of predetermined records) and process each one seperately. The input file could be split at the end of <CMPYID>,
             TRANS_DT and ZIP group and/or every 100,000(or whichever is larger) records for example.



Description: Here is how I process the input file to generate two output files:
  1) For every record in input file:  
    i) Read 5 fields
    ii) Validate as specified in the instructions
    iii) If valid, add a record_id(serial #) field and write to a file <input_file>_REVISED
    
  2) Read every record of <input_file>_REVISED sorted by CMPYID, zip and trn_date
    i) Check prev_record's zip and CMPY_ID
      a) if they match, find median, add transaction count and trans amount
      b) Write the record with record_id to a file called medianvals_by_zip.tmp
      c) If they don't match, median will be same as trans_amt;
      d) Write the record with record_id to the file medianvals_by_zip.tmp
   
    ii) Check prev record's cmpy_id and trns_date
      a) if they match, find median, add transaction count and trans amount
      b) If they don't match, write the record when cnt != 0 to a file called medianvals_by_date.tmp
    
    At the end, write last entry from (ii)
    
    3) Generate output file(medianvals_by_zip.txt) by sorting the file "medianvals_by_zip.tmp" on record_id to preserve the order of input file 
    4) Generate output file(medianvals_by_date.txt) by sorting the file "medianvals_by_date.tmp" on CMPYID and date 
