import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _013_RomanToInteger import Solution

class Test_013_RomanToInteger(unittest.TestCase):
    def test_romanToInt_3(self):
        solution = Solution()
        self.assertEqual(3, solution.romanToInt('III'))

    def test_romanToInt_4(self):
        solution = Solution()
        self.assertEqual(4, solution.romanToInt('IV'))

    def test_romanToInt_8(self):
        solution = Solution()
        self.assertEqual(8, solution.romanToInt('VIII'))

    def test_romanToInt_9(self):
        solution = Solution()
        self.assertEqual(9, solution.romanToInt('IX'))

    def test_romanToInt_47(self):
        solution = Solution()
        self.assertEqual(47, solution.romanToInt('XLVII'))

    def test_romanToInt_58(self):
        solution = Solution()
        self.assertEqual(58, solution.romanToInt('LVIII'))

    def test_romanToInt_83(self):
        solution = Solution()
        self.assertEqual(83, solution.romanToInt('LXXXIII'))

    def test_romanToInt_93(self):
        solution = Solution()
        self.assertEqual(93, solution.romanToInt('XCIII'))

    def test_romanToInt_1994(self):
        solution = Solution()
        self.assertEqual(1994, solution.romanToInt('MCMXCIV'))
