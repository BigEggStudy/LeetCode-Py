import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _045_JumpGame2 import Solution

class Test_045_JumpGame2(unittest.TestCase):
    def test_jump(self):
        solution = Solution()
        self.assertEqual(2, solution.jump([2,3,1,1,4]))

    def test_jump_2(self):
        solution = Solution()
        self.assertEqual(2, solution.jump([ 7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3 ]))

    def test_jump_oneItem_2(self):
        solution = Solution()
        self.assertEqual(0, solution.jump([ 1 ]))
