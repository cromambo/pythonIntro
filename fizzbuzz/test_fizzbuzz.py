from fizzbuzz import fizzbuzz
import pytest

def test_fizzbuzz_2_9():
  assert fizzbuzz(9, 2, 9) == 'buzz'
  assert fizzbuzz(17, 2, 9) == 17
  assert fizzbuzz(18, 2, 9) == 'fizzbuzz'
  assert fizzbuzz(19, 2, 9) == 19
  assert fizzbuzz(20, 2, 9) == 'fizz'

def test_fizzbuzz_divzero():  
  assert fizzbuzz(20, 0, 9) == 'error'
  assert fizzbuzz(20, 9, 0) == 'error'
  assert fizzbuzz(20, 0, 0) == 'error'
  assert fizzbuzz(0, 0, 0) == 'error'
  assert fizzbuzz(0, 3, 0) == 'error'
  assert fizzbuzz(0, 0, 5) == 'error'
  assert fizzbuzz(0, 3, 5) == 'fizzbuzz'
  
def test_fizzbuzz_3_5_nondivisible():  
  nonfizzbuzzNumList = [1, 2, 4, 7, -1, -2, -4, -7]
  for num in nonfizzbuzzNumList:
    assert fizzbuzz(num, 3, 5) == num
  
def test_fizzbuzz_3_5_fizz():    
  fizzNumList = [3, 6, 9, 12, 18, 21, -3, -6, -9]
  for num in fizzNumList:
    assert fizzbuzz(num, 3, 5) == 'fizz'
    
def test_fizzbuzz_3_5_buzz():    
  buzzNumList = [5, 10, 20, 25, 35, -5, -10, -20, -25, -35]
  for num in buzzNumList:
    assert fizzbuzz(num, 3, 5) == 'buzz'
    
def test_fizzbuzz_3_5_fizzbuzz():  
  fizzbuzzNumList = [15, 30, 45, 60, 150, 0, -15, -30, -45, -60, -150]
  for num in fizzbuzzNumList:
    assert fizzbuzz(num, 3, 5) == 'fizzbuzz'

def test_fizzbuzz_non_numeric_input():    
  dummylist = []
  junkValueList = ['a', 'string', '3', dummylist]
  with pytest.raises(TypeError):
    for val in junkValueList:
      fizzbuzz(val, 3, 5)
    