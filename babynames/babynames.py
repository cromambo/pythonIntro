#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  file = open(filename)
  contents = file.read()
  file.close()
  
  year = re.findall('Popularity in (\d\d\d\d)', contents)[0]
  ranknamename = re.findall('(\d+)[<>/td\s]+([\w]+)[<>/td\s]+(\w+)</td>', contents)
  rankdict = {}
  for ranktuple in ranknamename:
    rankdict[ranktuple[1]] = ranktuple[0]
    rankdict[ranktuple[2]] = ranktuple[0]
  
  retlist = []
  retlist.append(year)
  for key in sorted(rankdict.keys()):
    retlist.append('%s %s' %(key, rankdict[key]))  
  return retlist

def printRankListToFile(ranklist, filename):
  outfile = open(filename, 'w')
  for element in ranklist:
    outfile.write('%s\n' %(element))
  outfile.close()
  return
  
def printRankList(ranklist):
  for element in ranklist:
    print (element)
  return

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  filelist = []
  for dircontents in os.listdir():
    match = re.search('baby\d\d\d\d.html', dircontents)
    if match: filelist.append(match.group())
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  for filename in filelist:
    ranklist = extract_names(filename)
    if summary:
      print ('printing to file', filename + '.summary')
      printRankListToFile(ranklist, filename + '.summary')
    else:
      printRankList(ranklist)
  
  
if __name__ == '__main__':
  main()
