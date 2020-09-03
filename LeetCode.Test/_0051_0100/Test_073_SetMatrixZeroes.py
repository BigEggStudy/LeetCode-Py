import unittest

import sys
sys.path.append('LeetCode/_0051_0100')
sys.path.append('LeetCode.Test')

from _073_SetMatrixZeroes import Solution
import AssertHelper

class Test_073_SetMatrixZeroes(unittest.TestCase):
    def test_setZeroes_1(self):
        input_data = [
            [1,1,1],
            [1,0,1],
            [1,1,1]
        ]
        solution = Solution()
        solution.setZeroes(input_data)
        AssertHelper.assertArray2D([
            [1,0,1],
            [0,0,0],
            [1,0,1]
        ], input_data)

    def test_setZeroes_2(self):
        input_data = [
            [0,1,2,0],
            [3,4,5,2],
            [1,3,1,5]
        ]
        solution = Solution()
        solution.setZeroes(input_data)
        print(input_data)
        AssertHelper.assertArray2D([
            [0,0,0,0],
            [0,4,5,0],
            [0,3,1,0]
        ], input_data)

    def test_setZeroes_3(self):
        input_data = [
            [0,1],
            [3,0]
        ]
        solution = Solution()
        solution.setZeroes(input_data)
        print(input_data)
        AssertHelper.assertArray2D([
            [0,0],
            [0,0]
        ], input_data)

    def test_setZeroes_4(self):
        input_data = [
            [0,1,2,5],
            [3,4,5,2],
            [1,3,0,5]
        ]
        solution = Solution()
        solution.setZeroes(input_data)
        print(input_data)
        AssertHelper.assertArray2D([
            [0,0,0,0],
            [0,4,0,2],
            [0,0,0,0]
        ], input_data)

    def test_setZeroes_oneItem(self):
        input_data = [[1]]
        solution = Solution()
        solution.setZeroes(input_data)
        print(input_data)
        AssertHelper.assertArray2D([[1]], input_data)

    def test_setZeroes_oneItem_2(self):
        input_data = [[0]]
        solution = Solution()
        solution.setZeroes(input_data)
        print(input_data)
        AssertHelper.assertArray2D([[0]], input_data)
