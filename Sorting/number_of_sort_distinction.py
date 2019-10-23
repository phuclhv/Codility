import unittest

class TestStringMethods(unittest.TestCase):
  def test_blank(self):
        self.assertEqual(self.solution([]), 0)

  def test_small(self):
        self.assertEqual(self.solution([1,5,2,1,4,0]), 11)

  def solution(self, A):
      circle_endpoints = []

      # An array to store circle endpoints, we would turn on active_cirles from left end and turn of after right end
      for i, a in enumerate(A):
          circle_endpoints += [(i-a, True), (i+a, False)]
  
      circle_endpoints.sort(key=lambda x:x[0])
    
      intersections, active_circles = 0, 0

      # Go through circle_endpoints, turn on and off and add active circles.
      for _, is_beginning in circle_endpoints:
          if is_beginning:
              intersections += active_circles
              active_circles += 1
          else:
              active_circles -= 1
          if intersections > 10E6:
              return -1
  
      return intersections

if __name__ == '__main__':
    unittest.main()
