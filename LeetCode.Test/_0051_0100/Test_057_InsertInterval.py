import unittest

import sys
sys.path.append('LeetCode/_0051_0100')
sys.path.append('LeetCode.Test')

from _057_InsertInterval import Solution

import AssertHelper

class Test_057_InsertInterval(unittest.TestCase):
    def test_insert_1(self):
        solution = Solution()
        result = solution.insert([[1,3],[6,9]], [2,5])
        AssertHelper.assertArray2D([[1,5],[6,9]], result)

    def test_insert_2(self):
        solution = Solution()
        result = solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
        AssertHelper.assertArray2D([[1,2],[3,10],[12,16]], result)
