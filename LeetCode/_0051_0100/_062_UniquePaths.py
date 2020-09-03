#-----------------------------------------------------------------------------
# Runtime: 28ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rest = min(m, n) - 1
        if rest == 0: return 1
        if rest == 1: return m + n - 2

        result = 1
        temp = m + n - 2
        i = rest
        while i > 0:
            result *= temp
            temp -=1
            i -= 1

        while rest > 1:
            result //= rest
            rest -= 1

        return result
