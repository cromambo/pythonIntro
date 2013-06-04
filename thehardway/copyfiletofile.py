import sys

def copyfiletofile(src, dest):
  with open(src) as input:
    with open(dest, 'w') as output:
      output.write(input.read())
      input.seek(0)
      print (input.read())


def main():
  if not len(sys.argv) == 3:
    print ('usage: copyfiletofile src.txt dest.txt')
    sys.exit(-1)
  
  src_file = sys.argv[1]
  dest_file = sys.argv[2]
  print (src_file)
  print (dest_file)
  copyfiletofile(src_file, dest_file)
  
if __name__ == '__main__':
  main()