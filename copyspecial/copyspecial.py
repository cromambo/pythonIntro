#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]


  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
    
  dir = args[0]
  
  special = get_special_paths(dir)
  print special
  
  SpecialFilesFullPaths = [os.path.join(dir, file) for file in special]
  print SpecialFilesFullPaths
  
  if len(todir) != 0:
    createdir(todir)
    copytodir(SpecialFilesFullPaths, todir)
  
  if len(tozip) != 0:
    createdir(tozip)
    zipfilesIntoDir(SpecialFilesFullPaths, tozip, 'Specials.zip')

def zipfilesIntoDir(FileListFullPaths, TargetDir, ZipName):
  print 'zipping...'
  args = ['7za', 'a', ZipName]+FileListFullPaths
  print args
  subprocess.Popen(args)
  print 'zipped'
  
def copytodir(FilePathList, TargetDir):
  for file in FilePathList:
    shutil.copy(file, TargetDir)
  
def createdir(todir):  
  if len(todir) != 0:
    if os.path.exists(todir) == False:
      os.mkdir(todir)

def get_special_paths(dir):
  listdir = os.listdir(dir)
  special = [file for file in listdir if re.search('__\w+__', file)]
  return special 
  
if __name__ == "__main__":
  main()
