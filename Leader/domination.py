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