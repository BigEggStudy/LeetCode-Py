import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _055_JumpGame import Solution

class Test_055_JumpGame(unittest.TestCase):
    def test_canJump(self):
        solution = Solution()
        self.assertTrue(solution.canJump([2,3,1,1,4]))

    def test_canJump_2(self):
        solution = Solution()
        self.assertTrue(solution.canJump([ 7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3 ]))

    def test_canJump_oneItem_2(self):
        solution = Solution()
        self.assertTrue(solution.canJump([ 1 ]))

    def test_canJump_cannot(self):
        solution = Solution()
        self.assertFalse(solution.canJump([3,2,1,0,4]))
