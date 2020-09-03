import unittest

import sys
sys.path.append('LeetCode')

from ListNode import ListNode

def assertLinkList(expected: [], actual: ListNode):
    testCase = unittest.TestCase()

    testCase.assertIsNotNone(expected)
    testCase.assertIsNotNone(actual)
    testCase.assertTrue(len(expected) > 0)

    actualArray = []
    current = actual
    while current is not None:
        actualArray.append(current.val)
        current = current.next

    testCase.assertSequenceEqual(expected, actualArray)

def assertArray(expected: [], actual: [], ignoreLength: bool = False):
    testCase = unittest.TestCase()

    if not ignoreLength:
        testCase.assertEqual(len(expected), len(actual))

    for i in range(len(expected)):
        testCase.assertEqual(expected[i], actual[i])

def assertArray2D(expected: [[]], actual: [[]]):
    testCase = unittest.TestCase()

    testCase.assertIsNotNone(expected)
    testCase.assertIsNotNone(actual)

    testCase.assertEqual(len(expected), len(actual))
    for i, expected_sub in enumerate(expected):
        testCase.assertEqual(len(expected_sub), len(actual[i]))
        for j, actual_data in enumerate(actual[i]):
            testCase.assertEqual(expected[i][j], actual_data)
