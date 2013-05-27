
import random
from random import randint
import sys

def main():
  if len(sys.argv) != 3:
    print ('usage logfilegen.py outputfilename.txt 5000 #number of lines in output file')
    sys.exit(-1)
  
  outputfilename = sys.argv[1]
  elements = int(sys.argv[2])
  
  random.seed()
  with open(outputfilename, 'w') as outfile:
    while elements > 0:
      outfile.write('ip, ip, no:%(number)d ' % {'number':randint(0, 1000000)}),
      outfile.write ('%(hour)02d:%(min)02d:%(sec)02d' % {'hour':randint(0,23), 'min':randint(0,59), 'sec':randint(0,59)}), 
      outfile.write (' %(hour)02d:%(min)02d:%(sec)02d\n' % {'hour':randint(0,23), 'min':randint(0,59), 'sec':randint(0,59)}),
      elements -= 1

if __name__ == '__main__':
  main()