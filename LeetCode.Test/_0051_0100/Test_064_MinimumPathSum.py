import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _064_MinimumPathSum import Solution

class Test_064_MinimumPathSum(unittest.TestCase):
    def test_minPathSum(self):
        solution = Solution()
        self.assertEqual(7, solution.minPathSum([
            [1,3,1],
            [1,5,1],
            [4,2,1]
        ]))

    def test_minPathSum_2(self):
        solution = Solution()
        self.assertEqual(8, solution.minPathSum([
            [1,3],
            [1,5],
            [4,2]
        ]))

    def test_minPathSum_3(self):
        solution = Solution()
        self.assertEqual(6, solution.minPathSum([
            [1,3,1],
            [1,5,1]
        ]))

    def test_minPathSum_4(self):
        solution = Solution()
        self.assertEqual(6, solution.minPathSum([
            [1,3],
            [2,2],
            [5,1]
        ]))

    def test_minPathSum_5(self):
        solution = Solution()
        self.assertEqual(6, solution.minPathSum([
            [1,2,5],
            [3,2,1]
        ]))

    def test_minPathSum_oneRow(self):
        solution = Solution()
        self.assertEqual(5, solution.minPathSum([
            [1,3,1]
        ]))

    def test_minPathSum_oneColumn(self):
        solution = Solution()
        self.assertEqual(5, solution.minPathSum([
            [1],
            [3],
            [1]
        ]))

    def test_minPathSum_oneItem(self):
        solution = Solution()
        self.assertEqual(1, solution.minPathSum([
            [1]
        ]))

    def test_minPathSum_empty(self):
        solution = Solution()
        self.assertEqual(0, solution.minPathSum([]))
