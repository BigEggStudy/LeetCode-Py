import unittest
import pytest

import sys
sys.path.append('LeetCode/_0001_0050')

from _033_SearchInRotatedSortedArray import Solution

class Test_033_SearchInRotatedSortedArray(unittest.TestCase):
    @pytest.mark.timeout(1)
    def test_search_1(self):
        solution = Solution()
        self.assertEqual(4, solution.search([4,5,6,7,0,1,2], 0))

    @pytest.mark.timeout(1)
    def test_search_2(self):
        solution = Solution()
        self.assertEqual(5, solution.search([4,5,6,7,0,1,2], 1))

    @pytest.mark.timeout(1)
    def test_search_3(self):
        solution = Solution()
        self.assertEqual(6, solution.search([4,5,6,7,0,1,2], 2))

    @pytest.mark.timeout(1)
    def test_search_4(self):
        solution = Solution()
        self.assertEqual(0, solution.search([4,5,6,7,0,1,2], 4))

    @pytest.mark.timeout(1)
    def test_search_5(self):
        solution = Solution()
        self.assertEqual(1, solution.search([4,5,6,7,0,1,2], 5))

    @pytest.mark.timeout(1)
    def test_search_6(self):
        solution = Solution()
        self.assertEqual(2, solution.search([4,5,6,7,0,1,2], 6))

    @pytest.mark.timeout(1)
    def test_search_7(self):
        solution = Solution()
        self.assertEqual(3, solution.search([4,5,6,7,0,1,2], 7))

    @pytest.mark.timeout(1)
    def test_search_8(self):
        solution = Solution()
        self.assertEqual(0, solution.search([5, 1, 3], 5))

    @pytest.mark.timeout(1)
    def test_search_unwraped(self):
        solution = Solution()
        self.assertEqual(0, solution.search([0,1,2,4,5,6,7], 0))
        self.assertEqual(1, solution.search([0,1,2,4,5,6,7], 1))
        self.assertEqual(2, solution.search([0,1,2,4,5,6,7], 2))
        self.assertEqual(3, solution.search([0,1,2,4,5,6,7], 4))
        self.assertEqual(4, solution.search([0,1,2,4,5,6,7], 5))
        self.assertEqual(5, solution.search([0,1,2,4,5,6,7], 6))
        self.assertEqual(6, solution.search([0,1,2,4,5,6,7], 7))

    @pytest.mark.timeout(1)
    def test_search_notFound(self):
        solution = Solution()
        self.assertEqual(-1, solution.search([4,5,6,7,0,1,2], 3))
        self.assertEqual(-1, solution.search([4,5,6,7,0,1,2], 8))
        self.assertEqual(-1, solution.search([4,5,6,7,0,1,2], -1))

    @pytest.mark.timeout(1)
    def test_search_unwraped_notFound(self):
        solution = Solution()
        self.assertEqual(-1, solution.search([0,1,2,4,5,6,7], 3))
        self.assertEqual(-1, solution.search([0,1,2,4,5,6,7], 8))
        self.assertEqual(-1, solution.search([0,1,2,4,5,6,7], -1))
