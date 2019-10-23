'''
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
'''
from collections import defaultdict
import unittest

class TestStringMethods(unittest.TestCase):  
  def test_blank(self):
    self.assertEqual(self.solution([]), 0)

  def test_small(self):
    self.assertEqual(self.solution([4, 3, 4, 4, 4, 2]),2)
    
  def test_small_do_not_have_dominator(self):
    self.assertEqual(self.solution([1,2,3,4,5]),0)

  # Create 2 array to hold leaders counting from front and back
  # Increase count when front_leader[i] == back_leaders[i+1]
  # O(n) complexity and O(n) space
  def solution(self, A):
    
    

    # Store occurence, value in each element of leaders array
    front_leaders = [(0,0) for _ in range(len(A))]
    back_leaders = [(0,0) for _ in range(len(A))]
    
    unique_values = defaultdict(int)
    max_occur = 0
    # Build front_leaders array
    for idx in range(len(A)-1):
        unique_values[A[idx]] += 1
        if max_occur < unique_values[A[idx]]:
            front_leaders[idx] = (unique_values[A[idx]], A[idx])
            max_occur = unique_values[A[idx]]
        else:
            front_leaders[idx] = front_leaders[idx-1] 
            
    unique_values = defaultdict(int)
    max_occur = 0
    # Build back_leaders array
    for idx in range(len(A)-1,0,-1):
        unique_values[A[idx]] += 1
        if max_occur < unique_values[A[idx]]:
            back_leaders[idx] = (unique_values[A[idx]], A[idx])
            max_occur = unique_values[A[idx]]    
        else:
            back_leaders[idx] = back_leaders[idx+1] 
    
    res = 0
    # compare value, make sure each leaders are valid
    for idx in range(len(A)-1):
        if front_leaders[idx][1] == back_leaders[idx+1][1] and front_leaders[idx][0] > (idx+1)//2 and back_leaders[idx+1][0] > (len(A) - idx -1)//2:
            res +=1
    
    return res
                    
            
if __name__ == '__main__':
  unittest.main()
