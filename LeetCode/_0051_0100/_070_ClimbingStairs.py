#-----------------------------------------------------------------------------
# Runtime: 28ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4: return n

        n1, n2 = 2, 3
        for _ in range(4, n + 1):
            n1, n2 = n2, n1 + n2

        return n2
