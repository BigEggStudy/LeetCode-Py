import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _009_PalindromeNumber import Solution

class Test_009_PalindromeNumber(unittest.TestCase):
    def test_isPalindrome_Negative(self):
        solution = Solution()
        self.assertFalse(solution.isPalindrome(-1))
        self.assertFalse(solution.isPalindrome(-12))
        self.assertFalse(solution.isPalindrome(-121))

    def test_isPalindrome_LessThan_10(self):
        solution = Solution()

        for i in range(10):
            self.assertTrue(solution.isPalindrome(i))

    def test_isPalindrome_is_palindrome(self):
        solution = Solution()

        self.assertTrue(solution.isPalindrome(11))
        self.assertTrue(solution.isPalindrome(121))
        self.assertTrue(solution.isPalindrome(1441))

    def test_isPalindrome_isnot_alindrome(self):
        solution = Solution()

        self.assertFalse(solution.isPalindrome(12))
        self.assertFalse(solution.isPalindrome(123))
        self.assertFalse(solution.isPalindrome(1451))
