import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _031_NextPermutation import Solution

import AssertHelper

class Test_031_NextPermutation(unittest.TestCase):
    def test_nextPermutation_1(self):
        nums = [1, 2, 3]
        solution = Solution()
        solution.nextPermutation(nums)
        AssertHelper.assertArray([1, 3, 2], nums)

    def test_nextPermutation_2(self):
        nums = [1, 3, 2]
        solution = Solution()
        solution.nextPermutation(nums)
        AssertHelper.assertArray([2, 1, 3], nums)

    def test_nextPermutation_3(self):
        nums = [3, 2, 1]
        solution = Solution()
        solution.nextPermutation(nums)
        AssertHelper.assertArray([1, 2, 3], nums)

    def test_nextPermutation_4(self):
        nums = [1, 1, 5]
        solution = Solution()
        solution.nextPermutation(nums)
        AssertHelper.assertArray([1, 5, 1], nums)

    def test_nextPermutation_fullSet(self):
        nums = [1, 2, 3, 4]
        solution = Solution()

        solution.nextPermutation(nums)
        AssertHelper.assertArray([1, 2, 4, 3], nums)

        solution.nextPermutation(nums)
        AssertHelper.assertArray([ 1, 3, 2, 4 ], nums)

        solution.nextPermutation(nums)
        AssertHelper.assertArray([ 1, 3, 4, 2 ], nums)

        solution.nextPermutation(nums)
        AssertHelper.assertArray([1, 4, 2, 3], nums)

        solution.nextPermutation(nums)
        AssertHelper.assertArray([1, 4, 3, 2], nums)

        solution.nextPermutation(nums)
        AssertHelper.assertArray([2, 1, 3, 4], nums)

    def test_nextPermutation_empty(self):
        nums = []
        solution = Solution()
        solution.nextPermutation(nums)
        AssertHelper.assertArray([], nums)

    def test_nextPermutation_onlyOneItem(self):
        nums = [1]
        solution = Solution()
        solution.nextPermutation(nums)
        AssertHelper.assertArray([1], nums)