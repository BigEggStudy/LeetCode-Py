#-----------------------------------------------------------------------------
# Runtime: 120ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        newStr = "#"
        for char in s:
            newStr += char + "#"

        p = []
        range_max = 0
        center = 0
        longestPalindromeCenter = 0
        for index, char in enumerate(newStr):
            p.append(0)

            if range_max > index:
                p[index] = p[center * 2 - index] if p[center * 2 - index] < range_max - index else range_max - index
            while index - p[index] - 1 >= 0 and index + p[index] + 1 < len(newStr) and newStr[index - p[index] - 1] == newStr[index + p[index] + 1]:
                p[index] += 1

            if index + p[index] > range_max:
                range_max = index + p[index]
                center = index

            if p[index] > p[longestPalindromeCenter]:
                longestPalindromeCenter = index

        range = p[longestPalindromeCenter]
        return s[(longestPalindromeCenter - range) // 2 : (longestPalindromeCenter - range) // 2 + range]
