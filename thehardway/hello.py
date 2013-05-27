
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
if __name__ == '__main__':
  main()
