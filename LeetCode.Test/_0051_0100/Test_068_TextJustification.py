import unittest

import sys
sys.path.append('LeetCode/_0051_0100')
sys.path.append('LeetCode.Test')

from _068_TextJustification import Solution
import AssertHelper

class Test_068_TextJustification(unittest.TestCase):
    def test_fullJustify_1(self):
        solution = Solution()
        result = solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
        AssertHelper.assertArray([
            "This    is    an",
            "example  of text",
            "justification.  "
        ], result)

    def test_fullJustify_2(self):
        solution = Solution()
        result = solution.fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
        AssertHelper.assertArray([
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ], result)

    def test_fullJustify_3(self):
        solution = Solution()
        result = solution.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)
        AssertHelper.assertArray([
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ], result)
