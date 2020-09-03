import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _025_ReverseNodesInKGroup import Solution

import TestHelper, AssertHelper

class Test_025_ReverseNodesInKGroup(unittest.TestCase):
    def test_reverseKGroup(self):
        link = TestHelper.generateLinkList([1, 2, 3, 4])

        solution = Solution()
        result = solution.reverseKGroup(link, 2)
        AssertHelper.assertLinkList([2, 1, 4, 3], result)

    def test_reverseKGroup_empty(self):
        solution = Solution()
        result = solution.reverseKGroup(None, 0)
        self.assertEqual(None, result)

    def test_reverseKGroup_onlyOne(self):
        link = TestHelper.generateLinkList([1])

        solution = Solution()
        result = solution.reverseKGroup(link, 2)
        AssertHelper.assertLinkList([1], result)

    def test_reverseKGroup_onlyTwo(self):
        link = TestHelper.generateLinkList([1, 2])

        solution = Solution()
        result = solution.reverseKGroup(link, 2)
        AssertHelper.assertLinkList([2, 1], result)

    def test_reverseKGroup_Odd(self):
        link = TestHelper.generateLinkList([1, 2, 3])

        solution = Solution()
        result = solution.reverseKGroup(link, 2)
        AssertHelper.assertLinkList([2, 1, 3], result)

    def test_reverseKGroup_noswap(self):
        link = TestHelper.generateLinkList([1, 2, 3, 4])

        solution = Solution()
        result = solution.reverseKGroup(link, 1)
        AssertHelper.assertLinkList([1, 2, 3, 4], result)

    def test_reverseKGroup_moreswap(self):
        link = TestHelper.generateLinkList([1, 2, 3, 4, 5])

        solution = Solution()
        result = solution.reverseKGroup(link, 3)
        AssertHelper.assertLinkList([3, 2, 1, 4, 5], result)
