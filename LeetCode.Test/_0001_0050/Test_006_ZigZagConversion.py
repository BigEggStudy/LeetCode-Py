import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _006_ZigZagConversion import Solution

class Test_006_ZigZagConversion(unittest.TestCase):
    def test_convert_1(self):
        input = "PAYPALISHIRING"
        rowNumber = 3

        solution = Solution()
        result = solution.convert(input, rowNumber)

        self.assertEqual("PAHNAPLSIIGYIR", result)


    def test_convert_2(self):
        input = "PAYPALISHIRING"
        rowNumber = 4

        solution = Solution()
        result = solution.convert(input, rowNumber)

        self.assertEqual("PINALSIGYAHRPI", result)


    def test_convert_1_row(self):
        input = "PAYPALISHIRING"
        rowNumber = 1

        solution = Solution()
        result = solution.convert(input, rowNumber)

        self.assertEqual("PAYPALISHIRING", result)


if __name__ == '__main__':
    unittest.main()
