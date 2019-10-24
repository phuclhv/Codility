from collections import defaultdict
import unittest

class TestStringMethods(unittest.TestCase):  
  def test_blank(self):
    self.assertEqual(self.solution([]), 0)

  def test_small(self):
    self.assertEqual(self.solution([3, 2, 6, -1, 4, 5, -1, 2]),17)
    
  def test_small_all_neg(self):
    self.assertEqual(self.solution([-5, -4, -3, -2, -1]),0)

  def test_small_all_pos(self):
    self.assertEqual(self.solution([1, 3, 5, 2, 4]), 8)

  # complexity O(n) space O(n)
  def solution(self, A):
    max_slice_before = [0 for _ in range(len(A))]
    max_slice_after = [0 for _ in range(len(A))]
    
    for idx in range(1, len(A)):
        max_slice_before[idx] = max(max_slice_before[idx-1] + A[idx], 0)
    
    for idx in range(len(A)-2,-1,-1):
        max_slice_after[idx] = max(max_slice_after[idx+1] + A[idx], 0)
    
    max_sum_double = 0
    for idx in range(1, len(A)-1):
        max_sum_double = max(max_sum_double, max_slice_before[idx - 1] + max_slice_after[idx+1])
    
    return max_sum_double
            
if __name__ == '__main__':
  unittest.main()
