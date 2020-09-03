import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _047_Permutations2 import Solution

import AssertHelper

class Test_047_Permutations2(unittest.TestCase):
    def test_permuteUnique(self):
        solution = Solution()
        result = solution.permuteUnique([ 1, 1, 2 ])
        self.assertEqual(3, len(result))

        AssertHelper.assertArray2D([
            [1, 1, 2],
            [1, 2, 1],
            [2, 1, 1]
        ], result)

    def test_permuteUnique_2(self):
        solution = Solution()
        result = solution.permuteUnique([ 1, 1, 2, 2, 3 ])
        self.assertEqual(30, len(result))

    def test_permuteUnique_3(self):
        solution = Solution()
        result = solution.permuteUnique([ 1, 2, 2, 3 ])
        self.assertEqual(12, len(result))

    def test_permuteUnique_notOrdered(self):
        solution = Solution()
        result = solution.permuteUnique([ 3, 1, 2, 1, 2 ])
        self.assertEqual(30, len(result))

    def test_permuteUnique_withNavigateNumber(self):
        solution = Solution()
        result = solution.permuteUnique([ -1, 2, 0, -1, 1, 0, 1 ])
        self.assertEqual(630, len(result))

    def test_permuteUnique_oneItem(self):
        solution = Solution()
        result = solution.permuteUnique([ 1 ])
        self.assertEqual(1, len(result))

    def test_permuteUnique_allSame(self):
        solution = Solution()
        result = solution.permuteUnique([ 1, 1 ])
        self.assertEqual(1, len(result))
