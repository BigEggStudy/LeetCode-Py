import unittest

import sys
sys.path.append('LeetCode/_1051_1100')
sys.path.append('LeetCode.Test')

from _1057_CampusBikes import Solution
import AssertHelper

class Test_1057_CampusBikes(unittest.TestCase):
    def test_assignBikes_1(self):
        solution = Solution()
        result = solution.assignBikes([[0,0],[2,1]], [[1,2],[3,3]])
        self.assertSequenceEqual([1,0], result)

    def test_assignBikes_2(self):
        solution = Solution()
        result = solution.assignBikes([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]])
        self.assertEqual([0,2,1], result)
