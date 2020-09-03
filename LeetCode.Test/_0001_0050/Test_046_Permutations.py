import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _046_Permutations import Solution

import AssertHelper

class Test_046_Permutations(unittest.TestCase):
    def test_permute(self):
        solution = Solution()
        result = solution.permute([ 1, 2, 3 ])
        self.assertEqual(6, len(result))

        AssertHelper.assertArray2D([
            [1, 2, 3],
            [2, 1, 3],
            [2, 3, 1],
            [1, 3, 2],
            [3, 1, 2],
            [3, 2, 1]
        ], result)

    def test_permute_2(self):
        solution = Solution()
        result = solution.permute([ 1, 2, 3, 4 ])
        self.assertEqual(24, len(result))

    def test_permute_oneItem(self):
        solution = Solution()
        result = solution.permute([ 1 ])
        self.assertEqual(1, len(result))