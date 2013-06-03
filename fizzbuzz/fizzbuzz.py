
def fizzbuzz(testval, fizzval, buzzval):
  # if testval % (fizzval*buzzval) == 0:
    # return 'fizzbuzz' #this way is some extra duplication, if i decide to change 'fizz' to 'blah' i have to change 2 strings
    
  if fizzval == 0 or buzzval == 0:
    return 'error' #-1 #'Error: fizz and buzz values cannot be 0'

  retstr = ''
  if testval % fizzval == 0:
    retstr += 'fizz'
  if testval % buzzval == 0:
    retstr += 'buzz'
  if testval % fizzval != 0 and testval % buzzval != 0:
    retstr = testval
  return retstr


  
def main():
  for num in xrange(1,21):
    print fizzbuzz(num, 3, 5)

if __name__ == '__main__':
  main()
