import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _003_LongestSubstringWithoutRepeatingCharacters import Solution


class Test_003_LongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        input = "abcabcbb"

        solution = Solution()
        result = solution.lengthOfLongestSubstring(input)

        self.assertEqual(3, result)


    def test_lengthOfLongestSubstring(self):
        input = "pwwkew"

        solution = Solution()
        result = solution.lengthOfLongestSubstring(input)

        self.assertEqual(3, result)


    def test_lengthOfLongestSubstring_repeatChars(self):
        input = "bbbbb"

        solution = Solution()
        result = solution.lengthOfLongestSubstring(input)

        self.assertEqual(1, result)


    def test_lengthOfLongestSubstring_emptyInput(self):
        input = ""

        solution = Solution()
        result = solution.lengthOfLongestSubstring(input)

        self.assertEqual(0, result)


    def test_lengthOfLongestSubstring_longString(self):
        input = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

        solution = Solution()
        result = solution.lengthOfLongestSubstring(input)

        self.assertEqual(26, result)


    def test_lengthOfLongestSubstring_longString_haveShortRepeat(self):
        input = "abcdefghijklmnopqrstuvwxyzabcdefghijk  lmnopqrstuvwxyz"

        solution = Solution()
        result = solution.lengthOfLongestSubstring(input)

        self.assertEqual(27, result)


if __name__ == '__main__':
    unittest.main()
