from sys import argv

def exercise14():
  script, user_name = argv
  prompt = '> '
  
  print ('Hi %s, I\'m the %s script' % (user_name, script))
  print ('I\'d like to ask you a few questions')
  print ('Do you like me %s?' % user_name)
  likes = raw_input(prompt)
  
  print ('Alright so you said %s about liking me' % likes)

def exercise15():
  with open(argv[1]) as file:
    print file.read() #this puts the file read to the end so the next part prints nothing
    for line in file:
      print (line),
    pass
    
def main():
  exercise15()

if __name__ == '__main__':
  main()