#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or n == 1:
            return x
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1 / x

        result = 1.0
        while n > 0:
            if n & 0x1 == 1:
                result *= x
            n = n >> 1
            x = x * x

        return result
