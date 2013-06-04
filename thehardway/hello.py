
def exercise7():
  print 'Mary had a little lamb'
  print 'its fleece was white as %s' % 'snow'
  print 'and everywhere that mary went.'
  print '*' * 10
  
  end1 = 'c'
  end2 = 'h'
  end3 = 'e'
  end4 = 'e'
  end5 = 's'
  end6 = 'e'
  end7 = 'B'
  end8 = 'u'
  end9 = 'r'
  end10= 'g'
  end11= 'e'
  end12= 'r'
  
  print end1 + end2 + end3 + end4 + end5 + end6,
  print end7 + end8 + end9 + end10 + end11 + end12

def exercise8():
  formatter = '%r%r%r%r'
  print formatter % (1, 2, 3, 4)
  print formatter % ('one', 'two', 'three', 'four')
  print formatter % (True, False, False, True)
  print formatter % (formatter, formatter, formatter, formatter)
  print formatter % (
    "I had this thing.",
    "That you could type up right",
    "But it didn't sing.", 
    "So I said goodnight"
  )

def exercise9():
  #heres some new stuff
  days = 'Mon Tue Wed Thur Fri Sat Sun'
  months = 'Jan\nFeb\nMar\nApr\nMay\nJune\nJuly\nAug'
  
  print 'here are the days:', days
  print 'here are the months:', months
  
  print '''
  theres something going on here.
  with the three quotes
  we'll be able to type as much as we like.
  Even 5 lines if we want, or 5 or 6.
  '''
  
def exercise10():
  tabby_cat = "\tI'm tabbed in."
  persian_cat = "I'm split\non a line."
  backslash_cat = "I'm \\ a \\ cat."
  
  fat_cat = """
  I'll do a list:
  \t* Cat food
  \t* Fishies
  \t* Catnip\n\t* Grass
  """
  
  print tabby_cat
  print persian_cat
  print backslash_cat
  print fat_cat
  
  weird_escapes = 'start\vtest\555\xa0'
  print weird_escapes
  for unused in xrange(1000):
    for i in ['/', '-', '|','\\','|']:
      print '%s\r' % i,

def exercise11():
  pass
      
def main():
  print ('hello world')
  '''
  print 'i will now count my chickens:'
  
  print 'Hens', 25 + 30 / 6
  print 'Roosters', 100 - 25 * 3 % 4 #100 minus 75 mod 4 = 100 minus 3
  print 'now i will count the eggs:'
  
  print 3 + 2 + 1 - 5 + 4 % 2 - 1.0/4.0 +6
  #1 + 0 - 1/4 + 6
  #7 - 1/4
  #6.75, but 1/4 is 0 cause of rounding
  
  print 'is it true that 3 + 2 < 5 - 7?'
  print 3 + 2 < 5 - 7
  print 'what is 3 + 2?', 3+2
  print 'what is 5 -7?', 5 - 7
  print "oh that's why it's false"
  print 'how about some more'
  
  print 'is it greater', 5 > -2
  print 'is it greater or equal', 5 >= -2
  print 'is it less or equal', 5 <= -2
  '''
  '''
  cars = 100
  spaceinacar = 4.0
  drivers = 30
  passengers = 90
  cars_not_driven = cars - drivers
  cars_driven = drivers
  carpool_capacity = cars_driven * spaceinacar
  average_passengers_per_car = passengers / cars_driven
  
  print 'there are', cars, 'cars available.'
  print 'there are only', drivers, 'drivers available'
  print 'there will be', cars_not_driven, 'empty cars today'
  print 'we can transport', carpool_capacity, 'people today'
  print 'we have', passengers, 'to carpool today'
  print 'we need to put about', average_passengers_per_car, 'in each car'
  '''
  '''
  name = 'Zed A. Shaw'
  age = 35 #not a lie
  height = 74 #inches
  weight = 180 #pounds
  eyes = 'Blue'
  teeth = 'White'
  hair = 'Brown'
  height_cm = height * 2.2
  weight_kilos = weight * 2.2
  
  print "Let's talk about %s." % name
  print "he's %(#)0+F inches tall" % {'#': height}
  print "he's %d pounds heavy" % weight
  print "actually thats not too heavy"
  print "He's got %r eyes and %s harid,." %(eyes, hair)
  print "his teeth are usually %s depenign ont eh coffe." % teeth
  #this line is tricky, try to get it exactly right
  print "If I add %d, %d, and %d I get %d" %(age, height, weight, age + height + weight)
  '''
  exercise11()
if __name__ == '__main__':
  main()
