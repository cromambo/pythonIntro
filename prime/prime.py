
def main():
  for test in range(2,1000):
    for divisor in range(2, test):
      if test%divisor == 0:
        # print 'divisor %d goes into %d' %( divisor, test)
        break
    else: #for else, runs when loop finishes list, but not after break is called in the for
      print test, 'is prime'
      

if __name__ == '__main__':
  main()