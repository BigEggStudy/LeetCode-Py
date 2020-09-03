import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _015_3Sum import Solution

class Test_015_3Sum(unittest.TestCase):
    def test_threeSum_have(self):
        solution = Solution()
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], solution.threeSum([-1, 0, 1, 2, -1, -4]))

    def test_threeSum_have_2(self):
        solution = Solution()
        self.assertEqual([[-10, 4, 6], [-8, -1, 9], [-6, -3, 9], [-6, -2, 8], [-5, -4, 9], [-5, -3, 8], [-5, -1, 6], [-4, -2, 6], [-3, -1, 4], [-2, -2, 4]],
                         solution.threeSum([6, -5, -6, -1, -2, 8, -1, 4, -10, -8, -10, -2, -4, -1, -8, -2, 8, 9, -5, -2, -8, -9, -3, -5]))

    def test_threeSum_have_3(self):
        solution = Solution()
        self.assertEqual([[-5, 1, 4], [-4, 0, 4], [-4, 1, 3], [-2, -2, 4], [0, 0, 0], [1, 1, -2]],
                         solution.threeSum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]))

    def test_threeSum_have_all_zero(self):
        solution = Solution()
        self.assertEqual([[0, 0, 0]], solution.threeSum([0, 0, 0]))

    def test_threeSum_have_all_zero_2(self):
        solution = Solution()
        self.assertEqual([[0, 0, 0]], solution.threeSum([0, 0, 0, 0]))

    def test_threeSum_have_same(self):
        solution = Solution()
        self.assertEqual([[-1, -1, 2]], solution.threeSum([-1, -1, -1, -1, 2, 2, 2, 2]))

    def test_threeSum_not_all_small(self):
        solution = Solution()
        self.assertEqual([], solution.threeSum([-1, -1, -4]))

    def test_threeSum_not_all_large(self):
        solution = Solution()
        self.assertEqual([], solution.threeSum([0, 1, 2]))

    def test_threeSum_not_smallarray(self):
        solution = Solution()
        self.assertEqual([], solution.threeSum([]))
        self.assertEqual([], solution.threeSum([1]))
        self.assertEqual([], solution.threeSum([1, 2]))
        self.assertEqual([], solution.threeSum([0]))
        self.assertEqual([], solution.threeSum([0, 0]))
