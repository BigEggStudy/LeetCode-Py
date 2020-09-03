import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _005_LongestPalindromicSubstring import Solution

class Test_005_LongestPalindromicSubstring(unittest.TestCase):
    def test_longestPalindromeTest_Odd(self):
        input = "abcdefgfedcba"

        solution = Solution()
        result = solution.longestPalindrome(input)

        self.assertEqual("abcdefgfedcba", result)


    def test_longestPalindromeTest_Even(self):
        input = "abcdefggfedcba"

        solution = Solution()
        result = solution.longestPalindrome(input)

        self.assertEqual("abcdefggfedcba", result)


    def test_longestPalindromeTest_AllTheSame_Odd(self):
        input = "ccc"

        solution = Solution()
        result = solution.longestPalindrome(input)

        self.assertEqual("ccc", result)


    def test_longestPalindromeTest_AllTheSame_Even(self):
        input = "aaaaaaaaaa"

        solution = Solution()
        result = solution.longestPalindrome(input)

        self.assertEqual("aaaaaaaaaa", result)


    def test_longestPalindromeTest_EmptyString(self):
        input = ""

        solution = Solution()
        result = solution.longestPalindrome(input)

        self.assertEqual("", result)


    def test_longestPalindromeTest_OneCharacterString(self):
        input = "a"

        solution = Solution()
        result = solution.longestPalindrome(input)

        self.assertEqual("a", result)


    def test_longestPalindromeTest_MultiplePalindrome_LongestAtStart(self):
        input = "aabccdccbaaeeggee"

        solution = Solution()
        result = solution.longestPalindrome(input)

        self.assertEqual("aabccdccbaa", result)


    def test_longestPalindromeTest_MultiplePalindrome_LongestAtEnd(self):
        input = "eegffgeeaabcdcbaa"

        solution = Solution()
        result = solution.longestPalindrome(input)

        self.assertEqual("aabcdcbaa", result)


    def test_longestPalindromeTest_MultipleMixPalindrome(self):
        input = "abcdcbbcd"

        solution = Solution()
        result = solution.longestPalindrome(input)

        self.assertEqual("dcbbcd", result)


    def test_longestPalindromeTest_MultipleMixPalindrome_2(self):
        input = "abcddcbebcd"

        solution = Solution()
        result = solution.longestPalindrome(input)

        self.assertEqual("dcbebcd", result)


if __name__ == '__main__':
    unittest.main()
