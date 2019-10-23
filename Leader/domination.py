'''
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
'''
import unittest

class TestStringMethods(unittest.TestCase):  
  def test_blank(self):
    self.assertEqual(self.solution([]), -1)

  def test_small(self):
    self.assertIn(self.solution([3,4,3,2,3,-1,3,3]),(0,2,4,6,7))
    
  def test_small_do_not_have_dominator(self):
    self.assertEqual(self.solution([4,2,-1,3,3]),-1)

  def solution(self, A):

    # Create a psedo stack where we only hold stack_value, and stack_size
    stack_value, stack_size = 0, 0
    
    
    for idx in range(len(A)):
      # add new value when stack_size == 0 
      if stack_size == 0:
        stack_size += 1
        stack_value = A[idx]
        res = idx
      else:
        # Delete value when there's a pair with different values
        if stack_value != A[idx]:
          stack_size -= 1
        else:
          stack_size += 1
                
    count_occurence = 0
    
    # Check if value store in stack does occurs more than half time or not
    for value in A:
      if value == stack_value:
        count_occurence += 1
    
    # return index if the value appear more than half length of array
    if count_occurence > len(A)//2:
      return res
        
    return -1
                    
            
if __name__ == '__main__':
  unittest.main()