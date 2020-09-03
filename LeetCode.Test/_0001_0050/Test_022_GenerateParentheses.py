import unittest

import sys
sys.path.append('LeetCode/_0001_0050')

from _022_GenerateParentheses import Solution

class Test_022_GenerateParentheses(unittest.TestCase):
    def test_generateParenthesis_0(self):
        solution = Solution()
        result = solution.generateParenthesis(0)
        self.assertEqual([""], result)

    def test_generateParenthesis_1(self):
        solution = Solution()
        result = solution.generateParenthesis(1)
        self.assertEqual(["()"], result)

    def test_generateParenthesis_2(self):
        solution = Solution()
        result = solution.generateParenthesis(2)
        self.assertEqual(["(())","()()"], result)

    def test_generateParenthesis_3(self):
        solution = Solution()
        result = solution.generateParenthesis(3)
        self.assertEqual(["((()))","(()())","(())()","()(())","()()()"], result)
