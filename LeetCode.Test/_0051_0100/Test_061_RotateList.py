import unittest

import sys
sys.path.append('LeetCode/_0051_0100')
sys.path.append('LeetCode.Test')

from _061_RotateList import Solution

import TestHelper, AssertHelper

class Test_061_RotateList(unittest.TestCase):
    def test_rotateRight(self):
        link = TestHelper.generateLinkList([1, 2, 3, 4, 5])
        solution = Solution()
        result = solution.rotateRight(link, 2)
        AssertHelper.assertLinkList([4, 5, 1, 2, 3], result)

    def test_rotateRight_rollover(self):
        link = TestHelper.generateLinkList([0, 1, 2])
        solution = Solution()
        result = solution.rotateRight(link, 4)
        AssertHelper.assertLinkList([2, 0, 1], result)
