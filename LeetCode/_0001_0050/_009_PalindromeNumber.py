#-----------------------------------------------------------------------------
# Runtime: 68ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x >= 0 and x == int(str(x)[::-1])
