import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _058_LengthOfLastWord import Solution

class Test_058_LengthOfLastWord(unittest.TestCase):
    def test_lengthOfLastWord(self):
        solution = Solution()
        self.assertEqual(5, solution.lengthOfLastWord('Hello World'))

    def test_lengthOfLastWord_empty(self):
        solution = Solution()
        self.assertEqual(0, solution.lengthOfLastWord(''))

    def test_lengthOfLastWord_whitespace(self):
        solution = Solution()
        self.assertEqual(0, solution.lengthOfLastWord('    '))

    def test_lengthOfLastWord_tailSpace(self):
        solution = Solution()
        self.assertEqual(5, solution.lengthOfLastWord('Hello World   '))
