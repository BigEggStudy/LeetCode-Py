import unittest

import sys
sys.path.append('LeetCode/_0051_0100')
sys.path.append('LeetCode.Test')

from _074_SearchA2DMatrix import Solution

class Test_074_SearchA2DMatrix(unittest.TestCase):
    def test_searchMatrix_1(self):
        solution = Solution()
        self.assertTrue(solution.searchMatrix([
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ], 3))

    def test_searchMatrix_2(self):
        solution = Solution()
        self.assertFalse(solution.searchMatrix([
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ], 13))

    def test_searchMatrix_3(self):
        solution = Solution()
        self.assertTrue(solution.searchMatrix([
            [1],
            [10],
            [23]
        ], 10))

    def test_searchMatrix_4(self):
        solution = Solution()
        self.assertFalse(solution.searchMatrix([
            [1],
            [10],
            [23]
        ], 13))
