'''
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

    def solution(H)

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:
  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8

the function should return 7. The figure shows one possible arrangement of seven blocks.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array H is an integer within the range [1..1,000,000,000].

'''
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

