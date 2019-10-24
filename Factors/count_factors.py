import math
import unittest

class TestStringMethods(unittest.TestCase):  
  def test_1(self):
    self.assertEqual(self.solution(1), 1)

  def test_small(self):
    self.assertEqual(self.solution(5),2)
    
  def test_medium(self):
    self.assertEqual(self.solution(362880),160)

# Go up to square root of N, if N mod i = 0, then both i and N/i is factors --> increase count by 2
# If N is a square number, than we have to reduce count by 1 
  def solution(self, N):
      count_factor = 0
      limit = int(math.sqrt(N))
      for i in range(1, limit + 1):
          if N % i == 0:
              count_factor += 2
      if N / limit == limit: 
          count_factor -= 1
      return count_factor
                                  
if __name__ == '__main__':
  unittest.main()
