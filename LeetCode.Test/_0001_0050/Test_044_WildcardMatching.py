import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _044_WildcardMatching import Solution

class Test_044_WildcardMatching(unittest.TestCase):
    def test_isMatch_1(self):
        solution = Solution()
        self.assertFalse(solution.isMatch("aa", "a"))

    def test_isMatch_2(self):
        solution = Solution()
        self.assertTrue(solution.isMatch("aa", "*"))

    def test_isMatch_3(self):
        solution = Solution()
        self.assertFalse(solution.isMatch("cb", "?a"))

    def test_isMatch_4(self):
        solution = Solution()
        self.assertTrue(solution.isMatch("adceb", "*a*b"))

    def test_isMatch_5(self):
        solution = Solution()
        self.assertFalse(solution.isMatch("acdcb", "a*c?b"))

    def test_isMatch_6(self):
        solution = Solution()
        self.assertTrue(solution.isMatch("aa", "aa"))

    def test_isMatch_7(self):
        solution = Solution()
        self.assertTrue(solution.isMatch("aa", "a*"))

    def test_isMatch_8(self):
        solution = Solution()
        self.assertTrue(solution.isMatch("ab", "?*"))

    def test_isMatch_9(self):
        solution = Solution()
        self.assertFalse(solution.isMatch("aab", "c*a*b"))
