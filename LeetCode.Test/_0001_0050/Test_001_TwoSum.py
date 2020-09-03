import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _001_TwoSum import Solution

class Test_001_TwoSum(unittest.TestCase):
    def setUp(self):
        self.largeArray = []
        for i in range(20000):
            self.largeArray.append(i * 2)


    def test_twoSum_ordered(self):
        nums = [ 2, 7, 11, 15 ]
        target = 9

        solution = Solution()
        result = solution.twoSum(nums, target)

        self.assertEqual(2, len(result))
        self.assertSequenceEqual([0, 1], result)


    def test_twoSum_unordered(self):
        nums = [ 5, 75, 25 ]
        target = 100

        solution = Solution()
        result = solution.twoSum(nums, target)

        self.assertEqual(2, len(result))
        self.assertSequenceEqual([1, 2], result)


    def test_twoSum_dpulicate(self):
        nums = [ 5, 5, 15, 30 ]
        target = 20

        solution = Solution()
        result = solution.twoSum(nums, target)

        self.assertEqual(2, len(result))
        self.assertSequenceEqual([1, 2], result)


    def test_twoSum_all_same(self):
        nums = [ 5, 5, 55 ]
        target = 10

        solution = Solution()
        result = solution.twoSum(nums, target)

        self.assertEqual(2, len(result))
        self.assertSequenceEqual([0, 1], result)


    def test_twoSum_no_target(self):
        nums = [ 2, 7, 11, 15 ]
        target = 5

        solution = Solution()
        result = solution.twoSum(nums, target)

        self.assertEqual(0, len(result))


    def test_twoSum_larget_array(self):
        nums = self.largeArray
        target = 19082

        solution = Solution()
        result = solution.twoSum(nums, target)

        self.assertEqual(2, len(result))
        self.assertSequenceEqual([4770, 4771], result)


    def test_twoSum_larget_array_no_target(self):
        nums = self.largeArray
        target = 19081

        solution = Solution()
        result = solution.twoSum(nums, target)

        self.assertEqual(0, len(result))


if __name__ == '__main__':
    unittest.main()
