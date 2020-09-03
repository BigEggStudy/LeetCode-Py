import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _011_ContainerWithMostWater import Solution

class Test_011_ContainerWithMostWater(unittest.TestCase):
    def test_maxArea(self):
        solution = Solution()
        self.assertEqual(49, solution.maxArea([1,8,6,2,5,4,8,3,7]))
