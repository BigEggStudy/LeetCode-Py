import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _072_EditDistance import Solution

class Test_072_EditDistance(unittest.TestCase):
    def test_minDistance_1(self):
        solution = Solution()
        self.assertEqual(3, solution.minDistance("horse", "ros"))

    def test_minDistance_2(self):
        solution = Solution()
        self.assertEqual(5, solution.minDistance("intention", "execution"))

    def test_minDistance_3(self):
        solution = Solution()
        self.assertEqual(2, solution.minDistance("ab", "bc"))

    def test_minDistance_empty(self):
        solution = Solution()
        self.assertEqual(5, solution.minDistance("horse", ""))

    def test_minDistance_empty_2(self):
        solution = Solution()
        self.assertEqual(5, solution.minDistance("", "horse"))

    def test_minDistance_oneChar(self):
        solution = Solution()
        self.assertEqual(1, solution.minDistance("a", "b"))
