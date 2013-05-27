
import random
from random import randint

def main():
  random.seed()
  with open('giantlog.txt', 'w') as outfile:
    elements = 1000000
    while elements > 0:
      outfile.write('ip, ip, no:%(number)d ' % {'number':randint(0, 1000000)}),
      outfile.write ('%(hour)02d:%(min)02d:%(sec)02d' % {'hour':randint(0,23), 'min':randint(0,59), 'sec':randint(0,59)}), 
      outfile.write (' %(hour)02d:%(min)02d:%(sec)02d\n' % {'hour':randint(0,24), 'min':randint(0,59), 'sec':randint(0,59)}),
      elements -= 1

if __name__ == '__main__':
  main()