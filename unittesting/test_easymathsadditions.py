
import unittest
from easymaths import add

class TestEasyMaths(unittest.TestCase):
  def setUp(self):
    pass
  
  def test_two_positive_giant(self):
    self.assertEqual(add(100000000, 3), 100000003)
  

if __name__ == '__main__':
  unittest.main()