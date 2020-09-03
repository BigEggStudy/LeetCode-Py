import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _052_NQueens2 import Solution

class Test_052_NQueens2(unittest.TestCase):
    def test_totalNQueens_1(self):
        solution = Solution()
        result = solution.totalNQueens(1)
        self.assertEqual(1, result)

    def test_totalNQueens_2(self):
        solution = Solution()
        result = solution.totalNQueens(2)
        self.assertEqual(0, result)

    def test_totalNQueens_3(self):
        solution = Solution()
        result = solution.totalNQueens(3)
        self.assertEqual(0, result)

    def test_totalNQueens_4(self):
        solution = Solution()
        result = solution.totalNQueens(4)
        self.assertEqual(2, result)

    def test_totalNQueens_5(self):
        solution = Solution()
        result = solution.totalNQueens(5)
        self.assertEqual(10, result)
