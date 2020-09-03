import unittest

import sys
sys.path.append('LeetCode/_1151_1200')
sys.path.append('LeetCode.Test')

from _1197_MinimumKnightMoves import Solution
import AssertHelper

class Test_1197_MinimumKnightMoves(unittest.TestCase):
    def test_minKnightMoves_1(self):
        solution = Solution()
        result = solution.minKnightMoves(2, 1)
        self.assertEqual(1, result)

    def test_minKnightMoves_2(self):
        solution = Solution()
        result = solution.minKnightMoves(5, 5)
        self.assertEqual(4, result)

    def test_minKnightMoves_3(self):
        solution = Solution()
        result = solution.minKnightMoves(0, 0)
        self.assertEqual(0, result)
