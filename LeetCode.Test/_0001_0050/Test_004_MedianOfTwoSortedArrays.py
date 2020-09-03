import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _004_MedianOfTwoSortedArrays import Solution

class Test_004_MedianOfTwoSortedArrays(unittest.TestCase):
    def test_findMedianSortedArrays_odd(self):
        nums1 = [1, 2]
        nums2 = [3, 4, 5]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)

        self.assertEqual(3, result)


    def test_findMedianSortedArraysTest_even(self):
        nums1 = [1, 2, 3, 4]
        nums2 = [5, 6, 7, 8]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)

        self.assertEqual(4.5, result)

    def test_findMedianSortedArrays(self):
        nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        nums2 = [0, 6]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)

        self.assertEqual(10.5, result)


    def test_findMedianSortedArraysTest_num1Empty(self):
        nums1 = []
        nums2 = [1, 2, 3]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)

        self.assertEqual(2, result)


    def test_findMedianSortedArraysTest_num2Empty(self):
        nums1 = [1, 2, 3]
        nums2 = []

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)

        self.assertEqual(2, result)


    def test_findMedianSortedArraysTest_num1Empty_nums2SingleItem(self):
        nums1 = []
        nums2 = [1]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)

        self.assertEqual(1, result)


    def test_findMedianSortedArraysTest_num2Empty_nums1SingleItem(self):
        nums1 = [1]
        nums2 = []

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)

        self.assertEqual(1, result)


    def test_findMedianSortedArraysTest_nums1SingleItem_odd(self):
        nums1 = [1]
        nums2 = [2, 3, 4, 5, 6, 7]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)

        self.assertEqual(4, result)


    def test_findMedianSortedArraysTest_nums1SingleItem_even(self):
        nums1 = [1]
        nums2 = [2, 3, 4, 5, 6]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)

        self.assertEqual(3.5, result)


    def test_findMedianSortedArraysTest_nums2SingleItem_odd(self):
        nums1 = [2, 3, 4, 5, 6, 7]
        nums2 = [1]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)

        self.assertEqual(4, result)


    def test_findMedianSortedArraysTest_nums2SingleItem_even(self):
        nums1 = [2, 3, 4, 5, 6]
        nums2 = [1]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)

        self.assertEqual(3.5, result)


    def test_findMedianSortedArraysTest_mixedArray(self):
        nums1 = [2]
        nums2 = [1, 3, 4]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)

        self.assertEqual(2.5, result)


    def test_findMedianSortedArraysTest_duplicateItems(self):
        nums1 = [1, 1, 3, 3]
        nums2 = [1, 1, 3, 3]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)

        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()
