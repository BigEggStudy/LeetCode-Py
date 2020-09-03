import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _036_ValidSudoku import Solution

import AssertHelper

class Test_036_ValidSudoku(unittest.TestCase):
    def test_isValidSudoku(self):
        input = [
            [ '5','3','.','.','7','.','.','.','.'],
            [ '6','.','.','1','9','5','.','.','.'],
            [ '.','9','8','.','.','.','.','6','.'],
            [ '8','.','.','.','6','.','.','.','3'],
            [ '4','.','.','8','.','3','.','.','1'],
            [ '7','.','.','.','2','.','.','.','6'],
            [ '.','6','.','.','.','.','2','8','.'],
            [ '.','.','.','4','1','9','.','.','5'],
            [ '.','.','.','.','8','.','.','7','9']
        ]
        solution = Solution()
        self.assertTrue(solution.isValidSudoku(input))

    def test_isValidSudoku_ColumnNotValid(self):
        input = [
            [ '5','3','.','.','7','.','.','.','.'],
            [ '6','.','.','1','9','5','.','.','.'],
            [ '.','9','8','.','.','.','.','6','.'],
            [ '8','.','.','.','6','.','.','.','3'],
            [ '4','.','.','8','.','3','.','.','1'],
            [ '7','.','.','.','2','.','.','.','6'],
            [ '.','6','.','.','.','.','2','8','.'],
            [ '.','.','.','4','1','9','.','6','5'],
            [ '.','.','.','.','8','.','.','7','9']
        ]
        solution = Solution()
        self.assertFalse(solution.isValidSudoku(input))

    def test_isValidSudoku_RowNotValid(self):
        input = [
            [ '5','3','.','.','7','.','.','.','.'],
            [ '6','.','.','1','9','5','.','.','.'],
            [ '.','9','8','.','.','.','.','6','.'],
            [ '8','.','.','.','6','.','.','.','3'],
            [ '4','.','.','8','.','3','.','3','1'],
            [ '7','.','.','.','2','.','.','.','6'],
            [ '.','6','.','.','.','.','2','8','.'],
            [ '.','.','.','4','1','9','.','.','5'],
            [ '.','.','.','.','8','.','.','7','9']
        ]
        solution = Solution()
        self.assertFalse(solution.isValidSudoku(input))

    def test_isValidSudoku_SqureNotValid(self):
        input = [
            [ '5','3','.','.','7','.','.','.','.'],
            [ '6','.','.','1','9','5','.','.','.'],
            [ '.','9','8','5','.','.','.','6','.'],
            [ '8','.','.','.','6','.','.','.','3'],
            [ '4','.','.','8','.','3','.','.','1'],
            [ '7','.','.','.','2','.','.','.','6'],
            [ '.','6','.','.','.','.','2','8','.'],
            [ '.','.','.','4','1','9','.','.','5'],
            [ '.','.','.','.','8','.','.','7','9']
        ]
        solution = Solution()
        self.assertFalse(solution.isValidSudoku(input))
