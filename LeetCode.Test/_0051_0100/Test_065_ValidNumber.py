import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _065_ValidNumber import Solution

class Test_065_ValidNumber(unittest.TestCase):
    def test_isNumber_1(self):
        solution = Solution()
        self.assertTrue(solution.isNumber("0"))

    def test_isNumber_2(self):
        solution = Solution()
        self.assertTrue(solution.isNumber(" 0.1 "))

    def test_isNumber_3(self):
        solution = Solution()
        self.assertFalse(solution.isNumber("abc"))

    def test_isNumber_4(self):
        solution = Solution()
        self.assertFalse(solution.isNumber("1 a"))

    def test_isNumber_5(self):
        solution = Solution()
        self.assertTrue(solution.isNumber("2e10"))

    def test_isNumber_6(self):
        solution = Solution()
        self.assertTrue(solution.isNumber(" -90e3   "))

    def test_isNumber_7(self):
        solution = Solution()
        self.assertFalse(solution.isNumber(" 1e"))

    def test_isNumber_8(self):
        solution = Solution()
        self.assertFalse(solution.isNumber("e3"))

    def test_isNumber_9(self):
        solution = Solution()
        self.assertTrue(solution.isNumber(" 6e-1"))

    def test_isNumber_10(self):
        solution = Solution()
        self.assertFalse(solution.isNumber(" 99e2.5 "))

    def test_isNumber_11(self):
        solution = Solution()
        self.assertTrue(solution.isNumber("53.5e93"))

    def test_isNumber_12(self):
        solution = Solution()
        self.assertFalse(solution.isNumber(" --6 "))

    def test_isNumber_13(self):
        solution = Solution()
        self.assertFalse(solution.isNumber("-+3"))

    def test_isNumber_14(self):
        solution = Solution()
        self.assertFalse(solution.isNumber("95a54e53"))
