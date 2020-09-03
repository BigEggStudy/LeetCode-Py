import unittest

import sys
sys.path.append('LeetCode/_0401_0450')
sys.path.append('LeetCode.Test')

from _0410_SplitArrayLargestSum import Solution
import AssertHelper

class Test_0410_SplitArrayLargestSum(unittest.TestCase):
    def test_splitArray(self):
        solution = Solution()
        result = solution.splitArray([ 7, 2, 5, 10, 8 ], 2)
        self.assertEqual(18, result)
