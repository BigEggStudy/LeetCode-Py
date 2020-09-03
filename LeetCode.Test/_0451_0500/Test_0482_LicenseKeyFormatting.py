import unittest

import sys
sys.path.append('LeetCode/_0451_0500')
sys.path.append('LeetCode.Test')

from _0482_LicenseKeyFormatting import Solution
import AssertHelper

class Test_0482_LicenseKeyFormatting(unittest.TestCase):
    def test_licenseKeyFormatting_1(self):
        solution = Solution()
        result = solution.licenseKeyFormatting("5F3Z-2e-9-w", 4)
        self.assertEqual("5F3Z-2E9W", result)

    def test_licenseKeyFormatting_2(self):
        solution = Solution()
        result = solution.licenseKeyFormatting("2-5g-3-J", 2)
        self.assertEqual("2-5G-3J", result)
