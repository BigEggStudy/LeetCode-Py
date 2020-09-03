import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _028_ImplementStrStr import Solution

class Test_028_ImplementStrStr(unittest.TestCase):
    def test_strStr(self):
        solution = Solution()
        result = solution.strStr("hello", "ll")
        self.assertEqual(2, result)

    def test_strStr_1(self):
        solution = Solution()
        result = solution.strStr("hello", "lo")
        self.assertEqual(3, result)

    def test_strStr_2(self):
        solution = Solution()
        result = solution.strStr("hello", "he")
        self.assertEqual(0, result)

    def test_strStr_notfound(self):
        solution = Solution()
        result = solution.strStr("aaaaa", "bba")
        self.assertEqual(-1, result)

    def test_strStr_emptyneedle(self):
        solution = Solution()
        result = solution.strStr("aaaaa", "")
        self.assertEqual(0, result)
