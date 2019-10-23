import unittest

class TestStringMethods(unittest.TestCase):  
  def test_blank(self):
    self.assertEqual(self.solution([]), 0)

  def test_small(self):
    self.assertEqual(self.solution([8,8,5,7,9,8,7,4,9]), 7)

  def test_small_one_height(self):
    self.assertEqual(self.solution([2,2,2,2,2,2,2,2,2]), 1)

  def test_small_up_and_down(self):
    self.assertEqual(self.solution([1,2,1,2,1,2,1,2,1,2]), 6)
  
  def solution(self, H):
    num_blocks  = 0
    block_height = 0
    blocks = []

    # if the height is less then total block height: keep removing block
    # if the height is larger then total block height: adding one block
    for idx in range(len(H)):

      while blocks and block_height > H[idx]:
        block_height -= blocks.pop()

      if H[idx] > block_height:
        num_blocks += 1
        blocks.append(H[idx] - block_height)
        block_height = H[idx]
                  
    return num_blocks
            
if __name__ == '__main__':
  unittest.main()

