import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _048_RotateImage import Solution

import AssertHelper

class Test_048_RotateImage(unittest.TestCase):
    def test_rotate_oddLength(self):
        input = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        solution = Solution()
        solution.rotate(input)
        AssertHelper.assertArray2D([
            [7,4,1],
            [8,5,2],
            [9,6,3]
        ], input)

    def test_rotate_oddLength_2(self):
        input = [
            [ 1, 2, 3, 4, 5 ],
            [ 1, 2, 3, 4, 5 ],
            [ 1, 2, 3, 4, 5 ],
            [ 1, 2, 3, 4, 5 ],
            [ 1, 2, 3, 4, 5 ]
        ]
        solution = Solution()
        solution.rotate(input)
        AssertHelper.assertArray2D([
            [ 1, 1, 1, 1, 1 ],
            [ 2, 2, 2, 2, 2 ],
            [ 3, 3, 3, 3, 3 ],
            [ 4, 4, 4, 4, 4 ],
            [ 5, 5, 5, 5, 5 ]
        ], input)

    def test_rotate_evenLength(self):
        input = [
            [ 5, 1, 9,11],
            [ 2, 4, 8,10],
            [13, 3, 6, 7],
            [15,14,12,16]
        ]
        solution = Solution()
        solution.rotate(input)
        AssertHelper.assertArray2D([
            [15,13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7,10,11]
        ], input)

    def test_rotate_evenLength_2(self):
        input = [
            [ 1, 2, 3, 4, 5, 6 ],
            [ 1, 2, 3, 4, 5, 6 ],
            [ 1, 2, 3, 4, 5, 6 ],
            [ 1, 2, 3, 4, 5, 6 ],
            [ 1, 2, 3, 4, 5, 6 ],
            [ 1, 2, 3, 4, 5, 6 ]
        ]
        solution = Solution()
        solution.rotate(input)
        AssertHelper.assertArray2D([
            [ 1, 1, 1, 1, 1, 1 ],
            [ 2, 2, 2, 2, 2, 2 ],
            [ 3, 3, 3, 3, 3, 3 ],
            [ 4, 4, 4, 4, 4, 4 ],
            [ 5, 5, 5, 5, 5, 5 ],
            [ 6, 6, 6, 6, 6, 6 ]
        ], input)

    def test_rotate_empty(self):
        input = [[]]
        solution = Solution()
        solution.rotate(input)
        AssertHelper.assertArray2D([[]], input)

    def test_rotate_oneItem(self):
        input = [[1]]
        solution = Solution()
        solution.rotate(input)
        AssertHelper.assertArray2D([[1]], input)
