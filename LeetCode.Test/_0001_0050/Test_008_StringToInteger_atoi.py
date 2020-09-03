import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _008_StringToInteger_atoi import Solution

class Test_008_StringToInteger_atoi(unittest.TestCase):
    def test_myAtoi_1(self):
        solution = Solution()
        result = solution.myAtoi("42")

        self.assertEqual(42, result)

    def test_myAtoi_2(self):
        solution = Solution()
        result = solution.myAtoi("-42")

        self.assertEqual(-42, result)

    def test_myAtoi_startWith_space(self):
        solution = Solution()
        result = solution.myAtoi("   -42")

        self.assertEqual(-42, result)

    def test_myAtoi_startWith_space_2(self):
        solution = Solution()
        result = solution.myAtoi("   +42")

        self.assertEqual(42, result)

    def test_myAtoi_endWith_word(self):
        solution = Solution()
        result = solution.myAtoi("4193 with words")

        self.assertEqual(4193, result)

    def test_myAtoi_startWith_word(self):
        solution = Solution()
        result = solution.myAtoi("words and 987")

        self.assertEqual(0, result)

    def test_myAtoi_overflow(self):
        solution = Solution()
        result = solution.myAtoi("91283472332")

        self.assertEqual(2147483647, result)

    def test_myAtoi_overflow_2(self):
        solution = Solution()
        result = solution.myAtoi("-91283472332")

        self.assertEqual(-2147483648, result)

    def test_myAtoi_invalid(self):
        solution = Solution()
        result = solution.myAtoi("+")

        self.assertEqual(0, result)

    def test_myAtoi_invalid_2(self):
        solution = Solution()
        result = solution.myAtoi("-")

        self.assertEqual(0, result)

    def test_myAtoi_invalid_3(self):
        solution = Solution()
        result = solution.myAtoi("+-2")

        self.assertEqual(0, result)

if __name__ == '__main__':
    unittest.main()
