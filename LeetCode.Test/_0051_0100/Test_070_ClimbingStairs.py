import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _070_ClimbingStairs import Solution

class Test_070_ClimbingStairs(unittest.TestCase):
    def test_climbStairs_1(self):
        solution = Solution()
        self.assertEqual(1, solution.climbStairs(1))

    def test_climbStairs_2(self):
        solution = Solution()
        self.assertEqual(2, solution.climbStairs(2))

    def test_climbStairs_3(self):
        solution = Solution()
        self.assertEqual(3, solution.climbStairs(3))

    def test_climbStairs_4(self):
        solution = Solution()
        self.assertEqual(5, solution.climbStairs(4))

    def test_climbStairs_5(self):
        solution = Solution()
        self.assertEqual(8, solution.climbStairs(5))

    def test_climbStairs_6(self):
        solution = Solution()
        self.assertEqual(13, solution.climbStairs(6))

    def test_climbStairs_7(self):
        solution = Solution()
        self.assertEqual(21, solution.climbStairs(7))
