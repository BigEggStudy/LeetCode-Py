import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _060_PermutationSequence import Solution

class Test_060_PermutationSequence(unittest.TestCase):
    def test_getPermutation_1(self):
        solution = Solution()
        self.assertEqual("213", solution.getPermutation(3, 3))

    def test_getPermutation_2(self):
        solution = Solution()
        self.assertEqual("2314", solution.getPermutation(4, 9))

    def test_getPermutation_3(self):
        solution = Solution()
        self.assertEqual("123", solution.getPermutation(3, 1))
        self.assertEqual("132", solution.getPermutation(3, 2))
        self.assertEqual("213", solution.getPermutation(3, 3))
        self.assertEqual("231", solution.getPermutation(3, 4))
        self.assertEqual("312", solution.getPermutation(3, 5))
        self.assertEqual("321", solution.getPermutation(3, 6))
