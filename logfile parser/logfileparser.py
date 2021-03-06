'''
http://www.reddit.com/r/learnprogramming/comments/1exsrt/interview_question_find_the_1_of_the_file/
Disclaimer: This is a interview question, that I pretty much messed up. So most probably, I am not getting hired :-( .
But I do not want to make the same mistake next time around, and be prepared. Also the problem is interesting, at least for me.
Question:
There is a large networking log file of around 1GB or more, which has ASCII text. On each line you have entries like source ip, destination ip, error report number, start time, end time. These entries are separated by one white space.
The difference between start and end time should be as less as possible. The longer it is, we assume there was delay in that request and it is a problem child.
Your task, is to find out, the top 1% culprit requests that have the longest time, and display them or send them to a file. You can find the longest time by subtracting the start from end time. For purposes of convenience, let us not be concerned about the 24 hour time format, for the time being. That is request start at 23.59.00 and ends at 00.05.00
My attempt:
The file is large, so I cannot buffer the file (I am guessing here, I have never tried). So I will have to read the file and do the the output file simultaneously, and keeping a lock on the log file.
I know what the file size is roughly around 1GB for this problem or could be more (does not matter much, it is a large file). Now I know how much is 1% of 1GB that would be 1MB, and each line could have around 16 bytes of information.
So, now I make a max heap data structure, where the comparator is based on the difference between end time and start time. The number of nodes in my heap data structure would be around 1MB / 16B. Which is the information per node, that divides the actual size of the heap.
Now iterate over the log file line by line and keep inserting into the heap data structure. By end of the file iteration, you should have heap with most time consuming requests that form around 1% of the log file or rather 1% delaying requests. With the heap data, the root and the parents, I know when I iterate and print it to a file, I will have the longest delay request at the top and the others in descending orders.
I think, this can be done in python, but the interviewer did not ask me to write the code for this one. Maybe he was horrified with my approach.'''

import re
import sys
import math
import heapq
import datetime

def ParseLogFile(filename, linecount):
  minheap = []
  maxKeptLines = max(math.ceil(linecount / 100), 1)
  with open(filename, 'r') as file:
    for line in file:
      times = re.findall('\s(\d\d):(\d\d):(\d\d)', line)
      #minheap format ( dif, string of entire line ), heap sorts by dif
      if len(times) == 2:
        dif = FindTimeDifInSeconds(times)
        addIfHighestWithMaxLineCap(minheap, dif, line, maxKeptLines)
    
  return minheap

def FindTimeDifInSeconds(times):
  startseconds = (int)(times[0][0])*60*60 + (int)(times[0][1])*60 + (int)(times[0][2])
  endseconds = (int)(times[1][0])*60*60 + (int)(times[1][1])*60 + (int)(times[1][2])
  dif = math.fabs(endseconds - startseconds) #fabs just so I could use more random time data.
  #real solution would need to have dates in the log file to find elapsed time for entries that spanned multiple days
  return dif
  
def addIfHighestWithMaxLineCap(minheap, dif, line, maxKeptLines):
  if len(minheap) < maxKeptLines:
    heapq.heappush(minheap, (dif, line))
  else: # more than max lines to keep, have to take away a record to add one
      heapq.heappushpop(minheap, (dif, line)) #push item to heap, then remove the smallest item from the heap
  return

def countLines(filename):
  count = 0
  with open(filename, 'r') as file:
    for line in file:
      count += 1
  print ('Found %d lines in %s' %(count, filename))
  return count
  
def main():
  if(len(sys.argv) != 2):
    print ('usage logfileparser.py filename.txt')
    sys.exit(-1)
    
  filename = sys.argv[1]
  
  print 'Started line count:', datetime.datetime.now()
  linecount = countLines(filename)
  print 'Ended line count:', datetime.datetime.now()
  
  print 'Started Parse:', datetime.datetime.now()
  worsttimesminheap = ParseLogFile(filename, linecount)
  print 'Ended Parse:', datetime.datetime.now()
  print ('Length of result minheap: %d' % (len(worsttimesminheap)))
  
  outfilename = re.findall('(.+)\.', filename)[0] + 'WorstCases.txt'

  with open(outfilename, 'w') as outfile:
    for element in sorted(worsttimesminheap, reverse = True):
      # print (element[0], element[1])
      outfile.write('%s seconds\t%s' % (element[0], element[1]))

if __name__ == '__main__':
  main()
