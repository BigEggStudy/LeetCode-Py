import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _038_CountAndSay import Solution

class Test_038_CountAndSay(unittest.TestCase):
    def test_countAndSay_1(self):
        solution = Solution()
        self.assertEqual('1', solution.countAndSay(1))

    def test_countAndSay_2(self):
        solution = Solution()
        self.assertEqual('11', solution.countAndSay(2))

    def test_countAndSay_3(self):
        solution = Solution()
        self.assertEqual('21', solution.countAndSay(3))

    def test_countAndSay_4(self):
        solution = Solution()
        self.assertEqual('1211', solution.countAndSay(4))

    def test_countAndSay_5(self):
        solution = Solution()
        self.assertEqual('111221', solution.countAndSay(5))
