'''
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

        S is empty;
        S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

    class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..200,000];
        string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
'''
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
