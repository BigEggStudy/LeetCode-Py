import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _067_AddBinary import Solution

class Test_067_AddBinary(unittest.TestCase):
    def test_addBinary_1(self):
        solution = Solution()
        self.assertEqual("100", solution.addBinary("11", "1"))

    def test_addBinary_2(self):
        solution = Solution()
        self.assertEqual("10101", solution.addBinary("1010", "1011"))
