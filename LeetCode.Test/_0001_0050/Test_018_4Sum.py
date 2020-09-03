import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _018_4Sum import Solution

class Test_018_4Sum(unittest.TestCase):
    def test_fourSum_have(self):
        solution = Solution()
        self.assertEqual([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], solution.fourSum([1, 0, -1, 0, -2, 2], 0))
        self.assertEqual([[-1,  0, 0, 1]], solution.fourSum([1, 0, -1, 0], 0))

    def test_fourSum_have_2(self):
        solution = Solution()
        self.assertEqual([[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], solution.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))

    def test_fourSum_smallArray(self):
        solution = Solution()
        self.assertEqual([], solution.fourSum([1, 0, -1], 0))
        self.assertEqual([], solution.fourSum([1, 0], 0))
        self.assertEqual([], solution.fourSum([1], 0))
        self.assertEqual([], solution.fourSum([], 0))

    def test_fourSum_notHave(self):
        solution = Solution()
        self.assertEqual([], solution.fourSum([1, 0, -1, 3], 2))
        self.assertEqual([], solution.fourSum([1, 0, -1, 3], 1))

    def test_fourSum_sum_smaller(self):
        solution = Solution()
        self.assertEqual([], solution.fourSum([-1, 0, 1, 2], 3))

    def test_fourSum_sum_larger(self):
        solution = Solution()
        self.assertEqual([], solution.fourSum([-1, 0, 1, 2], 1))
