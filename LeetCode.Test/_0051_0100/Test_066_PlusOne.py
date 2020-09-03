import unittest

import sys
sys.path.append('LeetCode/_0051_0100')
sys.path.append('LeetCode.Test')

from _066_PlusOne import Solution
import AssertHelper

class Test_066_PlusOne(unittest.TestCase):
    def test_plusOne_1(self):
        solution = Solution()
        AssertHelper.assertArray([1,2,4], solution.plusOne([1,2,3]))

    def test_plusOne_2(self):
        solution = Solution()
        AssertHelper.assertArray([4,3,2,2], solution.plusOne([4,3,2,1]))

    def test_plusOne_zero(self):
        solution = Solution()
        AssertHelper.assertArray([1], solution.plusOne([0]))

    def test_plusOne_withCarry(self):
        solution = Solution()
        AssertHelper.assertArray([3,0], solution.plusOne([2,9]))

    def test_plusOne_withFirstCarry(self):
        solution = Solution()
        AssertHelper.assertArray([1,0], solution.plusOne([9]))
