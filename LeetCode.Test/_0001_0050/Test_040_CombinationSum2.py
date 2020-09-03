import unittest
import pytest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _040_CombinationSum2 import Solution

import AssertHelper

class Test_040_CombinationSum2(unittest.TestCase):
    @pytest.mark.timeout(1)
    def test_combinationSum2_1(self):
        candidates = [10,1,2,7,6,1,5]
        target = 8
        solution = Solution()
        AssertHelper.assertArray([ [1, 1, 6], [1, 2, 5], [1, 7], [2, 6] ], solution.combinationSum2(candidates, target))

    @pytest.mark.timeout(1)
    def test_combinationSum2_2(self):
        candidates = [2,5,2,1,2]
        target = 5
        solution = Solution()
        AssertHelper.assertArray([ [1,2,2], [5] ], solution.combinationSum2(candidates, target))

    @pytest.mark.timeout(1)
    def test_combinationSum2_notExist(self):
        candidates = [3,6,7]
        target = 5
        solution = Solution()
        AssertHelper.assertArray([], solution.combinationSum2(candidates, target))

    @pytest.mark.timeout(1)
    def test_combinationSum2_emptyCandidates(self):
        candidates = []
        target = 5
        solution = Solution()
        AssertHelper.assertArray([], solution.combinationSum2(candidates, target))
