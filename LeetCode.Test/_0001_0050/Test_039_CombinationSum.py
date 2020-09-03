import unittest
import pytest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _039_CombinationSum import Solution

import AssertHelper

class Test_039_CombinationSum(unittest.TestCase):
    @pytest.mark.timeout(1)
    def test_combinationSum_1(self):
        candidates = [2,3,6,7]
        target = 7
        solution = Solution()
        AssertHelper.assertArray([ [2,2,3], [7] ], solution.combinationSum(candidates, target))

    @pytest.mark.timeout(1)
    def test_combinationSum_2(self):
        candidates = [2,3,5]
        target = 8
        solution = Solution()
        AssertHelper.assertArray([ [2,2,2,2], [2,3,3], [3,5] ], solution.combinationSum(candidates, target))

    @pytest.mark.timeout(1)
    def test_combinationSum_notExist(self):
        candidates = [2,3,6,7]
        target = 1
        solution = Solution()
        AssertHelper.assertArray([], solution.combinationSum(candidates, target))

    @pytest.mark.timeout(1)
    def test_combinationSum_emptyCandidates(self):
        candidates = []
        target = 5
        solution = Solution()
        AssertHelper.assertArray([], solution.combinationSum(candidates, target))
