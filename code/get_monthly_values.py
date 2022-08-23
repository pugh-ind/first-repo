#! /usr/bin/python

import sys
import re

import datetime
import time

from csv import DictReader

#
#  Input file format, for records I care about...
#
# {'Account Name/Number': '231355253',           *
#  'Symbol': 'FBNDX',                            *
#  'Description': 'FIDELITY INVESTMENT GRADE',   *
#  'Quantity': '18791.846',                      *
#  'Last Price': '$8.42',                        *
#  'Last Price Change': '+$0.02',             
#  'Current Value': '$158227.34',                *
#  "Today's Gain/Loss Dollar": '+$375.83',
#  "Today's Gain/Loss Percent": '+0.24%',
#  'Total Gain/Loss Dollar': '-$1252.66',
#  'Total Gain/Loss Percent': '-0.79%',
#  'Cost Basis Per Share': '$8.49',
#  'Cost Basis Total': '$159480.00', 'Type': 'Cash'
# }
#
#   The starred ones are the ones I need...
#


if len(sys.argv) != 2:
   print ("can't open input file")
   sys.exit(1)

   
st = datetime.datetime.fromtimestamp(time.time()).strftime('%b-%d-%Y')
print(st)

def main():

   in_fh  = sys.argv[1]
   parts=in_fh.split('-')

   out_fh = open(parts[0]+'.tmp','w')
#  sql_fh = open(parts[0]+'.sql','w')

   lineCnt = 0

   for row in DictReader(open(in_fh,'r'),delimiter=','):

      if (row['Account Name/Number'].isnumeric()):

         print(row['Account Name/Number']+'\t'+row['Symbol']+'\t'+row['Description']+'\t'+row['Quantity']+'\t'+row['Last Price']+'\t'+row['Current Value'])
     
         out_fh.write("'"+row['Account Name/Number']+ "','"+ row['Symbol']+ "','"+row['Description'] +"',"+row['Quantity'] +','
                      +row['Last Price'] +','+ row['Current Value']+'\n')

#        sql_fh.write("insert "+'\n')

         lineCnt = lineCnt+1


   print("\nrecords used  "+str(lineCnt))
   sys.exit(0)

if __name__ == "__main__": main()

