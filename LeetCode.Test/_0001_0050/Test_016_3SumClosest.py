import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _016_3SumClosest import Solution

class Test_016_3SumClosest(unittest.TestCase):
    def test_threeSumClosest_close(self):
        solution = Solution()
        self.assertEqual(2, solution.threeSumClosest([-1, 2, 1, -4], 1))

    def test_threeSumClosest_match(self):
        solution = Solution()
        self.assertEqual(2, solution.threeSumClosest([-1, 2, 1, -4], 2))

    def test_threeSumClosest_same_match(self):
        solution = Solution()
        self.assertEqual(3, solution.threeSumClosest([1, 1, 1, 1], 3))

    def test_threeSumClosest_same_notmatch(self):
        solution = Solution()
        self.assertEqual(3, solution.threeSumClosest([1, 1, 1, 1], 2))

    def test_threeSumClosest_zero(self):
        solution = Solution()
        self.assertEqual(0, solution.threeSumClosest([0, 0, 0], 2))
        self.assertEqual(0, solution.threeSumClosest([0, 0, 0], 0))
