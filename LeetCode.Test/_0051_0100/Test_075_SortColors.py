import unittest

import sys
sys.path.append('LeetCode/_0051_0100')
sys.path.append('LeetCode.Test')

from _075_SortColors import Solution
import AssertHelper

class Test_075_SortColors(unittest.TestCase):
    def test_sortColors_1(self):
        solution = Solution()
        input = [2,0,2,1,1,0]
        solution.sortColors(input)
        AssertHelper.assertArray([0,0,1,1,2,2], input)

    def test_sortColors_2(self):
        solution = Solution()
        input = [2,2,0,0,1,1]
        solution.sortColors(input)
        AssertHelper.assertArray([0,0,1,1,2,2], input)

    def test_sortColors_3(self):
        solution = Solution()
        input = [2,2,1,1,0,0]
        solution.sortColors(input)
        AssertHelper.assertArray([0,0,1,1,2,2], input)

    def test_sortColors_4(self):
        solution = Solution()
        input = [0,0,0,0,0,0]
        solution.sortColors(input)
        AssertHelper.assertArray([0,0,0,0,0,0], input)

    def test_sortColors_5(self):
        solution = Solution()
        input = [1,1,1,1,1,1]
        solution.sortColors(input)
        AssertHelper.assertArray([1,1,1,1,1,1], input)

    def test_sortColors_6(self):
        solution = Solution()
        input = [2,2,2,2,2,2]
        solution.sortColors(input)
        AssertHelper.assertArray([2,2,2,2,2,2], input)
