import sys
import re

def Find(pat, text):
  match = re.search(pat, text)
  if match: print (match.group())
  else: print ('not found')
  return match

def main():
  text = 'sam@gmail.com, bob@hotmail.com, joe@Gmail.com, grank@gmail.com'
  pat = '([\w.]+)@([\w.]+)'
  m = Find(pat, text)
  # print (m.group(1), m.group(2))
  list = re.findall(pat, text, re.IGNORECASE)
  print ('len', len(list))
  for ele in list: print (ele)
  providerdict = {}
  providerdict = countIntoDict(list, providerdict)
  print(providerdict.items())
  return

 #tuple format (emailname, provider)
 #use provider as key, count as value
def countIntoDict(tupleList, dict):
  for tuple in tupleList:
    if tuple[1] in dict:
      dict[tuple[1]] += 1
    else:
      dict[tuple[1]] = 1
  return dict
  
if __name__ == '__main__':
  main()