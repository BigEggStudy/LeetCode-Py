import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _010_RegularExpressionMatching import Solution

class Test_010_RegularExpressionMatching(unittest.TestCase):
    def test_isMatch_match(self):
        solution = Solution()
        self.assertTrue(solution.isMatch("ab", "ab"))

    def test_isMatch_notmatch(self):
        solution = Solution()
        self.assertFalse(solution.isMatch("aa", "a"))

    def test_isMatch_withdot_match(self):
        solution = Solution()
        self.assertTrue(solution.isMatch("ab", "a."))

    def test_isMatch_withdot_notmatch(self):
        solution = Solution()
        self.assertFalse(solution.isMatch("aa", "b."))

    def test_isMatch_withstar_match(self):
        solution = Solution()
        self.assertTrue(solution.isMatch("aab", "a*b"))
        self.assertTrue(solution.isMatch("aab", "c*a*b"))

    def test_isMatch_withstar_notmatch(self):
        solution = Solution()
        self.assertFalse(solution.isMatch("ba", "a*"))

    def test_isMatch_withdotandstar_match(self):
        solution = Solution()
        self.assertTrue(solution.isMatch("", ".*"))
        self.assertTrue(solution.isMatch("ab", ".*"))

    def test_isMatch_withdotandstar_notmatch(self):
        solution = Solution()
        self.assertFalse(solution.isMatch("mississippi", "mis*is*p*."))
