#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        l = s.split()
        if not l:
            return 0
        return len(l[-1])
