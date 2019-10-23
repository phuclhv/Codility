import unittest

class TestStringMethods(unittest.TestCase):
  def test_blank(self):
        self.assertEqual(self.solution(""), 1)

  def test_small_right(self):
        self.assertEqual(self.solution("{[()()]}"), 1)

  def test_small_wrong(self):
        self.assertEqual(self.solution("([)()]"), 0)

  def solution(self,S):
    
    matching_brackets = {'(':')','{':'}','[':']'}
    opened_brackets  = []
    
    # Create a stack to store opened brackets
    # If encounter closed bracked, check it with the most recent value in stack. If not matched, return 0
    for bracket in S:
        if bracket in matching_brackets:
            opened_brackets.append(bracket)
        elif len(opened_brackets) ==0 or bracket != matching_brackets[opened_brackets.pop()]:
            return 0
    
    # If there still opening brackets in stack, return 0
    return 1 if len(opened_brackets) == 0 else 0

if __name__ == '__main__':
    unittest.main()
