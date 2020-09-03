import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _035_SearchInsertPosition import Solution

class Test_035_SearchInsertPosition(unittest.TestCase):
    def test_searchInsert_1(self):
        solution = Solution()
        self.assertEqual(2, solution.searchInsert([1,3,5,6], 5))

    def test_searchInsert_2(self):
        solution = Solution()
        self.assertEqual(1, solution.searchInsert([1,3,5,6], 2))

    def test_searchInsert_3(self):
        solution = Solution()
        self.assertEqual(4, solution.searchInsert([1,3,5,6], 7))

    def test_searchInsert_4(self):
        solution = Solution()
        self.assertEqual(0, solution.searchInsert([1,3,5,6], 0))
