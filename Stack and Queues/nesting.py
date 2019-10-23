'''


A string S consisting of N characters is called properly nested if:

        S is empty;
        S has the form "(U)" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..1,000,000];
        string S consists only of the characters "(" and/or ")".
'''
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

