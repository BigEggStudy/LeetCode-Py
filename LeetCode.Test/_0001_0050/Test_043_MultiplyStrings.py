import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _043_MultiplyStrings import Solution

class Test_043_MultiplyStrings(unittest.TestCase):
    def test_multiply_1(self):
        solution = Solution()
        self.assertEqual("6", solution.multiply("2", "3"))

    def test_multiply_2(self):
        solution = Solution()
        self.assertEqual("56088", solution.multiply("123", "456"))

    def test_multiply_3(self):
        solution = Solution()
        self.assertEqual("891", solution.multiply("9", "99"))

    def test_multiply_zero(self):
        solution = Solution()
        self.assertEqual("0", solution.multiply("9", "0"))

    def test_multiply_zero_2(self):
        solution = Solution()
        self.assertEqual("0", solution.multiply("0", "9"))
