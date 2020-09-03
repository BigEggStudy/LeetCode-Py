import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _023_MergeKSortedLists import Solution

import TestHelper, AssertHelper

class Test_023_MergeKSortedLists(unittest.TestCase):
    def test_mergeKLists(self):
        link1 = TestHelper.generateLinkList([1, 2, 4])
        link2 = TestHelper.generateLinkList([1, 3, 4])

        solution = Solution()
        result = solution.mergeKLists([link1, link2])
        AssertHelper.assertLinkList([1, 1, 2, 3, 4, 4], result)

    def test_mergeKLists_2(self):
        link1 = TestHelper.generateLinkList([1, 4, 5])
        link2 = TestHelper.generateLinkList([1, 3, 4])
        link3 = TestHelper.generateLinkList([2, 6])

        solution = Solution()
        result = solution.mergeKLists([link1, link2, link3])
        AssertHelper.assertLinkList([1, 1, 2, 3, 4, 4, 5, 6], result)

    def test_mergeKLists_oneLonger(self):
        link1 = TestHelper.generateLinkList([1, 2, 4, 6, 7, 8])
        link2 = TestHelper.generateLinkList([1, 3, 4])

        solution = Solution()
        result = solution.mergeKLists([link1, link2])
        AssertHelper.assertLinkList([1, 1, 2, 3, 4, 4, 6, 7, 8], result)

    def test_mergeKLists_oneLonger_2(self):
        link1 = TestHelper.generateLinkList([1, 3, 4])
        link2 = TestHelper.generateLinkList([1, 2, 4, 6, 7, 8])

        solution = Solution()
        result = solution.mergeKLists([link1, link2])
        AssertHelper.assertLinkList([1, 1, 2, 3, 4, 4, 6, 7, 8], result)

    def test_mergeKLists_oneEmpty(self):
        link1 = TestHelper.generateLinkList([1, 2, 4])
        link2 = TestHelper.generateLinkList([])

        solution = Solution()
        result = solution.mergeKLists([link1, link2])
        AssertHelper.assertLinkList([1, 2, 4], result)

    def test_mergeKLists_oneEmpty_2(self):
        link1 = TestHelper.generateLinkList([])
        link2 = TestHelper.generateLinkList([1, 2, 4])

        solution = Solution()
        result = solution.mergeKLists([link1, link2])
        AssertHelper.assertLinkList([1, 2, 4], result)
