import unittest

import sys
sys.path.append('LeetCode/_0051_0100')

from _071_SimplifyPath import Solution

class Test_071_SimplifyPath(unittest.TestCase):
    def test_simplifyPath_1(self):
        solution = Solution()
        self.assertEqual("/home", solution.simplifyPath("/home/"))

    def test_simplifyPath_2(self):
        solution = Solution()
        self.assertEqual("/", solution.simplifyPath("/../"))

    def test_simplifyPath_3(self):
        solution = Solution()
        self.assertEqual("/home/foo", solution.simplifyPath("/home//foo/"))

    def test_simplifyPath_4(self):
        solution = Solution()
        self.assertEqual("/c", solution.simplifyPath("/a/./b/../../c/"))

    def test_simplifyPath_5(self):
        solution = Solution()
        self.assertEqual("/c", solution.simplifyPath("/a/../../b/../c//.//"))

    def test_simplifyPath_6(self):
        solution = Solution()
        self.assertEqual("/a/b/c", solution.simplifyPath("/a//b////c/d//././/.."))
