import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _020_ValidParentheses import Solution

class Test_020_ValidParentheses(unittest.TestCase):
    def test_isValid_oneType(self):
        solution = Solution()
        self.assertTrue(solution.isValid('()'))

    def test_isValid_multipleType(self):
        solution = Solution()
        self.assertTrue(solution.isValid('()[]{}'))

    def test_isValid_mismatch(self):
        solution = Solution()
        self.assertFalse(solution.isValid('(]'))

    def test_isValid_earlyExist(self):
        solution = Solution()
        self.assertFalse(solution.isValid('([)]'))

    def test_isValid_multipleType_2(self):
        solution = Solution()
        self.assertTrue(solution.isValid('{[]}'))

    def test_isValid_withOtherCharacter(self):
        solution = Solution()
        self.assertFalse(solution.isValid('(123)'))
