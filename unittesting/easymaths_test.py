from easymaths import excepter
from easymaths import add

import pytest
def test_assert():
  with pytest.raises(SystemExit):
    excepter()
    
class TestAdd:
  def test_add_positives_small(self):
    assert add(2, 7) == 9
      
  def test_add_negatives_big(self):
    assert add(-20000000000, -7000000000000) == -7020000000000

  