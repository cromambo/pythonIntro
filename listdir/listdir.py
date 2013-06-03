import os
import subprocess
import sys

def printdir(dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    print filename
    print os.path.join(dir, filename)
    print os.path.abspath(os.path.join(dir, filename))

def listdir(dir):
  cmd = 'dir ' + dir
  print 'command to run: ', cmd

  (output, errors) = subprocess.Popen(
                    cmd, 
                    shell=True, 
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE).communicate()
  
  if errors:
    sys.stderr.write('errors: ', errors)
    sys.exit(1)
  print output
  

def main():
  print ('hello world')
 

  dir = os.getcwd()
  contents = os.listdir(os.getcwd())
  # print os.path.join(dir, contents[0])
  
  path = (dir+'\\genned')
  # print path
  if os.path.exists(path) != True:
    os.mkdir(dir+'\\genned')
    
  # printdir(os.getcwd())
  listdir(dir)
  
if __name__ == '__main__':
  main()
