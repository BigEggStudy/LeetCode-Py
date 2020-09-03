import unittest

import sys
sys.path.append('LeetCode/_0051_0100')
sys.path.append('LeetCode.Test')

from _056_MergeIntervals import Solution

import AssertHelper

class Test_056_MergeIntervals(unittest.TestCase):
    def test_merge_1(self):
        solution = Solution()
        result = solution.merge([[1,3],[2,6],[8,10],[15,18]])
        AssertHelper.assertArray2D([[1,6],[8,10],[15,18]], result)

    def test_merge_2(self):
        solution = Solution()
        result = solution.merge([[1,4],[4,5]])
        AssertHelper.assertArray2D([[1,5]], result)

    def test_merge_notOrder(self):
        solution = Solution()
        result = solution.merge([[1,4],[0,5]])
        AssertHelper.assertArray2D([[0,5]], result)
