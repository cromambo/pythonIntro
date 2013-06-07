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
import collections

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
 
def prime_gen(): # doesnt work!
  #2, 3, 5, 7, 11, 13, 17, 19
  yield 2
  yield 3
  n = 5
  base = 5
  while True:
    if n % 2 == 0 or n % 3 == 0: #if divisible, then isnt prime
      root = int(n**0.5)
    if n%base == 0:
      n = base
      yield base      
    if n%(base+2) == 0:
      n = base
      yield base + 2
    base += 6
    n += 6
    
#500001th prime 7368791
#time: 40.6859998703    
def get_primes_brute(number):
  while True: 
    if is_prime(number):
      yield number
    number += 1

#this is marginally faster than trying every number, doesnt let you pick a starting number
#500001th prime 7368791
#time: 39.2239999771

def get_primes():
  yield 2
  yield 3
  number = 5
  while True: 
    if is_prime(number):
      yield number
    if is_prime(number+2):
      yield number + 2
    number += 6
    
    
#euler #7, find the 10001st prime
def find_the_xth_prime(x):
  if not int(x) >= 1:
    return 'Error: x must be a positive number'

  gen = get_primes()
  for i in range(1, x):
    next(gen)
  return next(gen)

  #euler #10, sum of primes under 2 million
def sum_of_primes_under_x(x):
  if not int(x) >= 2:
    return 'Error: x must be a positive number 2 or greater'
    
  gen = get_primes()
  next_prime, sum = 0, 0
  while next_prime < x:
    sum += next_prime
    next_prime = next(gen)
  return sum

def fibonacci_gen():
  a = 1
  b = 1
  while True:
    a, b = b, a+b
    yield a

def multiples_of_x_or_y_gen(x, y):
  count = 1
  while True:
    # print (count)
    if count % x == 0 or count % y == 0:
      yield count
    count += 1

def factors(num):
  root = int((num ** 0.5)) + 1
  factors = []
  for i in range(1, root):
    if num % i == 0:
      factors.append(i)
      factors.append(int(num / i))
  print ('num:', num, 'factors:', factors)
  return sorted(factors)

def primes_in_list(list):
  # primes = []
  # for i in enumerate(list):
    # if is_prime(i):
      # primes.append(i)
  return [i for i in list if is_prime(i)]
  
def sum_of_list(list):
  return sum(list)
 

def is_palidrome(num):
  string = str(num)
  #extended slice syntax [begin:end:step]
  reverse = string[::-1]
  return string == reverse
  
def euler4():
  '''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

  Find the largest palindrome made from the product of two 3-digit numbers.
  '''
  Sourceformat = ' %dx%d '
  palindromes = {}
  for i in range(999, 100, -1):
    for j in range(999, 100, -1):
      multiple = i*j       
      if is_palidrome(multiple):
        if multiple in palindromes:
          palindromes[multiple] += Sourceformat % (i, j)
        else:
          palindromes[multiple] = Sourceformat % (i, j)
        break
  for key in sorted(palindromes.keys()):
    print ('key:', key, 'Source:', palindromes[key])
  return max(palindromes.keys())
  
def euler5():
  pass
def euler3():
  '''The prime factors of 13195 are 5, 7, 13 and 29.
  What is the largest prime factor of the number 600851475143 ?
  '''    
  factorList = factors(600851475143)
  primes = primes_in_list(factorList)
  print (primes[-1])
  
def euler1():
  sum = 0
  gen = multiples_of_x_or_y_gen(3, 5)
  multiple = 0
  while multiple < 1000:
    sum += multiple
    multiple = next(gen)
  return sum
  
def euler2():
  fibgen = fibonacci_gen()
  val = 0
  sum = 0
  while val < 4000000:
    # print (val)
    if val % 2 == 0:
      sum += val
    val = next(fibgen)
  print ('sum:', sum)
    
def main():
  time_start = time.time()
  
  s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
  d = collections.defaultdict(int)
  for k, v in s:
    d[k].append(v)
  print(d.items())

  # print (euler4())

  # print ('prime count:', sum_of_primes_under_x(200000))
  # x = 10001
  # print ('%dth prime' % x, find_the_xth_prime(x))

  # gen = get_primes_brute(100)
  # for i in range(0, 10):
    # print (next(gen))
  
  time_end = time.time()
  print ('time:', time_end - time_start)
  


if __name__ == '__main__':
  main()