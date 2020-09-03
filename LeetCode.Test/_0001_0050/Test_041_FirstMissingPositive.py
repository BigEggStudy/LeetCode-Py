import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _041_FirstMissingPositive import Solution

class Test_041_FirstMissingPositive(unittest.TestCase):
    def test_firstMissingPositive_1(self):
        solution = Solution()
        self.assertEqual(3, solution.firstMissingPositive([1,2,0]))

    def test_firstMissingPositive_2(self):
        solution = Solution()
        self.assertEqual(2, solution.firstMissingPositive([3,4,-1,1]))

    def test_firstMissingPositive_3(self):
        solution = Solution()
        self.assertEqual(1, solution.firstMissingPositive([7,8,9,11,12]))

    def test_firstMissingPositive_onlyOne(self):
        solution = Solution()
        self.assertEqual(2, solution.firstMissingPositive([1]))

    def test_firstMissingPositive_onlyOne_2(self):
        solution = Solution()
        self.assertEqual(1, solution.firstMissingPositive([2]))

    def test_firstMissingPositive_onlyOne_3(self):
        solution = Solution()
        self.assertEqual(1, solution.firstMissingPositive([0]))
