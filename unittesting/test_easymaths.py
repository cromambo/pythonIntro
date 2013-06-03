
import unittest
from easymaths import add

class TestEasyMaths(unittest.TestCase):
  def setUp(self):
    pass
  
  def test_two_positive_small(self):
    self.assertEqual(add(1, 3), 4)
  
  def test_two_negative_small(self):
    self.assertEqual(add(-11, -3), -14)
    
  def test_positive_and_negative__small(self):
    self.assertEqual(add(1, -3), -2)
    self.assertEqual(add(-1, 2), 1)
  

if __name__ == '__main__':
  unittest.main()