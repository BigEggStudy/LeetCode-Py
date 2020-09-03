import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _042_TrappingRainWater import Solution

class Test_042_TrappingRainWater(unittest.TestCase):
    def test_trap_1(self):
        solution = Solution()
        self.assertEqual(6, solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
