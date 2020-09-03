import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _021_MergeTwoSortedLists import Solution

import TestHelper, AssertHelper

class Test_021_MergeTwoSortedLists(unittest.TestCase):
    def test_mergeTwoLists(self):
        link1 = TestHelper.generateLinkList([1, 2, 4])
        link2 = TestHelper.generateLinkList([1, 3, 4])

        solution = Solution()
        result = solution.mergeTwoLists(link1, link2)
        AssertHelper.assertLinkList([1, 1, 2, 3, 4, 4], result)

    def test_mergeTwoLists_oneLonger(self):
        link1 = TestHelper.generateLinkList([1, 2, 4, 6, 7, 8])
        link2 = TestHelper.generateLinkList([1, 3, 4])

        solution = Solution()
        result = solution.mergeTwoLists(link1, link2)
        AssertHelper.assertLinkList([1, 1, 2, 3, 4, 4, 6, 7, 8], result)

    def test_mergeTwoLists_oneLonger_2(self):
        link1 = TestHelper.generateLinkList([1, 3, 4])
        link2 = TestHelper.generateLinkList([1, 2, 4, 6, 7, 8])

        solution = Solution()
        result = solution.mergeTwoLists(link1, link2)
        AssertHelper.assertLinkList([1, 1, 2, 3, 4, 4, 6, 7, 8], result)

    def test_mergeTwoLists_oneEmpty(self):
        link1 = TestHelper.generateLinkList([1, 2, 4])
        link2 = TestHelper.generateLinkList([])

        solution = Solution()
        result = solution.mergeTwoLists(link1, link2)
        AssertHelper.assertLinkList([1, 2, 4], result)

    def test_mergeTwoLists_oneEmpty_2(self):
        link1 = TestHelper.generateLinkList([])
        link2 = TestHelper.generateLinkList([1, 2, 4])

        solution = Solution()
        result = solution.mergeTwoLists(link1, link2)
        AssertHelper.assertLinkList([1, 2, 4], result)
