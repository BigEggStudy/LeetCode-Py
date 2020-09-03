import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _037_SudokuSolver import Solution

import AssertHelper

class Test_037_SudokuSolver(unittest.TestCase):
    def test_solveSudoku(self):
        input = [
            [ '5','3','.','.','7','.','.','.','.' ],
            [ '6','.','.','1','9','5','.','.','.' ],
            [ '.','9','8','.','.','.','.','6','.' ],
            [ '8','.','.','.','6','.','.','.','3' ],
            [ '4','.','.','8','.','3','.','.','1' ],
            [ '7','.','.','.','2','.','.','.','6' ],
            [ '.','6','.','.','.','.','2','8','.' ],
            [ '.','.','.','4','1','9','.','.','5' ],
            [ '.','.','.','.','8','.','.','7','9' ]
        ]
        solution = Solution()
        solution.solveSudoku(input)

        AssertHelper.assertArray([
            [ '5','3','4','6','7','8','9','1','2' ],
            [ '6','7','2','1','9','5','3','4','8' ],
            [ '1','9','8','3','4','2','5','6','7' ],
            [ '8','5','9','7','6','1','4','2','3' ],
            [ '4','2','6','8','5','3','7','9','1' ],
            [ '7','1','3','9','2','4','8','5','6' ],
            [ '9','6','1','5','3','7','2','8','4' ],
            [ '2','8','7','4','1','9','6','3','5' ],
            [ '3','4','5','2','8','6','1','7','9' ]
        ], input)

    def test_solveSudoku_2(self):
        input = [
            [ ".",".","9","7","4","8",".",".","." ],
            [ "7",".",".",".",".",".",".",".","." ],
            [ ".","2",".","1",".","9",".",".","." ],
            [ ".",".","7",".",".",".","2","4","." ],
            [ ".","6","4",".","1",".","5","9","." ],
            [ ".","9","8",".",".",".","3",".","." ],
            [ ".",".",".","8",".","3",".","2","." ],
            [ ".",".",".",".",".",".",".",".","6" ],
            [ ".",".",".","2","7","5","9",".","." ]
        ]
        solution = Solution()
        solution.solveSudoku(input)

        AssertHelper.assertArray([
            [ "5","1","9","7","4","8","6","3","2" ],
            [ "7","8","3","6","5","2","4","1","9" ],
            [ "4","2","6","1","3","9","8","7","5" ],
            [ "3","5","7","9","8","6","2","4","1" ],
            [ "2","6","4","3","1","7","5","9","8" ],
            [ "1","9","8","5","2","4","3","6","7" ],
            [ "9","7","5","8","6","3","1","2","4" ],
            [ "8","3","2","4","9","1","7","5","6" ],
            [ "6","4","1","2","7","5","9","8","3" ]
        ], input)