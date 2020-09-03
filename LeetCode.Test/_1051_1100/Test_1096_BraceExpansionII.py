import unittest

import sys
sys.path.append('LeetCode/_1051_1100')
sys.path.append('LeetCode.Test')

from _1096_BraceExpansionII import Solution
import AssertHelper

class Test_1096_BraceExpansionII(unittest.TestCase):
    def test_braceExpansionII_1(self):
        solution = Solution()
        result = solution.braceExpansionII("{a,b}{c,{d,e}}")
        self.assertSequenceEqual(["ac","ad","ae","bc","bd","be"], result)

    def test_braceExpansionII_2(self):
        solution = Solution()
        result = solution.braceExpansionII("{{a,z},a{b,c},{ab,z}}")
        self.assertEqual(["a","ab","ac","z"], result)
