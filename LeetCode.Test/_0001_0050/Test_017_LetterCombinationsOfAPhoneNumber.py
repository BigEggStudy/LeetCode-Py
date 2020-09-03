import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _017_LetterCombinationsOfAPhoneNumber import Solution

class Test_017_LetterCombinationsOfAPhoneNumber(unittest.TestCase):
    def test_letterCombinations_1(self):
        solution = Solution()
        self.assertEqual(["ad","ae","af","bd","be","bf","cd","ce","cf"], solution.letterCombinations('23'))

    def test_letterCombinations_withOne(self):
        solution = Solution()
        self.assertEqual([], solution.letterCombinations('111'))
        self.assertEqual([], solution.letterCombinations('123'))
        self.assertEqual([], solution.letterCombinations('213'))
        self.assertEqual([], solution.letterCombinations('231'))

    def test_letterCombinations_withZero(self):
        solution = Solution()
        self.assertEqual([], solution.letterCombinations('000'))
        self.assertEqual([], solution.letterCombinations('023'))
        self.assertEqual([], solution.letterCombinations('203'))
        self.assertEqual([], solution.letterCombinations('230'))
