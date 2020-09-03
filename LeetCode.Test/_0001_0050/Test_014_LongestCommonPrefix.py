import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _014_LongestCommonPrefix import Solution

class Test_014_LongestCommonPrefix(unittest.TestCase):
    def test_longestCommonPrefix_have(self):
        solution = Solution()
        self.assertEqual('fl', solution.longestCommonPrefix(["flower","flow","flight"]))

    def test_longestCommonPrefix_nothave(self):
        solution = Solution()
        self.assertEqual('', solution.longestCommonPrefix(["dog","racecar","car"]))

    def test_longestCommonPrefix_nothave_2(self):
        solution = Solution()
        self.assertEqual('', solution.longestCommonPrefix(["","racecar","car"]))

    def test_longestCommonPrefix_empty(self):
        solution = Solution()
        self.assertEqual('', solution.longestCommonPrefix([]))

    def test_longestCommonPrefix_onlyone(self):
        solution = Solution()
        self.assertEqual('dog', solution.longestCommonPrefix(["dog"]))
