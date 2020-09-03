import unittest
import pytest

import sys
sys.path.append('LeetCode/_0001_0050')

from _029_DivideTwoIntegers import Solution

class Test_029_DivideTwoIntegers(unittest.TestCase):
    def test_divide_1(self):
        solution = Solution()
        self.assertEqual(3, solution.divide(10, 3))

    def test_divide_2(self):
        solution = Solution()
        self.assertEqual(-2, solution.divide(7, -3))

    def test_divide_3(self):
        solution = Solution()
        self.assertEqual(-2, solution.divide(-7, 3))

    def test_divide_4(self):
        solution = Solution()
        self.assertEqual(2, solution.divide(-7, -3))

    def test_divide_norest_1(self):
        solution = Solution()
        self.assertEqual(1, solution.divide(2, 2))
        self.assertEqual(2, solution.divide(4, 2))
        self.assertEqual(3, solution.divide(6, 2))

    def test_divide_norest_2(self):
        solution = Solution()
        self.assertEqual(-1, solution.divide(2, -2))
        self.assertEqual(-2, solution.divide(4, -2))
        self.assertEqual(-3, solution.divide(6, -2))

    def test_divide_norest_3(self):
        solution = Solution()
        self.assertEqual(-1, solution.divide(-2, 2))
        self.assertEqual(-2, solution.divide(-4, 2))
        self.assertEqual(-3, solution.divide(-6, 2))

    def test_divide_norest_4(self):
        solution = Solution()
        self.assertEqual(1, solution.divide(-2, -2))
        self.assertEqual(2, solution.divide(-4, -2))
        self.assertEqual(3, solution.divide(-6, -2))

    def test_divide_overflow_1(self):
        solution = Solution()
        self.assertEqual(2147483647, solution.divide(2147483647, 1))

    def test_divide_overflow_2(self):
        solution = Solution()
        self.assertEqual(-2147483648, solution.divide(-2147483648, 1))

    def test_divide_overflow_3(self):
        solution = Solution()
        self.assertEqual(-2147483647, solution.divide(2147483647, -1))

    def test_divide_overflow_4(self):
        solution = Solution()
        self.assertEqual(2147483647, solution.divide(-2147483648, -1))

    @pytest.mark.timeout(1)
    def test_divide_large_number_1(self):
        solution = Solution()
        self.assertEqual(1073741823, solution.divide(2147483647, 2))

    @pytest.mark.timeout(1)
    def test_divide_large_number_2(self):
        solution = Solution()
        self.assertEqual(-1073741823, solution.divide(2147483647, -2))

    @pytest.mark.timeout(1)
    def test_divide_large_number_3(self):
        solution = Solution()
        self.assertEqual(-1073741824, solution.divide(-2147483648, 2))

    @pytest.mark.timeout(1)
    def test_divide_large_number_4(self):
        solution = Solution()
        self.assertEqual(1073741824, solution.divide(-2147483648, -2))
