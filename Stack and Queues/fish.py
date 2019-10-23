import unittest

class TestStringMethods(unittest.TestCase):
  def test_all_down(self):
    self.assertEqual(self.solution([1,2,3,4],[1,1,1,1]), 4)

  def test_all_up(self):
    self.assertEqual(self.solution([1,2,3,4],[0,0,0,0]), 4)

  def test_small(self):
    self.assertEqual(self.solution([4,3,2,1,5],[0,1,0,0,0]), 2)


  def solution(self, A, B):
    down_stream = []
    alive_count = 0

    # Create a stack of down_stream fish
    # If a fish is upstream, if it can eat all fish going downstream before it, then it's alive. Increase count
    for idx in range(len(A)):
        if B[idx] == 1:
            down_stream.append(A[idx])
        else:
            while down_stream:
                if down_stream[-1] < A[idx]:
                    down_stream.pop()
                else:
                    break
            else:
                alive_count += 1        

    # At the end, add all alive fish going downstream                
    alive_count += len(down_stream)
    return alive_count

if __name__ == '__main__':
    unittest.main()
