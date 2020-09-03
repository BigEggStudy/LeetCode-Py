import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _026_RemoveDuplicatesFromSortedArray import Solution

import AssertHelper

class Test_026_RemoveDuplicatesFromSortedArray(unittest.TestCase):
    def test_removeDuplicates(self):
        nums = [1, 1, 2]

        solution = Solution()
        result = solution.removeDuplicates(nums)
        self.assertEqual(2, result)
        AssertHelper.assertArray([1, 2], nums, True)

    def test_removeDuplicates_1(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

        solution = Solution()
        result = solution.removeDuplicates(nums)
        self.assertEqual(5, result)
        AssertHelper.assertArray([0, 1, 2, 3, 4], nums, True)

    def test_removeDuplicates_empty(self):
        nums = []

        solution = Solution()
        result = solution.removeDuplicates(nums)
        self.assertEqual(0, result)
        AssertHelper.assertArray([], nums, True)

    def test_removeDuplicates_onlyOne(self):
        nums = [1]

        solution = Solution()
        result = solution.removeDuplicates(nums)
        self.assertEqual(1, result)
        AssertHelper.assertArray([1], nums, True)
