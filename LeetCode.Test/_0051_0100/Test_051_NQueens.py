import unittest

import sys
sys.path.append('LeetCode/_0051_0100')
sys.path.append('LeetCode.Test')

from _051_NQueens import Solution

import AssertHelper

class Test_051_NQueens(unittest.TestCase):
    def test_solveNQueens_1(self):
        solution = Solution()
        result = solution.solveNQueens(1)
        AssertHelper.assertArray2D(['Q'], result)

    def test_solveNQueens_2(self):
        solution = Solution()
        result = solution.solveNQueens(2)
        AssertHelper.assertArray2D([], result)

    def test_solveNQueens_3(self):
        solution = Solution()
        result = solution.solveNQueens(3)
        AssertHelper.assertArray2D([], result)

    def test_solveNQueens_4(self):
        solution = Solution()
        result = solution.solveNQueens(4)
        AssertHelper.assertArray2D([
            ['.Q..','...Q','Q...','..Q.'],
            ['..Q.','Q...','...Q','.Q..']
        ], result)

    def test_solveNQueens_5(self):
        solution = Solution()
        result = solution.solveNQueens(5)
        AssertHelper.assertArray2D([
            ['Q....','..Q..','....Q','.Q...','...Q.'],
            ['Q....','...Q.','.Q...','....Q','..Q..'],
            ['.Q...','...Q.','Q....','..Q..','....Q'],
            ['.Q...','....Q','..Q..','Q....','...Q.'],
            ['..Q..','Q....','...Q.','.Q...','....Q'],
            ['..Q..','....Q','.Q...','...Q.','Q....'],
            ['...Q.','Q....','..Q..','....Q','.Q...'],
            ['...Q.','.Q...','....Q','..Q..','Q....'],
            ['....Q','.Q...','...Q.','Q....','..Q..'],
            ['....Q','..Q..','Q....','...Q.','.Q...']
        ], result)
