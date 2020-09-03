import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _049_GroupAnagrams import Solution

import AssertHelper

class Test_049_GroupAnagrams(unittest.TestCase):
    def test_groupAnagrams(self):
        solution = Solution()
        result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        AssertHelper.assertArray2D([
            ["eat","tea","ate"],
            ["tan","nat"],
            ["bat"]
        ], result)
