import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _024_SwapNodesInPairs import Solution

import TestHelper, AssertHelper

class Test_024_SwapNodesInPairs(unittest.TestCase):
    def test_swapPairs(self):
        link = TestHelper.generateLinkList([1, 2, 3, 4])

        solution = Solution()
        result = solution.swapPairs(link)
        AssertHelper.assertLinkList([2, 1, 4, 3], result)

    def test_swapPairs_empty(self):
        solution = Solution()
        result = solution.swapPairs(None)
        self.assertEqual(None, result)

    def test_swapPairs_onlyOne(self):
        link = TestHelper.generateLinkList([1])

        solution = Solution()
        result = solution.swapPairs(link)
        AssertHelper.assertLinkList([1], result)

    def test_swapPairs_onlyTwo(self):
        link = TestHelper.generateLinkList([1, 2])

        solution = Solution()
        result = solution.swapPairs(link)
        AssertHelper.assertLinkList([2, 1], result)

    def test_swapPairs_Odd(self):
        link = TestHelper.generateLinkList([1, 2, 3])

        solution = Solution()
        result = solution.swapPairs(link)
        AssertHelper.assertLinkList([2, 1, 3], result)
