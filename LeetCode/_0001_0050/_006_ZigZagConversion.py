#-----------------------------------------------------------------------------
# Runtime: 100ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or len(s) <= 1:
            return s

        result = ""
        cycle = 2 * numRows - 2
        for i in range(0, numRows):
            for j in range(i, len(s), cycle):
                result += s[j]
                if i == 0 or i == numRows - 1 or j + cycle - i * 2 >= len(s):
                    continue

                result += s[j + cycle - i * 2]

        return result
