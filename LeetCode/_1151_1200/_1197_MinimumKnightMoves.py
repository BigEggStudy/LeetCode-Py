#-----------------------------------------------------------------------------
# Runtime: 36ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x < y:
            x, y = y, x

        if x == 1 and y == 0:
            return 3
        if x == 2 and y == 2:
            return 4

        delta = x - y
        if y > delta:
            return delta - 2 * ((delta - y) // 3)
        else:
            return delta - 2 * ((delta - y) // 4)
