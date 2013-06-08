def main():
  #create a mapping of states to abbreviations
  states = {
    'Oregon': 'OR',
    'Florida' : 'FLA',
    'California' : 'CA',
    'New York': 'NY',
    'Michigan': 'MI'    
  }
  
  #create a basic set of states and some cities in them
  cities = {
    'CA': 'San Francisco', 
    'MI': 'Detroit',
    'FLA': 'Jacksonville'
  }
  
  #add some more cities
  cities['OR'] = 'Portland'
  cities['NY'] = 'New York City'
  
  #print out some cities
  print ('-' * 10)
  print ('NY State has:', cities['NY'])
  print ('OR State has:', cities['OR'])
  
  #print some states
  print ('*' * 10)
  print ('Michigan\'s abbreviation is: ', states['Michigan'])
  print ('Florida\'s abbreviation is: ', states['Florida'])
  
  #do it by using the two dicts together
  print ('@' * 10)
  print ('Oregon has', cities[states['Oregon']])
  
  #print every state abbreviations
  print ('^' * 8)
  for key_state, value_abbr in states.items():
    print ('%s\'s abbreviation is %s' % (key_state, value_abbr))
    
  #print every city in every state
  print('!'*12)
  for city in cities.values():
    print (city)
  
  #now do every state name with its abbres and all its cities
  print ('-' * 8)
  for state, abbrev in states.items():
    print ('%(state)s is abbreviated %(abbrev)s and has city %(city)s' % {'state':state, 'abbrev':abbrev, 'city':cities[abbrev]} )
  
  #get abbrev from state taht might not be there
  state = states.get('Texas', 'key not found')
  if not state:
    print ('not found')
  else:
    print (state)
if __name__ == '__main__':
  main()