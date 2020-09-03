import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _069_Sqrt_X import Solution

class Test_069_Sqrt_X(unittest.TestCase):
    def test_mySqrt_0(self):
        solution = Solution()
        self.assertEqual(0, solution.mySqrt(0))

    def test_mySqrt_1(self):
        solution = Solution()
        self.assertEqual(1, solution.mySqrt(1))

    def test_mySqrt_2(self):
        solution = Solution()
        self.assertEqual(1, solution.mySqrt(2))

    def test_mySqrt_3(self):
        solution = Solution()
        self.assertEqual(1, solution.mySqrt(3))

    def test_mySqrt_4(self):
        solution = Solution()
        self.assertEqual(2, solution.mySqrt(4))

    def test_mySqrt_8(self):
        solution = Solution()
        self.assertEqual(2, solution.mySqrt(8))

    def test_mySqrt_9(self):
        solution = Solution()
        self.assertEqual(3, solution.mySqrt(9))

    def test_mySqrt_16(self):
        solution = Solution()
        self.assertEqual(4, solution.mySqrt(16))
