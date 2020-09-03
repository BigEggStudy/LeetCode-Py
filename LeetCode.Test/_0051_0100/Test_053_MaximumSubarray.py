import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _053_MaximumSubarray import Solution

class Test_053_MaximumSubarray(unittest.TestCase):
    def test_maxSubArray_1(self):
        solution = Solution()
        result = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        self.assertEqual(6, result)

    def test_maxSubArray_2(self):
        solution = Solution()
        result = solution.maxSubArray([-2])
        self.assertEqual(-2, result)

    def test_maxSubArray_3(self):
        solution = Solution()
        result = solution.maxSubArray([-2, -1])
        self.assertEqual(-1, result)

    def test_maxSubArray_4(self):
        solution = Solution()
        result = solution.maxSubArray([1,2,3,4])
        self.assertEqual(10, result)

    def test_maxSubArray_5(self):
        solution = Solution()
        result = solution.maxSubArray([5,-6])
        self.assertEqual(5, result)

    def test_maxSubArray_emptyArray(self):
        solution = Solution()
        result = solution.maxSubArray([])
        self.assertEqual(0, result)
