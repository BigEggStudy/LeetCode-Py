import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _012_IntegerToRoman import Solution

class Test_012_IntegerToRoman(unittest.TestCase):
    def test_intToRoman_3(self):
        solution = Solution()
        self.assertEqual("III", solution.intToRoman(3))

    def test_intToRoman_4(self):
        solution = Solution()
        self.assertEqual("IV", solution.intToRoman(4))

    def test_intToRoman_8(self):
        solution = Solution()
        self.assertEqual("VIII", solution.intToRoman(8))

    def test_intToRoman_9(self):
        solution = Solution()
        self.assertEqual("IX", solution.intToRoman(9))

    def test_intToRoman_47(self):
        solution = Solution()
        self.assertEqual("XLVII", solution.intToRoman(47))

    def test_intToRoman_58(self):
        solution = Solution()
        self.assertEqual("LVIII", solution.intToRoman(58))

    def test_intToRoman_83(self):
        solution = Solution()
        self.assertEqual("LXXXIII", solution.intToRoman(83))

    def test_intToRoman_93(self):
        solution = Solution()
        self.assertEqual("XCIII", solution.intToRoman(93))

    def test_intToRoman_1994(self):
        solution = Solution()
        self.assertEqual("MCMXCIV", solution.intToRoman(1994))
