#-----------------------------------------------------------------------------
# Runtime: 36ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x

        last, result = 0.0, 1.0
        while last != result:
            last = result
            result = (result + x / result) / 2

        return int(last)
