#! /usr/bin/env python
import sys
import os


# Example input record:
# 01880 ADNV MLVN |||||||STEVEN||ADDONIVIO|||STEVE||||STVN|||M||8||MELVIN|ST||||Y|S|7|0

# Example output record:
# 01880 ADNV MLVN |ADDONIVIO


if len(sys.argv) != 2:
   print ("Must pass in one argument only - an input file")
   sys.exit(1)

def main():

  inFile = sys.argv[1]
  outFile= inFile + "_output"

  in_fh  = open(inFile ,'r')
  out_fh = open(outFile,'w')

  for line in in_fh:
#    values = line.split("|")

#    fullName = values[9]

#    outRec = values[0] + '|' + fullName + '\n'

    out_fh.write(line)


  in_fh.close()
  out_fh.close()

  sys.exit(0)

if __name__ == '__main__': main()





#p = re.compile(' ([A-Za-z]\{3}) ') 
#p = re.compile(' (\w+) ')
#




