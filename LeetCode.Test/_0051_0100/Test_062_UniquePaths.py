import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _062_UniquePaths import Solution

class Test_062_UniquePaths(unittest.TestCase):
    def test_uniquePaths_1(self):
        solution = Solution()
        self.assertEqual(3, solution.uniquePaths(3, 2))

    def test_uniquePaths_2(self):
        solution = Solution()
        self.assertEqual(28, solution.uniquePaths(3, 7))

    def test_uniquePaths_oneRow(self):
        solution = Solution()
        self.assertEqual(1, solution.uniquePaths(1, 7))

    def test_uniquePaths_oneColumn(self):
        solution = Solution()
        self.assertEqual(1, solution.uniquePaths(7, 1))

    def test_uniquePaths_twoRow(self):
        solution = Solution()
        self.assertEqual(7, solution.uniquePaths(2, 7))

    def test_uniquePaths_twoColumn(self):
        solution = Solution()
        self.assertEqual(7, solution.uniquePaths(7, 2))
