import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _030_SubstringWithConcatenationOfAllWords import Solution

import AssertHelper

class Test_030_SubstringWithConcatenationOfAllWords(unittest.TestCase):
    def test_findSubstring_haveMatch(self):
        solution = Solution()
        result = solution.findSubstring("barfoothefoobarman", ["foo","bar"])
        AssertHelper.assertArray([0, 9], result)

    def test_findSubstring_haveMatch_2(self):
        solution = Solution()
        result = solution.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
        AssertHelper.assertArray([6, 9, 12], result)

    def test_findSubstring_sameWord(self):
        solution = Solution()
        result = solution.findSubstring("barfoothefoofooman", ["foo","foo"])
        AssertHelper.assertArray([9], result)

    def test_findSubstring_emptyWords(self):
        solution = Solution()
        result = solution.findSubstring("barfoothefoofooman", [])
        AssertHelper.assertArray([], result)

    def test_findSubstring_noMatch(self):
        solution = Solution()
        result = solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])
        AssertHelper.assertArray([], result)
