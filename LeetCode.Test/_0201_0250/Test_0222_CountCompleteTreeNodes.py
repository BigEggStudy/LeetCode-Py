import unittest

import sys
sys.path.append('LeetCode/_0201_0250')
sys.path.append('LeetCode.Test')

from _0222_CountCompleteTreeNodes import Solution
from TreeNode import TreeNode
import AssertHelper, TestHelper

class Test_0222_CountCompleteTreeNodes(unittest.TestCase):
    def test_countNodes(self):
        solution = Solution()
        self.assertEqual(2, solution.countNodes(TestHelper.generateTree([ 1, 2 ])))
        self.assertEqual(3, solution.countNodes(TestHelper.generateTree([ 1, 2, 3 ])))
        self.assertEqual(4, solution.countNodes(TestHelper.generateTree([ 1, 2, 3, 4 ])))
        self.assertEqual(5, solution.countNodes(TestHelper.generateTree([ 1, 2, 3, 4, 5 ])))
        self.assertEqual(6, solution.countNodes(TestHelper.generateTree([ 1, 2, 3, 4, 5, 6 ])))
        self.assertEqual(7, solution.countNodes(TestHelper.generateTree([ 1, 2, 3, 4, 5, 6, 7 ])))

    def test_countNodes_None(self):
        solution = Solution()
        self.assertEqual(0, solution.countNodes(None))

    def test_countNodes_just_root(self):
        solution = Solution()
        self.assertEqual(1, solution.countNodes(TestHelper.generateTree([ 1 ])))
