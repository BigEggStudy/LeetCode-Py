import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _032_LongestValidParentheses import Solution

class Test_032_LongestValidParentheses(unittest.TestCase):
    def test_longestValidParentheses_1(self):
        solution = Solution()
        self.assertEqual(2, solution.longestValidParentheses("(()"))

    def test_longestValidParentheses_2(self):
        solution = Solution()
        self.assertEqual(4, solution.longestValidParentheses(")()())"))

    def test_longestValidParentheses_3(self):
        solution = Solution()
        self.assertEqual(2, solution.longestValidParentheses("())"))
