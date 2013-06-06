'''>>> class Bank(): # let's create a bank, building ATMs
...    crisis = False
...    def create_atm(self):
...        while not self.crisis:
...            yield "$100"
>>> hsbc = Bank() # when everything's ok the ATM gives you as much as you want
>>> corner_street_atm = hsbc.create_atm()
>>> print(corner_street_atm.next())
$100
>>> print(corner_street_atm.next())
$100
>>> print([corner_street_atm.next() for cash in range(5)])
['$100', '$100', '$100', '$100', '$100']
>>> hsbc.crisis = True # crisis is coming, no more money!
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> wall_street_atm = hsbc.create_atm() # it's even true for new ATMs
>>> print(wall_street_atm.next())
<type 'exceptions.StopIteration'>
>>> hsbc.crisis = False # trouble is, even post-crisis the ATM remains empty
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> brand_new_atm = hsbc.create_atm() # build a new one to get back in business
>>> for cash in brand_new_atm:
...    print cash'''

import time

#6.865 sec for primes under 1 million
#17.19 sec for primes under 2 million
def is_prime2(n):
    """"precondition n is a nonnegative integer
postcondition:  return True if n is prime and False otherwise."""
    if n < 2: 
         return False;
    if n % 2 == 0:
         # return False
         return n == 2
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

#4.5 second for primes under 1 million
#10.73 second for primes under 2 million
#6.86 second for primes under 2 million with generator method
def is_prime(n):
  if n == 2 or n == 3:
    return True
  if n < 2 or n%2 == 0: #there are no primes less than 2, nor any even number
    return False
  if n < 9: #of (2, 3, 4, 5, 6, 7, 8), (2, 3, 4, 6, 8) are eliminated already, leaving 5 and 7, which are prime
    return True
  if n%3 == 0:
    return False
  #now all multiples of 2 and 3 have been eliminated
  r = int(n**0.5) #square root
  #only need to check divisors up to the square root of the tested number b/c past that, divisors repeat
  #consider 144
  #9 x 16 = 144
  #12 x 12 = 144
  #16 x 9 = 144
  #so while trying values, ...8, 9, 10, 11, 12..
  #testing with 13 would be useless b/c 13 x 11.08 = 144 was already covered by 11.08 x 13 = 144
  
  #all prime numbers other than 2 and 3 are of the form 6n+/-1
  #so trying every 6th number lessens how many values are checked
  #I do this by starting at 5, checking primality with 5 and 7, and adding 6 for the next check
  base = 5
  while base <= r:
    # print str(base) + ' ',
    if n%base == 0: return False
    if n%(base+2) == 0: return False
    base += 6
  return True
 
def get_primes(number):
  while True: 
    if is_prime(number):
      yield number
    number += 1
    
  #euler #7, find the 10001st prime
def find_the_xth_prime(x):
  if not int(x) >= 1:
    return 'Error: x must be a positive number'

  gen = get_primes(2)
  for i in xrange(1, x+1):
    prime = gen.next()
    if i == x:
      return prime

  #euler #10, sum of primes under 2 million
def sum_of_primes_under_x(x):
  if not int(x) >= 2:
    return 'Error: x must be a positive number 2 or greater'
    
  gen = get_primes(2)
  next_prime, sum = 0, 0
  while next_prime < x:
    sum += next_prime
    next_prime = gen.next()
  return sum
     
def main():
  time_start = time.time()


  # print 'prime count:', sum_of_primes_under_x(2000000)
  x = 10001
  print '%dth prime' % x, find_the_xth_prime(x)

  
  time_end = time.time()
  print 'time:', time_end - time_start
  


if __name__ == '__main__':
  main()