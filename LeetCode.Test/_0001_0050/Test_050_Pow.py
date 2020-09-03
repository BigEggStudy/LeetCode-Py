import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _050_Pow import Solution

class Test_050_Pow(unittest.TestCase):
    def test_myPow(self):
        solution = Solution()
        self.assertAlmostEqual(1024.0, solution.myPow(2.0, 10))

    def test_myPow_2(self):
        solution = Solution()
        self.assertAlmostEqual(9.261, solution.myPow(2.1, 3))

    def test_myPow_negativeN(self):
        solution = Solution()
        self.assertAlmostEqual(0.250, solution.myPow(2.0, -2))

    def test_myPow_zeroX(self):
        solution = Solution()
        self.assertAlmostEqual(0, solution.myPow(0, -2))

    def test_myPow_zeroX_2(self):
        solution = Solution()
        self.assertAlmostEqual(0, solution.myPow(0, 2))

    def test_myPow_zeroN(self):
        solution = Solution()
        self.assertAlmostEqual(1, solution.myPow(5, 0))

    def test_myPow_zeroN_2(self):
        solution = Solution()
        self.assertAlmostEqual(1, solution.myPow(-5, 0))
