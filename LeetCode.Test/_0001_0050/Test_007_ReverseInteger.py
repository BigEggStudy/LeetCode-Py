import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _007_ReverseInteger import Solution

class Test_007_ReverseInteger(unittest.TestCase):
    def test_reverse_1(self):
        solution = Solution()
        result = solution.reverse(123)

        self.assertEqual(321, result)

    def test_reverse_2(self):
        solution = Solution()
        result = solution.reverse(-123)

        self.assertEqual(-321, result)

    def test_reverse_3(self):
        solution = Solution()
        result = solution.reverse(120)

        self.assertEqual(21, result)

    def test_reverse_overflow(self):
        solution = Solution()
        result = solution.reverse(1534236469)

        self.assertEqual(0, result)

    def test_reverse_overflow_2(self):
        solution = Solution()
        result = solution.reverse(-1534236469)

        self.assertEqual(0, result)

if __name__ == '__main__':
    unittest.main()
