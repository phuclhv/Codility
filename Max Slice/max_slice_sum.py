from collections import defaultdict
import unittest

class TestStringMethods(unittest.TestCase):  
  def test_blank(self):
    self.assertEqual(self.solution([]), 0)

  def test_small(self):
    self.assertEqual(self.solution([3, 2, -6, 4, 0]),5)
    
  def test_small_all_neg(self):
    self.assertEqual(self.solution([-5, -4, -3, -2, -1]),-1)

  def test_small_all_pos(self):
    self.assertEqual(self.solution([1, 3, 5 , 2, 4]), 15)

  def solution(self, A):
    # If all element is negative, the slice will be the max value
    if not A:
      return 0
    max_slice, cur_slice = max(A), 0
    
    # Keep compare cur_slice with max_slice. 
    # If cur_slice <0, it means that mean that our starting idx will not be in that range --> reset cur_slice
    for value in A:
        cur_slice += value
        max_slice = max(max_slice, cur_slice)
        cur_slice = max(cur_slice,0)
        
    return max_slice
            
if __name__ == '__main__':
  unittest.main()
