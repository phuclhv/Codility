
import unittest

class TestStringMethods(unittest.TestCase):
  def test_blank(self):
        self.assertEqual(self.solution(""), 1)

  def test_small_balance(self):
        self.assertEqual(self.solution("(((())))"), 1)

  def test_small_mixed(self):
        self.assertEqual(self.solution("(())())"), 0)

  def test_small_mixed1(self):
        self.assertEqual(self.solution("(())(())"), 1)

  def solution(self, S):
    count_open = 0

    # Going through the list, return 0 if there's more closed bracket than opened bracket at any point
    for bracket in S:
        if bracket == '(':
            count_open += 1
        else:
            count_open -= 1
        if count_open < 0:
            return 0

    # Only return true if all brackets have been matched            
    return 0 if count_open != 0 else 1

if __name__ == '__main__':
    unittest.main()

