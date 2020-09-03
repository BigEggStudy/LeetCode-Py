import unittest

import sys
sys.path.append('LeetCode/_1001_1050')
sys.path.append('LeetCode.Test')

from _1007_MinimumDominoRotationsForEqualRow import Solution
import AssertHelper

class Test_1007_MinimumDominoRotationsForEqualRow(unittest.TestCase):
    def test_minDominoRotations_1(self):
        solution = Solution()
        result = solution.minDominoRotations([ 2, 1, 2, 4, 2, 2 ], [ 5, 2, 6, 2, 3, 2 ])
        self.assertEqual(2, result)

    def test_minDominoRotations_2(self):
        solution = Solution()
        result = solution.minDominoRotations([ 3, 5, 1, 2, 3], [ 3, 6, 3, 3, 4])
        self.assertEqual(-1, result)
