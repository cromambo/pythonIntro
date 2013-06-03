#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  print (filename)
  with open(filename) as file:
    filecontents = file.read()
    urls = set(re.findall('GET (\S*puzzle\S*)', filecontents))
    underscore_index = filename.index('_')
    host = filename[underscore_index + 1:]
    return ['http://'+host+path for path in sorted(urls)]
  return []
  
def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  create_directory(dest_dir)
  
  index_file = open(dest_dir + '\index.html', 'w')
  
  index_file.write('<verbatim><html><body>')
  count = 0
  for url in img_urls:
    print 'Retrieving:', url
    destination_path = dest_dir + '\img' + str(count)+'.jpg'
    index_file.write('<img src=%s>' % destination_path)
    print 'Target:', destination_path
    try:
      urllib.urlretrieve(url, destination_path)
    except:
      print ('URL opening failed')
    count += 1
  index_file.write('</html></body>')
  index_file.close()
  
def create_directory(dir):
  # os.makedirs(dir, exist_ok=True) #python 3.2+only
  if len(dir) != 0:
    if not os.path.exists(dir):
      print ('Creating', dir)
      os.makedirs(dir)
  pass

def main():
  args = sys.argv[1:]

  if not args:
    print ('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
    pass
  else:
    print ('\n'.join(img_urls))

if __name__ == '__main__':
  main()
