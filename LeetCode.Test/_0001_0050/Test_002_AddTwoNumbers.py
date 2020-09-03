import unittest

import sys
sys.path.append('LeetCode/_0001_0050')
sys.path.append('LeetCode.Test')

from _002_AddTwoNumbers import Solution

import TestHelper, AssertHelper

class Test_002_AddTwoNumbers(unittest.TestCase):
    def test_addTwoNumbers(self):
        link = TestHelper.generateLinkList([2, 4, 3])

        solution = Solution()
        result = solution.addTwoNumbers(link, link)

        AssertHelper.assertLinkList([4, 8, 6], result)


    def test_addTwoNumbers_zero(self):
        link = TestHelper.generateLinkList([0])

        solution = Solution()
        result = solution.addTwoNumbers(link, link)

        AssertHelper.assertLinkList([0], result)


    def test_addTwoNumbers_hasCarry(self):
        link1 = TestHelper.generateLinkList([2, 4, 3])
        link2 = TestHelper.generateLinkList([5, 6, 4])

        solution = Solution()
        result = solution.addTwoNumbers(link1, link2)

        AssertHelper.assertLinkList([7, 0, 8], result)


    def test_addTwoNumbers_hasMultipleCarry(self):
        link1 = TestHelper.generateLinkList([1])
        link2 = TestHelper.generateLinkList([9, 9])

        solution = Solution()
        result = solution.addTwoNumbers(link1, link2)

        AssertHelper.assertLinkList([0, 0, 1], result)


    def test_addTwoNumbers_firstNumCarry(self):
        link1 = TestHelper.generateLinkList([3, 4, 4])
        link2 = TestHelper.generateLinkList([3, 4, 6])

        solution = Solution()
        result = solution.addTwoNumbers(link1, link2)

        AssertHelper.assertLinkList([6, 8, 0, 1], result)


    def test_addTwoNumbers_l1Long(self):
        link1 = TestHelper.generateLinkList([2, 4, 3, 1])
        link2 = TestHelper.generateLinkList([5, 6, 4])

        solution = Solution()
        result = solution.addTwoNumbers(link1, link2)

        AssertHelper.assertLinkList([7, 0, 8, 1], result)


    def test_addTwoNumbers_l1Long_withZero(self):
        link1 = TestHelper.generateLinkList([1, 8])
        link2 = TestHelper.generateLinkList([0])

        solution = Solution()
        result = solution.addTwoNumbers(link1, link2)

        AssertHelper.assertLinkList([1, 8], result)


    def test_addTwoNumbers_l1None(self):
        link1 = TestHelper.generateLinkList(None)
        link2 = TestHelper.generateLinkList([1, 8])

        solution = Solution()
        result = solution.addTwoNumbers(link1, link2)

        AssertHelper.assertLinkList([1, 8], result)


    def test_addTwoNumbers_l2Long(self):
        link1 = TestHelper.generateLinkList([5, 6, 4])
        link2 = TestHelper.generateLinkList([2, 4, 3, 1])

        solution = Solution()
        result = solution.addTwoNumbers(link1, link2)

        AssertHelper.assertLinkList([7, 0, 8, 1], result)


    def test_addTwoNumbers_l1Long_withZero(self):
        link1 = TestHelper.generateLinkList([0])
        link2 = TestHelper.generateLinkList([1, 8])

        solution = Solution()
        result = solution.addTwoNumbers(link1, link2)

        AssertHelper.assertLinkList([1, 8], result)


    def test_addTwoNumbers_l1None(self):
        link1 = TestHelper.generateLinkList([1, 8])
        link2 = TestHelper.generateLinkList(None)

        solution = Solution()
        result = solution.addTwoNumbers(link1, link2)

        AssertHelper.assertLinkList([1, 8], result)


if __name__ == '__main__':
    unittest.main()
