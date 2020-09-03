#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

import sys

INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1
POSITIVE_OVERFLOW = INT_MAX // 10
NAGATIVE_OVERFLOW = INT_MIN // 10

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)

        result = 0
        while (x != 0):
            if (result > POSITIVE_OVERFLOW or result < NAGATIVE_OVERFLOW):
                return 0
            result = result * 10 + x % 10
            x = x // 10

        return sign * result
