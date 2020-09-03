import unittest

import sys
sys.path.append('LeetCode/_0801_0850')
sys.path.append('LeetCode.Test')

from _0843_GuesstheWord import Solution, Master
import AssertHelper

class Test_0843_GuesstheWord(unittest.TestCase):
    def test_findSecretWord_1(self):
        wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
        m = Master("acckzz", wordlist)

        solution = Solution()
        solution.findSecretWord(wordlist, m)

        self.assertTrue(m.guessCount <= 10)
