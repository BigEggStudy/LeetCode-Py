import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _019_RemoveNthNodeFromEndOfList import Solution

import TestHelper, AssertHelper

class Test_019_RemoveNthNodeFromEndOfList(unittest.TestCase):
    def test_removeNthFromEnd(self):
        link = TestHelper.generateLinkList([1, 2, 3, 4, 5])

        solution = Solution()
        result = solution.removeNthFromEnd(link, 2)

        AssertHelper.assertLinkList([1, 2, 3, 5], result)

    def test_removeNthFromEnd_head(self):
        link = TestHelper.generateLinkList([1, 2, 3, 4, 5])

        solution = Solution()
        result = solution.removeNthFromEnd(link, 5)

        AssertHelper.assertLinkList([2, 3, 4, 5], result)

    def test_removeNthFromEnd_end(self):
        link = TestHelper.generateLinkList([1, 2, 3, 4, 5])

        solution = Solution()
        result = solution.removeNthFromEnd(link, 1)

        AssertHelper.assertLinkList([1, 2, 3, 4], result)
