import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _034_SearchForARange import Solution

import AssertHelper

class Test_034_SearchForARange(unittest.TestCase):
    def test_searchRange(self):
        nums = [5, 7, 7, 8, 8, 10]
        solution = Solution()
        AssertHelper.assertArray([3, 4], solution.searchRange(nums, 8))
        AssertHelper.assertArray([0, 0], solution.searchRange(nums, 5))
        AssertHelper.assertArray([1, 2], solution.searchRange(nums, 7))
        AssertHelper.assertArray([5, 5], solution.searchRange(nums, 10))

    def test_searchRange_notFound(self):
        nums = [5, 7, 7, 8, 8, 10]
        solution = Solution()
        AssertHelper.assertArray([-1, -1], solution.searchRange(nums, 6))
        AssertHelper.assertArray([-1, -1], solution.searchRange(nums, 9))
        AssertHelper.assertArray([-1, -1], solution.searchRange(nums, 11))
