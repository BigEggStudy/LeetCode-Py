import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _027_RemoveElement import Solution

import AssertHelper

class Test_027_RemoveElement(unittest.TestCase):
    def test_removeElement(self):
        nums = [3, 2, 2, 3]

        solution = Solution()
        result = solution.removeElement(nums, 3)
        self.assertEqual(2, result)
        AssertHelper.assertArray([2, 2], nums, True)

    def test_removeElement_1(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]

        solution = Solution()
        result = solution.removeElement(nums, 2)
        self.assertEqual(5, result)
        AssertHelper.assertArray([0, 1, 3, 0, 4], nums, True)

    def test_removeElement_empty(self):
        nums = []

        solution = Solution()
        result = solution.removeElement(nums, 2)
        self.assertEqual(0, result)
        AssertHelper.assertArray([], nums, True)

    def test_removeElement_onlyOne(self):
        nums = [1]

        solution = Solution()
        result = solution.removeElement(nums, 2)
        self.assertEqual(1, result)
        AssertHelper.assertArray([1], nums, True)

    def test_removeElement_onlyOne_removed(self):
        nums = [1]

        solution = Solution()
        result = solution.removeElement(nums, 1)
        self.assertEqual(0, result)
        AssertHelper.assertArray([], nums, True)
