import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _063_UniquePaths2 import Solution

class Test_063_UniquePaths2(unittest.TestCase):
    def test_uniquePathsWithObstacles(self):
        solution = Solution()
        self.assertEqual(2, solution.uniquePathsWithObstacles([
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]))

    def test_uniquePathsWithObstacles_2(self):
        solution = Solution()
        self.assertEqual(3, solution.uniquePathsWithObstacles([
            [0,1,0],
            [0,0,0],
            [0,0,0]
        ]))

    def test_uniquePathsWithObstacles_startWithObstacle(self):
        solution = Solution()
        self.assertEqual(0, solution.uniquePathsWithObstacles([
            [1,0,0],
            [0,0,0],
            [0,0,0]
        ]))

    def test_uniquePathsWithObstacles_oneRow(self):
        solution = Solution()
        self.assertEqual(1, solution.uniquePathsWithObstacles([[0,0]]))

    def test_uniquePathsWithObstacles_oneColumn(self):
        solution = Solution()
        self.assertEqual(1, solution.uniquePathsWithObstacles([
            [0],
            [0]
        ]))
