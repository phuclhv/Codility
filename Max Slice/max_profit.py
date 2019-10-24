from collections import defaultdict
import unittest

class TestStringMethods(unittest.TestCase):  
  def test_blank(self):
    self.assertEqual(self.solution([]), 0)

  def test_small(self):
    self.assertEqual(self.solution([1, 2, 3, 4, 5]),4)
    
  def test_small_no_best_way(self):
    self.assertEqual(self.solution([5, 4, 3, 2, 1]),0)

  def test_small_random(self):
    self.assertEqual(self.solution([23171, 21011, 21123 , 21366 , 21013, 21367]),356)

  def solution(self, A):
    if len(A) == 0:
        return 0
        
    cur_min, cur_max, profit = A[0], A[0], 0
    for value in A:
        cur_min = min(cur_min, value)
        cur_max = max(cur_min, value)
        profit = max(profit, cur_max - cur_min)
        
    return profit
                    
            
if __name__ == '__main__':
  unittest.main()
