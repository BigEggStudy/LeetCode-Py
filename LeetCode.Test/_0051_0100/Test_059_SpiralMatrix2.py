import unittest

import sys
sys.path.append('LeetCode/_0051_0100')
sys.path.append('LeetCode.Test')

from _059_SpiralMatrix2 import Solution

import AssertHelper

class Test_059_SpiralMatrix2(unittest.TestCase):
    def test_generateMatrix_1(self):
        solution = Solution()
        AssertHelper.assertArray2D([[1]], solution.generateMatrix(1))

    def test_generateMatrix_2(self):
        solution = Solution()
        AssertHelper.assertArray2D([
            [1,2],
            [4,3]
        ], solution.generateMatrix(2))

    def test_generateMatrix_3(self):
        solution = Solution()
        AssertHelper.assertArray2D([
            [1,2,3],
            [8,9,4],
            [7,6,5]
        ], solution.generateMatrix(3))

    def test_generateMatrix_4(self):
        solution = Solution()
        AssertHelper.assertArray2D([
            [ 1, 2, 3, 4],
            [12,13,14, 5],
            [11,16,15, 6],
            [10, 9, 8, 7]
        ], solution.generateMatrix(4))
