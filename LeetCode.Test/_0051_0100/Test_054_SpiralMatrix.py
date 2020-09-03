import unittest

import sys
sys.path.append('LeetCode/_0051_0100')
sys.path.append('LeetCode.Test')

from _054_SpiralMatrix import Solution

import AssertHelper

class Test_054_SpiralMatrix(unittest.TestCase):
    def test_spiralOrder_1(self):
        solution = Solution()
        result = solution.spiralOrder([
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ])
        print(result)
        AssertHelper.assertArray([1,2,3,6,9,8,7,4,5], result)

    def test_spiralOrder_2(self):
        solution = Solution()
        result = solution.spiralOrder([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9,10,11,12]
        ])
        print(result)
        AssertHelper.assertArray([1,2,3,4,8,12,11,10,9,5,6,7], result)

    def test_spiralOrder_3(self):
        solution = Solution()
        result = solution.spiralOrder([
            [ 1, 2, 3],
            [ 4, 5, 6],
            [ 7, 8, 9],
            [10,11,12]
        ])
        print(result)
        AssertHelper.assertArray([1,2,3,6,9,12,11,10,7,4,5,8], result)

    def test_spiralOrder_4(self):
        solution = Solution()
        result = solution.spiralOrder([
            [ 1, 2, 3, 4],
            [ 5, 6, 7, 8],
            [ 9,10,11,12],
            [13,14,15,16]
        ])
        print(result)
        AssertHelper.assertArray([1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10], result)

    def test_spiralOrder_onlyOne(self):
        solution = Solution()
        result = solution.spiralOrder([
            [1]
        ])
        print(result)
        AssertHelper.assertArray([1], result)

    def test_spiralOrder_onlyTwo(self):
        solution = Solution()
        result = solution.spiralOrder([
            [1,2]
        ])
        print(result)
        AssertHelper.assertArray([1,2], result)

    def test_spiralOrder_onlyTwo_2(self):
        solution = Solution()
        result = solution.spiralOrder([
            [1],
            [2]
        ])
        print(result)
        AssertHelper.assertArray([1,2], result)

    def test_spiralOrder_twoByThree(self):
        solution = Solution()
        result = solution.spiralOrder([
            [1,2,3],
            [4,5,6]
        ])
        print(result)
        AssertHelper.assertArray([1,2,3,6,5,4], result)

    def test_spiralOrder_threeByTwo(self):
        solution = Solution()
        result = solution.spiralOrder([
            [1,2],
            [3,4],
            [5,6]
        ])
        print(result)
        AssertHelper.assertArray([1,2,4,6,5,3], result)

    def test_spiralOrder_oneLine(self):
        solution = Solution()
        result = solution.spiralOrder([
            [1,2,3]
        ])
        print(result)
        AssertHelper.assertArray([1,2,3], result)

    def test_spiralOrder_oneLine_2(self):
        solution = Solution()
        result = solution.spiralOrder([
            [1],
            [2],
            [3]
        ])
        print(result)
        AssertHelper.assertArray([1,2,3], result)
